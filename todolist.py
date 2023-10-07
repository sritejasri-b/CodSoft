import tkinter
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x700+400+100")
root.resizable(False,False)

task_list=[]
def addtask():
    task=entry.get()
    entry.delete(0,END)
    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"{task}\n")
        task_list.append(task)
        list.insert(END,task)

def deleteTask():
    global task_list
    task= str(list.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
             for task in task_list:
                 taskfile.write(task+"\n")
        list.delete(ANCHOR)         

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks= taskfile.readlines()
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                list.insert(END,task)
    except:
        file = open('tasklist.txt','w')
        file.close()
            
        
    
#for icons
image_path = r"C:/Users/byris/OneDrive/Documents/images/topbar (1).png"
top_image = PhotoImage(file=image_path)
Label(root,image= top_image).pack()
image_path1 = r"C:/Users/byris/OneDrive/Documents/images/dock (1).png"
dock_img = PhotoImage(file= image_path1)
Label(root,image= dock_img,bg="#32405b").place(x=30,y=25)

label = Label(root,text="ALL TASKS",font="arial 20 bold",fg="white",bg="#32405b")
label.place(x=130,y=20)

#frame widget
frame = Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=160)

#for input
input=StringVar()
entry=Entry(frame,width=18,font="arial 20",bd=0)
entry.place(x=10,y=7)
entry.focus()

#ADD button to add task
button= Button(frame,text="ADD",font="arial 20 bold",width=5,bg="#5a95ff",fg="#fff",bd=0,command=addtask)
button.place(x=320)

frame1 = Frame(root,bd=3,width=700,height=250,bg="#32405b")
frame1.pack(pady=(200,0))
list=Listbox(frame1,font=('arial',12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
list.pack(side=LEFT,fill=BOTH,padx=2)
scroll_bar= Scrollbar(frame1)
scroll_bar.pack(side= RIGHT,fill = BOTH)

list.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list.yview)

#delete
link = r"C:/Users/byris/OneDrive/Documents/images/delete.png"
delete_icon = PhotoImage(file = link)
d= Button(root,image = delete_icon,bd=0,command=deleteTask)
d.pack(side=BOTTOM, pady = 13)

openTaskFile()
root.mainloop()