import os.path
import getpass
from os.path import *
from Tkinter import *
#Retrieve computer username
computer_user = getpass.getuser()
#Create first window which loads entered client name
root1 = Tk()
root1.title("Load Client")
root1.geometry('500x200+200+200')

info = ""
#Set save path to desktop for client text file
save_path = ('/Users/' + computer_user + '/Desktop')

#Creates client entry box and sets variable "user_name" to client
user_name = StringVar(root1)
user_name.set("")
user_entry = Entry(root1, textvariable=user_name)
user_entry.pack()

#Label for client entry box
user_label = Label(root1, text = "Client Name")
user_label.pack()

#Function which loads client information into the next window
def load_user():
    #Gets client information from set save path and assigns variable to information
    user_load = os.path.join(save_path, user_name.get() + ".txt")
    #Loads information from client text file into variable "info"
    customer_file = open(user_load, 'a')
    customer_file = open(user_load)
    info = customer_file.read()
    #Closes first window after "load" button has been pressed
    root1.destroy()

#Creating button for "load" and setting call function to "load_user"
load = Button(root1, text="Load", command=load_user)
load.place(relx=.5, rely=.9, anchor="c")
root1.mainloop()

#Creating main window for information entries with dates and time
root = Tk()
root.title(user_name.get())
root.geometry('1000x500+200+200')

#Option list for months
OPTIONS = [
    "January",
    "Febuary",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#Option list for years
YEARS = [
    "2014",
    "2015",
    "2016",
    "2017"
]
#Search and load client text file
user_load = os.path.join(save_path, user_name.get() + ".txt")
#Open client text file for editing and print existing information in left textbox
customer_file = open(user_load, 'a')
customer_file = open(user_load)
info = customer_file.read()
#Assigning variable and creating drop down menu for Months
variable = StringVar(root)
variable.set("Month")
month = OptionMenu(root, variable, *OPTIONS)
month.place(relx=.3, rely=.8, anchor="c")
#Assigning variable and creating drop down menu for Days
variable1 = StringVar(root)
variable1.set("Day")
day = OptionMenu(root, variable1, *range(32))
day.place(relx=.2, rely=.8, anchor="c")
#Assigning variable and creating drop down menu for Year
variable2 = StringVar(root)
variable2.set("Year")
year = OptionMenu(root, variable2, *YEARS)
year.place(relx=.4, rely=.8, anchor="c")
#Creating 'read only' textbox to display client information
text = Text(root, bd = 5)
text.config(highlightbackground='black')
text.insert(INSERT, info)
text.config(state=DISABLED)
text.place(x = 0, y = 0)
#Creating editing textbox to add information to client file
text1 = Text(root, bd = 5)
text1.config(highlightbackground='red')
text1.place(x = 580, y = 0)
#Assigning variable and creating entry box for starting hour of work
startwork = StringVar(root)
startwork.set("0")
starthours = Entry(root, textvariable=startwork)
starthours.place(relx=.55, rely=.83, anchor="c", width = 50)
#Assigning variable and creating entry box for ending hour of work
endwork = StringVar(root)
endwork.set("0")
endhours = Entry(root, textvariable=endwork)
endhours.place(relx=.60, rely=.83, anchor="c", width = 50)
#Creating label for start entry box
start = Label(root, text = "Start")
start.place(relx=.53, rely=.76)
#Creating label for end entry box
end = Label(root, text = "End")
end.place(relx=.58, rely=.76)

#Function for save button, this writes/adds new information to client info
def save_input():
    #Get entry information for time and convert to integers
    endworkhour = float(endwork.get())
    startworkhour = float(startwork.get())
    #Calculations for 24 hour clock
    if (endworkhour < startworkhour):
        total_time = (startworkhour - (endworkhour + 24))
    elif (endworkhour > startworkhour):
        total_time = (endworkhour - startworkhour)
    #Get absolute value of "total_time"
    total_time = abs(total_time)
    #Assign variable to the new information being added to the client file
    new_info = (("%s %s, %s, for %s hours \n")%(variable.get(),variable1.get(),variable2.get(), total_time)) + (text1.get("1.0",END) + ("\n"))
    #Open and write new inforation into client file
    customer_file = open(user_load, 'a')
    customer_file.write(new_info)
    customer_file.close()
    customer_file = open(user_load)
    #Print new information on second half of the window
    info = customer_file.read()
    #Make other text box 'read only'
    text = Text(root, bd = 5)
    text.config(highlightbackground='black')
    text.insert(INSERT, info)
    text.config(state=DISABLED)
    text.place(x = 0, y = 0)
    text1.delete('1.0', END)
    #Reset all default entry box values
    variable.set("Month")
    variable1.set("Day")
    variable2.set("Year")
    startwork.set("0")
    endwork.set("0")
#Create Save button
b = Button(root, text="Save", command=save_input)
b.place(relx=.7, rely=.8, anchor="c")
root.mainloop()
