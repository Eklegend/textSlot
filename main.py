import random

MAX_LINES = 3   # global constant
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3


symbol_count ={
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
symbol_value ={ # this multiples the winnings according the alphaber
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines=[]
    for line in range(lines):
        symbol = columns[0][line] # check from 1st column
        for column in columns:
            symbol_to_check = column[line] #check the symbol in column 
            if symbol != symbol_to_check: #if symbol is not equal to previous symbol,then break
                break 
        #if we didint break then below will run
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines






# generate which symbols is gonna be on which column based on the frequency we have here
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols =[]
    # we are using a dictionary. symbol.items gives a key and value associated with a dictionary
    for symbol,symbol_count in symbols.items():  # symbol is alphabet and symbol count is the numbering
        # we use _ as a unused variable. we dont care abt the count
        for _ in range(symbol_count): 
        # when symbol count is 2, then letter A will be added twice in the all_symbols[] list
            all_symbols.append(symbol)
    
    columns = [] # defining our colums list
    # generate values in column for every single column we have
    for col in range(cols):
        column = [] # our column is now a empty list
        #[:] this means it copies the list and data to the new varible
        current_symbol = all_symbols[:] #current symbols stores the same object as all symbols and any
        # changes to all_symbols will effect current_symbol
        for _ in range(rows): #number of values we have to generate is equal to the number of rows in slot machine
            value = random.choice(current_symbol) # choices are taken from current _symbols
            # ex: random choice picks "A", now .remove will remove "A" so it doesnt select A in the next slot
            current_symbol.remove(value) # removes values from current_symbol list
            # now we add value "A" to column
            column.append(value)

        
        columns.append(column)
    return columns


    
# now we tanspose the colums. ( transposing)
def print_slot_machine(columns):
    for row in range(len(columns[0])): # loop throughe every single row
        # for every single row, we loop through every column
        for i, column in enumerate(columns): # this i and enumerate will give you a index. 
            # since we have enumerate, column is given value. Since we have 3 items, so 0,1,2 columns,
            # and when i is not equal to (3-1) , it gives a "|", when i is equal to (3-1) it doesnt give "|"
            if i != len(columns)-1:  # also like this if i != 2 
                print(column[row], end =" | ")
            #when i is equal to (3-1) it doesnt give "|"
            else:
                print(column[row], end="")
        print()# doing an empty print statement, brings it down to next line

    

def deposit():# collecting user onput on deposit value
    while True:
        amount = input("What would you like to deposit $ ? :")
        #isdigit makes sure the value enter is a positive integer
        if amount.isdigit():
            amount= int(amount)# user input will be in string, so we use this to convert it to int
            if amount > 0:
                break # this will break the while loop and move the amount to other place later on
            else:
                print("Amount must be greater than 0. ")
        else:
            print("Please enter a number :) : ") # if the value if not a number this will pop up
    return amount 

def get_number_of_lines(): # this sets up the betting on lines and how many lines can be bet on
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES)+ ")? :")
        #isdigit makes sure the value enter is a positive integer
        if lines.isdigit():
            lines= int(lines)# user input will be in string, so we use this to convert it to int
            if 1 <= lines <= MAX_LINES: # if my lines are more than or = to 1 and less then or equal to 3(MAX_LINES)
                break # this will break the while loop and move the amount to other place later on
            else:
                print("Enter valid number of lines ")
        else:
            print("Please enter a number :) : ") # if the value if not a number this will pop up
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line $ ? :")
        #isdigit makes sure the value enter is a positive integer
        if amount.isdigit():
            amount= int(amount)# user input will be in string, so we use this to convert it to int
            if MIN_BET<=amount<=MAX_BET:
                break # this will break the while loop and move the amount to other place later on
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET} :")
                # we are adding and f to add values/varibles in a sentence
        else:
            print("Please enter a number :) : ") # if the value if not a number this will pop up
    return amount     


def spin(balance):
    lines = get_number_of_lines()

    while True: # to make sure the amount user is betting is in their balance limit
            bet = get_bet()
            total_bet= bet*lines

            if total_bet>balance:
                print(f"You do not have enough to bet the amount, your current balance is ${balance}")
            else:
                break
        

    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines: 100", *winning_lines) #this * means, it gets the data from the above winning_lines 
    return winnings-total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is : ${balance}")
        answer = input("Press enter to play and (q to quit).")
        if answer == "q":
            break
        balance+=spin(balance)


    print(f"you left with ${balance}.")

    

main()