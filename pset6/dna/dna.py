import sys
import csv


def checking_for_each_STR(seq, header):
    occurrences = []
    # Counting occurrences for each STR in header
    for i in range(1, len(header)):
        count = counter(seq, header[i])
        occurrences.append(str(count))
    return occurrences 
    

def counter(seq, STR):
    repetition = []
    j = len(STR)
    # Iterating over seq by single increment
    for i in range(len(seq)):
        check = seq[i:i+j]
        # If there's a match 
        if check == STR:
            counter = 0
            # Check next presence of sequence and count it
            for l in range(i, len(seq), j):
                check1 = seq[l:j+l]
                if check1 == STR:
                    counter += 1
                else:
                    break
            repetition.append(counter)
    if repetition:
        repetition.sort()
        highest = repetition[-1]
        return highest
    else:
        return 0
    

# Checking command-line args
if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    sys.exit(0)

# Create a list of dictionary's of people's database from reading .csv file
database = []

# Reading .csv file using reader 
with open(sys.argv[1], "r") as csv_file:
    reader = csv.reader(csv_file)
    header = next(reader)
    for row in reader:
        database.append(row)

# Reading text file 
text_file = open(sys.argv[2])
seq = text_file.read()

 
occurrences = checking_for_each_STR(seq, header)


for i in range(len(database)):
    check = database[i].copy()
    check.pop(0)
    if check == occurrences:
        print(database[i][0])
        sys.exit()

print("No match")