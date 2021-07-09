#Calculator Logic

class Calculator:

# Function to add in the entry of text display
    def clickbut(self, number): 
        global operator
        operator = operator + str(number)
        textin.set(operator)

# Function to find the result of the operation
    def evaluate(self) :
        try:
            global operator
            input=str(eval(operator))
            textin.set(input)
            operator= ""
        except: 
            textin.set("ERROR")
            operator = "" 
            
# Function that clears the whole entry of text display   
    def clrALLbut():
        global operator
        textin.set("")
        operator=""

# Function to delete one by one from the last in the entry of text display
    def backspacebut():
        global operator
        operator=operator[:-1]
        textin.set(operator)
    
    
c = Calculator()



