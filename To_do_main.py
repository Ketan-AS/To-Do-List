from tkinter import *
import mysql.connector as m

def main():
    mydatabase = m.connect(host="localhost", user="root", password="Ketan@1234", database="Project")
    cursor = mydatabase.cursor()

    # cursor.execute('DROP TABLE IF EXISTS Tasks;')
    # cursor.execute("CREATE TABLE Tasks(SrNo INT(3) PRIMARY KEY AUTO_INCREMENT, task VARCHAR(100))")

    def add_task():
        task = entry.get()
        if task:
            listbox.insert(END, task)
            entry.delete(0, END)
            # Save the task to the database
            cursor.execute("INSERT INTO Tasks(task) VALUES(%s)", [task])
            mydatabase.commit()

    def delete_task():
        try:
            index = listbox.curselection()
            selected_task = listbox.get(index)
            listbox.delete(index)
            # Delete the task from the database
            cursor.execute("DELETE FROM Tasks WHERE task=%s", (selected_task,))
            mydatabase.commit()
        except:
            pass
    
    def print_records():
        cursor.execute("SELECT * FROM tasks")
        records = cursor.fetchall()
        for record in records:
            print(record)

    def exit_gui():
        root.destroy()

    root = Tk()
    root.geometry("800x600+100+50") 
    root.title("To-Do List")
    
    bg =PhotoImage(file="to-do-list2.png")

    #label
    mylabel = Label(root,image =bg)
    mylabel.place(x=0,y=0,relwidth =1,relheight=1)

    frame = Frame(root)
    frame.pack(pady=10, anchor=NW)


    listbox = Listbox(frame, width=50, height=15, font=('Times',12))
    listbox.pack(side=LEFT, fill=Y, anchor=NW)


    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    entry = Entry(root, font=("Times", 15, "bold"))
    entry.place(x=75,y=350)

    add_button = Button(root, text="Add Task", command=add_task)
    add_button.place(x=25,y=400)

    delete_button = Button(root, text="Delete Task", command=delete_task)
    delete_button.place(x=100,y=400)

    print_button = Button(root, text="Print Records", command=print_records)
    print_button.place(x=200,y=400)

    exit_button = Button(root, text="Exit", command=exit_gui)
    exit_button.place(x=300,y=400)

    root.mainloop()
