-- Keep a log of any SQL queries you execute as you solve the mystery.

.schema
/* To explore the schema to understand what
 data is available and how table connect with each other. */

-- Clues:
-- July 28, 2020 (28/07/2020)
-- Chamberlin Street

-- First let's look at crime scene reports to find out what 
-- happened at Chamberlin Street on 28 july 2020
select * from crime_scene_reports
where year = 2020 and month = 7 and day = 28 and street = 'Chamberlin Street';

-- Clues:
-- 1. 3 witness
-- 2. Crime Time 10:15 am
-- 3. Interview script contains 'Courthouse'
-- 4. Crime location Courthouse

-- Lets look at intervies of people at that day and whose trascript contains 'courthouse'
select transcript from interviews
where year = 2020 and month = 7 and day = 28 and transcript like "%courthouse%";


--Output:
        -- 161	Ruth	2020	7	28	Sometime within ten minutes of the theft, I saw the thief get into a car in the courthouse parking lot and drive away.
        --  If you have security footage from the courthouse parking lot, you might want to look for cars that left the parking lot in that time frame.

        -- 162	Eugene	2020	7	28	I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at the courthouse,
        --  I was walking by the ATM on Fifer Street and saw the thief there withdrawing some money.

        -- 163	Raymond	2020	7	28	As the thief was leaving the courthouse, they called someone who talked to them for less than a minute. In the call, I heard the thief 
        -- say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the fli...

-- Clues:
-- 1. after 10 min (10:15am + 10) check paking lot security cams
-- 2. Thief widthdraw money from ATM on Fifer Street (Before crime earlier this morning)
-- 3. Thief called someone for < 1 min call-time earliest flight out of the town (after crime as thief was leaving)


-- Check courthouse security logs between 10:15 am and 10:25 am
select * from courthouse_security_logs 
where year = 2020 and month = 7 and day = 28 and hour = 10 and minute between 15 and 25

-- Output:
        -- 260	2020	7	28	10	16	exit	5P2BI95
        -- 261	2020	7	28	10	18	exit	94KL13X
        -- 262	2020	7	28	10	18	exit	6P58WS2
        -- 263	2020	7	28	10	19	exit	4328GD8
        -- 264	2020	7	28	10	20	exit	G412CB7
        -- 265	2020	7	28	10	21	exit	L93JTIZ
        -- 266	2020	7	28	10	23	exit	322W7JE
        -- 267	2020	7	28	10	23	exit	0NTHK55

-- Now let's narrow down the person list from ATM transactions

-- Checking ATM transactions on that day at Fifer Street with license plate that we retrived from security logs
create view [Sus list] as
select *  from people
join bank_accounts on people.id = bank_accounts.person_id
join atm_transactions on bank_accounts.account_number = atm_transactions.account_number
where people.license_plate in 
    (select courthouse_security_logs.license_plate from courthouse_security_logs 
    where year = 2020 
    and month = 7 
    and day = 28 
    and hour = 10 
    and minute between 15 and 25)
and atm_transactions.day =28 
and atm_transactions.month = 7 
and atm_transactions.year = 2020 
and atm_transactions.atm_location = 'Fifer Street'

--Output: 
        -- 686048	Ernest	    (367) 555-5533	5773159633	94KL13X	49610011	686048	2010	267	49610011	2020	7	28	Fifer Street	withdraw	50
        -- 514354	Russell	    (770) 555-1861	3592750733	322W7JE	26013199	514354	2012	336	26013199	2020	7	28	Fifer Street	withdraw	35
        -- 396669	Elizabeth	(829) 555-5269	7049073643	L93JTIZ	25506511	396669	2014	288	25506511	2020	7	28	Fifer Street	withdraw	20
        -- 467400	Danielle	(389) 555-5198	8496433585	4328GD8	28500762	467400	2014	246	28500762	2020	7	28	Fifer Street	withdraw	48

-- Checking phone number and who they called from Sus list at time frame 10:15am to 10:25am
select sus_list.phone_number,duration,name,receiver from sus_list
join phone_calls on phone_calls.caller = sus_list.phone_number
where duration <= 60
and phone_calls.year = 2020 and phone_calls.month = 7 and phone_calls.day = 28

-- Output:
        -- (367) 555-5533	45	Ernest	(375) 555-8161
        -- (770) 555-1861	49	Russell	(725) 555-3243


--Suspect List:
-- 1. Ernest
-- 2. Russell

-- Let's find the receiver of calls
select * from people
where phone_number in ('(375) 555-8161','(725) 555-3243')

--Output:
        -- 847116	Philip	    (725) 555-3243	3391710505	GW362R6
        -- 864400	Berthold	(375) 555-8161	NULL	    4V16VO0

-- Checking flight leaving after 10:25 am from Fiftyville 
select flights.id,origin_airport_id, airports.city, hour, minute from flights 
join airports on airports.id = flights.origin_airport_id
where year = 2020 
and month = 7
and day = 29
and city = 'Fiftyville' 
order by hour

-- Output:
        -- 36	8	Fiftyville	8	20
        -- 43	8	Fiftyville	9	30
        -- 23	8	Fiftyville	12	15
        -- 53	8	Fiftyville	15	20
        -- 18	8	Fiftyville	16	0
-- So the latest flight is on 8:20 am and flight id is 36
-- Checking passenger details on flight id 36 and wether its matching with any suspect
select name, phone_number, sus_list.passport_number, passengers.passport_number, flight_id from sus_list
join passengers on passengers.passport_number = sus_list.passport_number
where flight_id = 36

--Output:
    -- Ernest	    (367) 555-5533	5773159633	36
    -- Danielle	    (389) 555-5198	8496433585	36

-- Therefore the thief is Ernest
-- Ernest is headed to can be found out by checking destination city of filght 36

select flights.id, destination_airport_id, full_name, city from flights
join airports on airports.id = flights.destination_airport_id
where flights.id  = 36

-- Ernest is headed to Heathrow Airport, London
-- Berthold is the accomplice

