from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from cv2 import cv2
import numpy as np
import json
from PIL import Image, ImageOps
import os

#Needed Global variables
path = ''
panel = ''


def openVid():
    import faceApp_explore
    

# This function allows you to images from the OS, it is executed when you click the load image button
def loadImage():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select A File", filetype = (("png", "*.jpg"), ("All Files", "*.*")))
    global path
    global panel
    path = filename
    #Cant get resizing to work
    #path = os.path.basename(filename)      
    #path = path.resize(path,(250, 250), Image.ANTIALIAS) #The (250, 250) is (height, width)
    #path.save('eg', format='PNG')
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(frame, width= 100,  image =img)
    panel.image = img
    panel.place(relx=0.15, rely=0.15, relwidth=0.20, relheight=0.50)
    


#This function collects all input data
def profile():
    FirstName = firstName.get()
    LastName = lastName.get()
    Age = age.get()
    Gender = gender.get()
    LastArea = lastArea.get()
    Image = path
    

#This function create dictionaries to store user profile
def prfDict():
    
    DictName  = {}  
    Name      = firstName.get() 
    Last_Name = lastName.get()
    Age       = age.get()
    Gender    = gender.get() 
    Last_Area = lastArea.get()
    Image     = path
    
    DictName['Name'] = Name
    DictName['Last Name'] = Last_Name
    DictName['Age'] = Age
    DictName['Gender'] = Gender
    DictName['Last Area'] = Last_Area
    DictName['Image'] = Image

    with open("Database.json", "a+") as f:
        f.write("{}\n".format(json.dumps(DictName)))
             
def search():
    input = searchBoxintake.get()
    inputStr = input
    
    with open('Database.json', 'r') as d:
        data = json.load(d)
        for key, values in data.items():
            if inputStr == values:
                print(data.get('Name'), data.get('Last Name'), 
                data.get('Age'), data.get('Gender'), data.get('Last Area'))

    #Text Box - Display of searched information
    searchName = tk.Label(frame, text = data.get('Name') )
    searchLastName = tk.Label(frame, text = data.get('Last Name') )
    searchAge = tk.Label(frame, text = data.get('Age') )
    searchGender = tk.Label(frame, text = data.get('Gender') )
    searchArea = tk.Label(frame, text = data.get('Last Area') )

    searchName.place(relx=0.19, rely=0.8, relwidth=0.25, relheight=0.07)
    searchLastName.place(relx=0.19, rely=0.9, relwidth=0.25, relheight=0.07)
    searchAge.place(relx=0.62, rely=0.8, relwidth=0.07, relheight=0.07)            
    searchGender.place(relx=0.83, rely=0.8, relwidth=0.10, relheight=0.07)
    searchArea.place(relx=0.63, rely=0.9, relwidth=0.20, relheight=0.07)
    searchBoxintake.delete(0, 'end')            

               
#This functions clears all input data
def clearInput():
    firstName.delete(0, 'end')
    lastName.delete(0, 'end')
    age.delete(0, 'end')
    gender.delete(0, 'end')
    lastArea.delete(0, 'end')
    panel.config(image = "")


master = tk.Tk() 
#Create canvas and frame to hold widgets
w = Canvas(master, width=900, height=500)
w.pack() 
#Inside Frame
frame = tk.Frame(master, bg= "white")
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


#Load image button -takes in the missing person photograph  
load_image_button = tk.Button(frame, text = "Load Image", bg='yellow', fg='black', command = loadImage) 
load_image_button.place(relx=0.10, rely=0.7, relwidth=0.30, relheight=0.07)

#Create profile button - Creates profile and stores data in dictionary
profile_button = tk.Button(frame, text = "Create Profile", bg='gray', fg='black',command = lambda:[profile(), prfDict(), clearInput() ])
profile_button.place(relx=0.6, rely=0.56, relwidth=0.35, relheight=0.07)

#Video Button - Opens live stream and runs object detection 
searchByvid_button = tk.Button(frame, text = "Search by Video", bg='gray', fg='black',command = openVid )
searchByvid_button.place(relx=0.6, rely=0.63, relwidth=0.35, relheight=0.07)

#Search Box - Iterates over json file and returns data 
searchBox = tk.Button(frame, text = "Search", bg='yellow', fg='black', command = search)
searchBoxintake = tk.Entry(frame, bd = 3) 
searchBox.place(relx=0.6, rely=0.7, relwidth=0.10, relheight=0.07)
searchBoxintake.place(relx=0.7, rely=0.703, relwidth=0.25, relheight=0.07)



#Information intake
#First Name
labelName= tk.Label(frame, text='First Name')
firstName = tk.Entry(frame)
labelName.place(relx=0.6, rely=0.16, relwidth=0.10, relheight=0.07)
firstName.place(relx=0.7, rely=0.16, relwidth=0.25, relheight=0.07)

#Last Name
labelLastName= tk.Label(frame, text='Last Name')
lastName = tk.Entry(frame)
labelLastName.place(relx=0.6, rely=0.24, relwidth=0.10, relheight=0.07)
lastName.place(relx=0.7, rely=0.24, relwidth=0.25, relheight=0.07)

#Age
labelAge= tk.Label(frame, text='Age')
age = tk.Entry(frame)
labelAge.place(relx=0.6, rely=0.32, relwidth=0.10, relheight=0.07)
age.place(relx=0.7, rely=0.32, relwidth=0.25, relheight=0.07)

#Gender
labelGender= tk.Label(frame, text='Gender')
gender = tk.Entry(frame)
labelGender.place(relx=0.6, rely=0.40, relwidth=0.10, relheight=0.07)
gender.place(relx=0.7, rely=0.40, relwidth=0.25, relheight=0.07)

#Area last seen
labelLastArea= tk.Label(frame, text='Area last seen')
lastArea = tk.Entry(frame)
labelLastArea.place(relx=0.6, rely=0.48, relwidth=0.10, relheight=0.07)
lastArea.place(relx=0.7, rely=0.48, relwidth=0.25, relheight=0.07)

#Search label results
textBox_Name = tk.Label(frame, text='Name:')
textBox_Name.place(relx=0.10, rely=0.8, relwidth=0.10, relheight=0.07) 

textBox_LastName = tk.Label(frame, text='Last Name:')
textBox_LastName.place(relx=0.10, rely=0.9, relwidth=0.10, relheight=0.07)

textBox_Age = tk.Label(frame, text='Age:')
textBox_Age.place(relx=0.50, rely=0.8, relwidth=0.13, relheight=0.07)

textBox_Area = tk.Label(frame, text='Area last seen:')
textBox_Area.place(relx=0.50, rely=0.9, relwidth=0.13, relheight=0.07)

textBox_Area = tk.Label(frame, text='Gender:')
textBox_Area.place(relx=0.75, rely=0.8, relwidth=0.10, relheight=0.07)

mainloop()
