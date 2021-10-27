import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
import flask
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

os.environ["API_KEY"] = "pk_509fa91459a84d9394a69b0bc1d45481"
# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Retriving data from database
    info = db.execute("SELECT symbol, sum(qty) as Total_Qty FROM transactions WHERE user_id = ? GROUP BY symbol",session["user_id"])
    
    # Removing stocks with total qty of shares 0
    info = list(filter(lambda e : e['Total_Qty'] != 0,info))
    
    # Updating list of dict with latest price and name
    for i in range(len(info)):
        share_info = lookup(info[i]['symbol'])
        info[i]['name'] = share_info['name']
        info[i]["price"] = share_info['price']
        info[i]["total"] = round(share_info['price'] * info[i]['Total_Qty'],2)  
    
    # Calculating total cash available in user account
    cash = float(db.execute("SELECT cash from users where id = ?", session['user_id'])[0]['cash'])

    return render_template("index.html", list1 = info,cash = cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # Rendering buy page
    if request.method == "GET":
        return render_template("buy.html")

    # When user clicks buy button
    if request.method == "POST":
        info = lookup(request.form.get("symbol"))
        
        # For invalid symbols
        if info == None:
            flash("Invalid Symbol")
            return render_template("buy.html")
        
        # Current price of stocks
        price = info["price"]

        # Finding total value of shares to be bought by user
        qty = int(request.form.get('shares'))
        value = int(price) * qty
        
        # Retriving cash available
        userid = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?",userid)[0]['cash']
        
        # Check for insufficient funds
        if value > cash:
            flash("Insufficient funds")
            return render_template("buy.html")
        
        # Purchasing shares
        db.execute("INSERT INTO transactions(user_id,type,symbol,name,price,qty,datetime) VALUES(?,?,?,?,?,?,datetime('now', 'localtime'))",userid,"buy",info["symbol"],info["name"],price,qty)
        db.execute("UPDATE users SET cash = ? WHERE id = ?",cash-value,userid)
        flash("Stocks purchased successfully")
        return redirect("/")

    return apology("Something went wrong", 403)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # Retriving data from database
    info = db.execute("SELECT * FROM transactions where user_id = ?",session["user_id"])

    return render_template("history.html", list1 = info)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # Rendering Quote page
    if request.method == "GET":
        return render_template("quote.html")
    
    # When user clicks quote button
    if request.method == "POST":
        info = lookup(request.form.get("symbol"))

        # If lookup return none
        if info == None:
            flash("Symbol not found")
            return render_template("quote.html")

        company = info['name']
        symbol = info['symbol']
        price = usd(info['price'])
        return render_template('quoted.html',company = company, symbol = symbol, price = price)

    return apology("Something went wrong", 403)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Rendering Register page
    if request.method == 'GET':
        return render_template("register.html")
    
    # When user click register button
    if request.method == "POST":
        # Checks for valid user inputs
        if not request.form.get('username'):
            flash("Username is missing")
            return render_template("register.html")

        # Getting username from form
        username = request.form.get("username")

        if not request.form.get('password'):
            flash('Password is missing')
            return render_template("register.html")

        if request.form.get("password")  != request.form.get("re-password"):
            flash("Password don't match")
            return render_template("register.html")
        
        # Hasing password
        password = generate_password_hash(request.form.get('password'))

        # Creating new user in database
        db.execute("INSERT INTO users(username,hash) values (?,?)", username,password)
        return render_template('login.html')

    return apology("Something went wrong", 403)


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # Rendering sell page
    if request.method == "GET":
        return render_template("sell.html")

    # When user clicks buy button
    if request.method == "POST":
        info = lookup(request.form.get("symbol"))
        
        # For invalid symbols
        if info == None:
            flash("Invalid Symbol")
            return render_template("buy.html")
        
        # Current price of stocks
        cur_price = info["price"]
              
        # Finding total value of shares to be bought by user
        qty = int(request.form.get('shares'))
        value = int(cur_price) * qty
        
         # Look for amount of stocks in user account
        amt_shares_in_database =  db.execute("SELECT sum(qty) as Total_Qty FROM transactions WHERE user_id = ? and symbol = ? GROUP BY symbol",session["user_id"],info['symbol'])[0]['Total_Qty']
        
        # Check for insufficient shares
        if qty > amt_shares_in_database:
            flash("Insufficient shares")
            return render_template("sell.html")
        
        # Retriving cash available
        cash = db.execute("SELECT cash FROM users WHERE id = ?",session['user_id'])[0]['cash']
        
        # Updating database after selling shares
        db.execute("INSERT INTO transactions(user_id,type,symbol,name,price,qty,datetime) VALUES(?,?,?,?,?,?,datetime('now', 'localtime'))",session['user_id'],"sell",info["symbol"],info["name"],cur_price,(-qty))
        db.execute("UPDATE users SET cash = ? WHERE id = ?",cash+value,session['user_id'])
        flash("Stocks sold successfully")
        return redirect("/")
    return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
