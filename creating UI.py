import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import tkinter.filedialog
import os

## user to pass two file paths
base_filename = r'basefile.xlsx'
comp_filename = r'compfile.xlsx'
base_mixed_file = r'basefile mixed.xlsx'
comp_mixed_file = r'compfilemixed.xlsx'

# have user pass csv files
base_csv = r'basefile mixed.csv'
comp_csv = r'compfilemixed.csv'


'''
GOAL: WORK ON CREATING THE UI FOR THE USER TO GIVE THE INFO WE IN ORDER TO EXE THE SCRIPT
STATUS: WIP
TO DO: 
A - DONE - close first window asking for files and open new with the dorp down
B - STATUS - REPLACE .GRID WITH .PLACE; LOOKS BETTER
C - STATUS - PASS THE LIST FROM UI1 TO UI2
D - IF X/CLOSE PRESSED, EXIT INSTEAD OF MOVING TO THE NEXT UI
'''



## initiate tkinter UI and settings
root = tk.Tk()
root.title("QA Tool") # title
screenwidth = root.winfo_screenwidth() #dynamic screenwidth based on computer
screenheight = root.winfo_screenheight() #dynamic screenheight based on computer
height = 200
width = 350

# dynamic UI sizeing
alignstr = '%dx%d+%d+%d' % ((width + screenwidth/10),(height +screenheight/10),(screenwidth - width) / 2, (screenheight - height) / 2) ## dynamic sizing for the screen
# set size of UI
root.geometry("400x400")
## allow resizing from the user
root.resizable(width=True, height=True)
## App Name
AppLabel = tk.Label(root, text='QA Tool')

################## Functions ##################


## browse files function for base file
def browsefunc1():
    # open file explorer + file types
    filename =tkinter.filedialog.askopenfilename(filetypes=(("csv files","*.csv"),("All files","*.*")))
    # clear the entry box [to prevent errors in filepath]
    ent1.delete(0,tk.END)
    # add this to the entry box
    ent1.insert(tk.END, filename)


## browse files function for comp file
def browsefunc2():
    # open file explorer + file types
    filename =tkinter.filedialog.askopenfilename(filetypes=(("csv files","*.csv"),("All files","*.*")))
    # clear the entry box [to prevent errors in filepath]
    ent2.delete(0,tk.END)
    # add this to the entry box
    ent2.insert(tk.END, filename) # add this to the entry box


## get the string from the entry box; for submit button
def get_data():
    # set variables to global so they can be used elsewhere
    global base_columnList
    global comp_columnList
    # get value [filepath] from entry box
    basefilepath = ent1.get()
    compfilepath = ent2.get()
    # show user the files that have been passed
    print(f"Files chosen are:\n"
          f"- {os.path.dirname(basefilepath)}\n"
          f"- {os.path.dirname(compfilepath)}")

    # create data frame files
    base_df = pd.read_csv(basefilepath)
    comp_df = pd.read_csv(compfilepath)

    # get column headers into a list [to pass to OptionsMenu (dropdown)]
    base_columnList = list(base_df.columns.values) ## list of column headers in file A
    comp_columnList = list(comp_df.columns.values) ## list of column headers in file B

    # # checks
    # print(base_columnList)
    # print(comp_columnList)

    # close the UI in order to use data and open next one
    root.destroy()

## grab column pairs and put into list
def grab():
    print(f"adding {variableb.get()} and {variablec.get()}")
    pair = variableb.get(),variablec.get()
    pair = list(pair)
    column_list.append(pair)
    #print(column_list)

######################## UI #1 -- GET THE FILES FROM USRE ########################

## BUTTON 1 - entry box and browse for base file

## label for the base file
label= tk.Label(root, text="Base File here:", font=('Verdana 13'))
label.place(x=50,y=0)

# browse button
b1=tk.Button(root,text="BROWSE",font=40,command=browsefunc1,bd="4")
b1.place(x=10,y=30)

# entry box where the filepath will appear
ent1=tk.Entry(root,font=40)
ent1.place(x=100,y=35)

## BUTTON 2 - entry box and browse for base file ##

## label for the comp file
label= tk.Label(root, text="Comp File here:", font=('Verdana 13'))
label.place(x = 50,y = 80)

# browse button
b2=tk.Button(root,text="BROWSE",font=40,command=browsefunc2,bd="4")
b2.place(x = 10,y = 110)

# entry box 2 where the filepath will appear
ent2=tk.Entry(root,font = 40)
ent2.place(x = 100,y = 115)

## button to confirm the selected files are the one the user wants
getbutton = tk.Button(root, text= "SUBMIT", command= get_data,bg='dark green',bd="8",fg="white")
getbutton.place(x = 150,y = 150)

## print message to user in case of ayn error
msg_to_user = tk.Label(root, text="Please submit two files \nyou want to compare", font=('Verdana 13'))
msg_to_user.place(x=100,y=200)


root.mainloop()

######################## UI TO GET THE FILES FROM USRE ########################





###################### UI #2 -- DROP DOWN MENU AND CREATING MAPPING LIST ################

## start the second UI to get the column headers
root = tk.Tk()
root.title("QA Tool2")
root.geometry("400x400")
root.resizable(width=True, height=True) ## allow resizing from the user
AppLabel = tk.Label(root, text='QA Tool2')


## EXE THE QA TOOL SCRIPT ##
def execute():
    print(column_list)
    root.destroy()



column_list = []

# dropdown menu for 1; basefile
variableb = tk.StringVar(root)
variableb.set(base_columnList[0])
basefile_DropDownMenu = tk.OptionMenu(root,variableb,*base_columnList)
basefile_DropDownMenu.place(x=40,y=40)

# label to indicate which files headers these are
basefile_dropdown_label = tk.Label(root, text="Base File:", font=('Verdana 13'))
basefile_dropdown_label.place(x = 40,y = 10)



# dropdown menu for 1; compfile
variablec = tk.StringVar(root)
variablec.set(comp_columnList[0])
compfile_DropDownMenu = tk.OptionMenu(root,variablec,*comp_columnList)
compfile_DropDownMenu.place(x=160,y=40)

# label to indicate which files headers these are
compfile_dropdown_label = tk.Label(root, text="Comp File:", font=('Verdana 13'))
compfile_dropdown_label.place(x = 160,y = 10)


## grab button to add the two columns and put them into a list
grab = tk.Button(root,text='add',command=grab)
grab.place(x = 300,y = 40)


## execute button
execute = tk.Button(root, text= "execute",command=execute,bg='dark green',bd="8",fg="white")
execute.place(x = 130,y = 90)



root.mainloop()




