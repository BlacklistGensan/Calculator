from tkinter import *
cal= Tk()
textin = StringVar()
operator = ""
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
    def clrALLbut(self):
        global operator
        textin.set("")
        operator=""
        
# Function to delete one by one from the last in the entry of text display
    def backspacebut(self):
        global operator
        operator=operator[:-1]
        textin.set(operator)


    def __init__(self):
        cal.title("Blacklist Gensan")
        callabel = Label(cal, text="Blacklist Gensan",fg= "white",bg="black",font = ("Bodoni MT Black",20,"bold"))
        callabel.pack(side=TOP)
        cal.title("Calculator")
        callabel = Label(cal, text="Calculator",fg="white",bg="black",font = ("Bodoni MT Black",30,"bold"))
        callabel.pack(side=BOTTOM)
        cal.config(background = "black")
        cal.geometry("344x455")
        cal.resizable(False, False)

        caltext = Entry(cal,font=("Bodoni MT Black",20, "bold"),textvar=textin,width=17,bd=10,fg="white",bg="black",justify="right")
        caltext.pack()
        caltext.pack(side=TOP)

#BUTTONS

# 1st Row
        but7=Button(cal,padx=16,pady=13,bd=6,fg="white",bg="black",command = lambda:self.clickbut(7),text ="7", font=("Script MT Bold",14,"bold"))
        but7.place(x=11,y=110)

        but8=Button(cal,padx=16,pady=13,bd=6,fg="white",bg="black",command = lambda:self.clickbut(8),text ="8", font=("Script MT Bold",14,"bold"))
        but8.place(x=76,y=110)

        but9=Button(cal,padx=16,pady=14,bd=5,fg="white",bg="black",command = lambda:self.clickbut(9),text ="9", font=("Script MT Bold",14,"bold"))
        but9.place(x=140,y=110)
# 2nd Row
        but4=Button(cal,padx=16,pady=13,bd=6,fg="white",bg="black",command = lambda:self.clickbut(4),text ="4", font=("Script MT Bold",14,"bold"))
        but4.place(x=11,y=181.5)

        but5=Button(cal,padx=16,pady=12.5,bd=6,fg="white",bg="black",command = lambda:self.clickbut(5),text ="5", font=("Script MT Bold",14,"bold"))
        but5.place(x=76,y=181.5)

        but6=Button(cal,padx=15,pady=12.5,bd=6,fg="white",bg="black",command = lambda:self.clickbut(6),text ="6", font=("Script MT Bold",14,"bold"))
        but6.place(x=140,y=181.5)

# 3rd Row
        but1=Button(cal,padx=16.5,pady=13,bd=6,fg="white",bg="black",command = lambda:self.clickbut(1),text ="1", font=("Script MT Bold",14,"bold"))
        but1.place(x=11,y=254)

        but2=Button(cal,padx=16,pady=13,bd=6,fg="white",bg="black",command = lambda:self.clickbut(2),text ="2", font=("Script MT Bold",14,"bold"))
        but2.place(x=76,y=254)

        but3=Button(cal,padx=15,pady=13,bd=6,fg="white",bg="black",command = lambda:self.clickbut(3),text ="3", font=("Script MT Bold",14,"bold"))
        but3.place(x=140,y=254)



# 4th Row
        butdot=Button(cal,padx=19,pady=14.5,bd=6,fg="white",bg="black",command = lambda:self.clickbut("."),text =".", font=("Script MT Bold",14,"bold"))
        butdot.place(x=11,y=325)
        
        but0=Button(cal,padx=45,pady=12,bd=5,fg="white",bg="black",command = lambda:self.clickbut(0),text ="0", font=("Arial Black",14,"bold"))
        but0.place(x=76,y=325)



#OPERATIONS +, -, *, /, clrALL, delete

# 1st Row
        butclear=Button(cal,padx=14,pady=14,bd=5,fg="white",bg="black",text="AC",command=self.clrALLbut,font=("Impact",14,"bold"))
        butclear.place(x=270,y=110)

        butbackspace=Button(cal,padx=14,pady=14,bd=5,fg="white",bg="black",text="CE",command=self.backspacebut,font=("Impact",14,"bold"))
        butbackspace.place(x=202,y=110)
        
# 2nd Row
        butsub=Button(cal,padx=20,pady=13,bd=6,fg="white",bg="black",text="-",command = lambda:self.clickbut("-"), font=("Script MT Bold",14,"bold"))
        butsub.place(x=202,y=181.5)
        
        butml=Button(cal,padx=18.4,pady=13,bd=6,fg="white",bg="black",text="*",command = lambda:self.clickbut("*"), font=("Script MT Bold",14,"bold"))
        butml.place(x=270,y=181.5)

# 3rd Row
        butdiv=Button(cal,padx=18,pady=14,bd=6,fg="white",bg="black",text="/",command = lambda:self.clickbut("/"), font=("Script MT Bold",14,"bold"))
        butdiv.place(x=270,y=254)

# 3rd to 4th Row
        butadd=Button(cal,padx=17,pady=51,bd=5,fg="white",bg="black",text="+",command = lambda:self.clickbut("+"), font=("Script MT Bold",14,"bold"))
        butadd.place(x=202,y=254)


        butml=Button(cal,padx=18.4,pady=13,bd=6,fg="white",bg="black",text="*",command = lambda:self.clickbut("*"), font=("Script MT Bold",14,"bold"))
        butml.place(x=270,y=181.5)


# 4th Row
        butequal=Button(cal,padx=17,pady=14,bd=6,fg="black",bg="orange",command=self.evaluate,text="=",font=("Impact",14,"bold"))
        butequal.place(x=270,y=326)

obj = Calculator()

cal.mainloop()

