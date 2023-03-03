from tkinter import *

screen = Tk()
screen.geometry("400x480")

#button function
def calculate():
    eng_marks = int(english_entry.get())
    hin_marks = int(hindi_entry.get())
    mat_marks = int(mathematics_entry.get())
    sci_marks = int(science_entry.get())
    soc_marks = int(social_science_entry.get())
    total = (eng_marks + hin_marks + mat_marks + sci_marks + soc_marks)
    average = int(total/5)
    Label(screen,text=total,font="impack 15 bold").place(x=175,y=255)
    Label(screen, text=average, font="impack 15 bold").place(x=175, y=285)
    if average>40:
        grade = "PASS"
        Label(screen, text=grade, font="impack 15 bold", fg="green").place(x=175, y=315)
    else:
        grade = "FAIL"
        Label(screen,text=grade,font="impack 15 bold",fg="red").place(x=175,y=315)

#Heading
Label(screen,text="Grade Calculator",font="impack 20 bold",bg="purple",fg="white").pack(fill=X)

#subjects
Label(screen,text="English",font="23").place(x=30,y=70)
Label(screen,text="Hindi",font="23").place(x=30,y=105)
Label(screen,text="Mathematics",font="23").place(x=30,y=140)
Label(screen,text="Science",font="23").place(x=30,y=175)
Label(screen,text="Social science",font="23").place(x=30,y=210)
Label(screen,text="Total",font="impack 13 bold").place(x=30,y=255)
Label(screen,text="Average",font="impack 13 bold").place(x=30,y=285)
Label(screen,text="Grade",font="impack 13 bold").place(x=30,y=315)

# entry box
english_entry = Entry(screen,font="20",width=15,bd=2)
english_entry.place(x=180,y=70)

hindi_entry = Entry(screen,font="20",width=15,bd=2)
hindi_entry.place(x=180,y=105)

mathematics_entry = Entry(screen,font="20",width=15,bd=2)
mathematics_entry.place(x=180,y=140)

science_entry = Entry(screen,font="20",width=15,bd=2)
science_entry.place(x=180,y=170)

social_science_entry = Entry(screen,font="20",width=15,bd=2)
social_science_entry.place(x=180,y=210)

#button
Button(screen,text="Calculate",font="impack 13 bold",bg="light blue",command=calculate).place(x=80,y=380)
Button(screen,text="Exit",font="impack 13 bold",bg="red",fg="white",width=8,command=lambda:exit()).place(x=210,y=380)
mainloop()