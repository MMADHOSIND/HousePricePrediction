from tkinter import *
from tkinter import font
from tkinter import messagebox  

# ==========Configs============
root = Tk()
root.title('House Price Prediction model')
root.config(bg='black')
root.geometry('700x700')
root.resizable(width=False, height=False)

# ==========Labels Configs============
label1_font = font.Font(size=18, weight='bold')
label_input_font = font.Font(size=13)

# ==========Labels============
lbl1 = Label(root, text='Enter the following inputs to predict the price', bg='black', fg='white', bd=0, font=label1_font)
lbl1.pack()

lblMHV = Label(root, text='Median_House_Value :', font=label_input_font, bg='black', fg='white', bd=0)
lblMHV.place(x=100, y=100)

lblMI = Label(root, text='Median_Income :', font=label_input_font, bg='black', fg='white', bd=0)
lblMI.place(x=100, y=150)

lblMA = Label(root, text='Median_Age :', font=label_input_font, bg='black', fg='white', bd=0)
lblMA.place(x=100, y=200)

lblTR = Label(root, text='Tot_Rooms :', font=label_input_font, bg='black', fg='white', bd=0)
lblTR.place(x=100, y=250)

lblTB = Label(root, text='Tot_Bedrooms :', font=label_input_font, bg='black', fg='white', bd=0)
lblTB.place(x=100, y=300)

lblPP = Label(root, text='Population :', font=label_input_font, bg='black', fg='white', bd=0)
lblPP.place(x=100, y=350)

lblHH = Label(root, text='Households :', font=label_input_font, bg='black', fg='white', bd=0)
lblHH.place(x=100, y=400)

lblLTT = Label(root, text='Latitude :', font=label_input_font, bg='black', fg='white', bd=0)
lblLTT.place(x=100, y=450)

lblLGT = Label(root, text='Longitude:', font=label_input_font, bg='black', fg='white', bd=0)
lblLGT.place(x=100, y=500)

# ==========Inputs============
inputMHV = Entry(root, bd=0)
inputMHV.place(x=300, y=100)

inputMI = Entry(root, bd=0)
inputMI.place(x=300, y=150)

inputMA = Entry(root, bd=0)
inputMA.place(x=300, y=200)

inputTR = Entry(root, bd=0)
inputTR.place(x=300, y=250)

inputTB = Entry(root, bd=0)
inputTB.place(x=300, y=300)

inputPP = Entry(root, bd=0)
inputPP.place(x=300, y=350)

inputHH = Entry(root, bd=0)
inputHH.place(x=300, y=400)

inputLTT = Entry(root, bd=0)
inputLTT.place(x=300, y=450)

inputLGT = Entry(root, bd=0)
inputLGT.place(x=300, y=500)

# ==========Functions============

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def check_inputs():
    empty_fields = []
    invalid_fields = []
    
   
    fields = [
        (inputMHV, "Median House Value"),
        (inputMI, "Median Income"),
        (inputMA, "Median Age"),
        (inputTR, "Total Rooms"),
        (inputTB, "Total Bedrooms"),
        (inputPP, "Population"),
        (inputHH, "Households"),
        (inputLTT, "Latitude"),
        (inputLGT, "Longitude")
    ]
    
    for entry, label in fields:
        value = entry.get()
        if value == "":
            empty_fields.append(label)
        elif not is_float(value):  
            invalid_fields.append(label)

    if empty_fields or invalid_fields:
        error_message = ""
        
        if empty_fields:
            error_message += f"The following fields are empty: {', '.join(empty_fields)}\n"
        if invalid_fields:
            error_message += f"The following fields should contain valid numbers: {', '.join(invalid_fields)}"
        
        messagebox.showerror("Input Error", error_message)
    else:
        messagebox.showinfo("Success", "All inputs are valid! but the model is not ready yet!!!")
       
def show_help():
    help_window = Toplevel(root)  
    help_window.title("Help")
    help_window.geometry("1100x400")
    help_window.resizable(height=False,width=False)  
    help_window.config(bg='black')

    lblHelp = Label(help_window, text="""1) Median House Value: Median house value for households within a block (measured in US Dollars) [$]
2) Median Income: Median income for households within a block of houses (measured in tens of thousands of US Dollars) [10k$]
3) Median Age: Median age of a house within a block; a lower number is a newer building [years]
4) Total Rooms: Total number of rooms within a block
5) Total Bedrooms: Total number of bedrooms within a block
6) Population: Total number of people residing within a block
7) Households: Total number of households, a group of people residing within a home unit, for a block
8) Latitude: A measure of how far north a house is; a higher value is farther north [°]
9) Longitude: A measure of how far west a house is; a higher value is farther west [°]

Block = 6,000 to 15,000 m2""",
                    bg='black', fg='white', font=label_input_font)
    lblHelp.pack()

 


# ==========‌Buttons============
btnPRED = Button(root, text='Predict',bd=0,bg='white', command=check_inputs)
btnPRED.place(x=300, y=600)

btnHELP = Button(root,text='Help',bd=0,bg='white',command=show_help)
btnHELP.place(x=380,y=600)

root.mainloop()


# 1) Median House Value: Median house value for households within a block (measured in US Dollars) [$]
# 2) Median Income: Median income for households within a block of houses (measured in tens of thousands of US Dollars) [10k$]
# 3) Median Age: Median age of a house within a block; a lower number is a newer building [years]
# 4) Total Rooms: Total number of rooms within a block
# 5) Total Bedrooms: Total number of bedrooms within a block
# 6) Population: Total number of people residing within a block
# 7) Households: Total number of households, a group of people residing within a home unit, for a block
# 8) Latitude: A measure of how far north a house is; a higher value is farther north [°]
# 9) Longitude: A measure of how far west a house is; a higher value is farther west [°]
# 10) Distance to coast: Distance to the nearest coast point [m]
# 11) Distance to Los Angeles: Distance to the centre of Los Angeles [m]
# 12) Distance to San Diego: Distance to the centre of San Diego [m]
# 13) Distance to San Jose: Distance to the centre of San Jose [m]
# 14) Distance to San Francisco: Distance to the centre of San Francisco [m]
# Block = 6,000 to 15,000 m2