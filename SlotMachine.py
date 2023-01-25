import random

MAX_LINES = 3
MAX_BET = 100
MINIMUM_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_values = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def get_slot_maching_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    columns = [[],[],[]]
    for col in range(cols):
        column = []
        copy = all_symbols[:]
        for row in range(rows):
            value = random.choice(copy)
            column.append(value)
            copy.remove(value)
        columns[col] = column[:]
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,col in enumerate(columns):
            if i!=len(columns)-1:
                print(col[row], "|",end = "")
            else:
                print(col[row],end="\n")

def deposit():
    while True:
        amount = input("Insert amount: ");
        if amount.isdigit():
            amount = int(amount)
            if amount >0:
                break
            else:
                print("Amount must be >0")
        else:
            print("Enter a number!")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Insert nr of lines(1 -> "+str(MAX_LINES)+ "): " );
        if lines.isdigit():
            lines = int(lines)
            if lines >0 and lines<=MAX_LINES:
                break
            else:
                print("Nr of lines must be > 0 AND < "+str(MAX_LINES))
        else:
            print("Enter a number!")
    return lines
def check_winnings(columns,lines,bet,values):
    total = 0
    nr_of_lines = 0
    for line in range(lines):
        setA = set()
        for col in columns:
            setA.add(col[line])
        if len(setA) == 1:
            nr_of_lines+=1
            for elem in setA:
                total+=values[elem]*bet
    return total if nr_of_lines == lines else 0


def get_bet(lines,balance):
    while True:
        amount = input("What would you like to bet on each line?$ ");
        if amount.isdigit():
            amount = int(amount)
            if amount >= MINIMUM_BET and amount<=MAX_BET and amount*lines <= balance :
                break
            elif amount*lines > balance:
                print("You must choose something lower,your amount bet is over your left balance!")
                print(f"Current balance is:{balance}")
            else:
                print("The amount must be between "+str(MINIMUM_BET)+"$ and "+str(MAX_BET)+"$")
        else:
            print("Enter a number!")
    return amount
def main():
    balance = deposit()
    while balance>0:
        lines = get_number_of_lines()
        bet_amount = get_bet(lines,balance)
        if lines*bet_amount:
            print(f"You are betting ${bet_amount} on {lines}.Total bet is equal to:{lines*bet_amount}")
        slots = get_slot_maching_spin(ROWS,COLS,symbol_count)
        print_slot_machine(slots)
        total = check_winnings(slots,lines,bet_amount,symbol_values)
        print("Your winnings are:",total)
        balance += total - bet_amount*lines
        print("Your current balance is:",balance)
        c = input("Press enter if u want to continue or q if u want to quit!")
        if c == 'q':
            break
main()