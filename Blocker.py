import backend as db
from tkinter import *

#host_temp=r"C:\Users\desktop\PycharmProjects\project\hosts"

#path of host file
hostfile=r"C:\Windows\System32\drivers\etc\hosts"
redirect ="127.0.0.1"

def remove():

        #  remove site from blocked sites list
        rm_site =unblock_value.get()

        with open(hostfile,"r+") as file:

            content = file.readlines()
            file.seek(0)

            for line in content:

                if  rm_site in line:
                    pass
                else:
                    file.write(line)
                    db.delete(rm_site)      #Deleting from Blocked sites data

            file.truncate()                 # Closing the file


        e1.delete(0, END)
        e2.delete(0, END)

def add():

        # Adding Url into blocked site list
        add_site = list(block_value.get().split())

        with open(hostfile,"r+") as file:
            content=file.readlines()

            for website in add_site:

                if website in content:
                    pass                    # if website is already blocked wont add to file again
                else:
                    file.write(redirect+"   "+website+"\n")
                    add_site="".join(add_site)
                    db.insert(add_site,redirect)
                                                    #inserting into host file and database

            file.truncate()

        e1.delete(0,END)
        e2.delete(0,END)

def view_list():

    view_block.delete(0,END)
    for col in db.view():
        view_block.insert(END,col)


window=Tk()

window.wm_title("Website Blocker")

add_button=Button(window, text="Add", command=add, width=10)
rm_button=Button(window, text="Remove", command=remove, width=10)
view_button=Button(window,text="View",command=view_list,width=10)

l1=Label(window,text="Enter Url to  Block ")
l1.grid(row=0,column=0)

l2=Label(window,text="Enter Url to Unblock ")
l2.grid(row=1,column=0)

l3=Label(window,text="Blocked Sites List")
l3.grid(row=2,column=0)

block_value=StringVar()
e1=Entry(window,textvariable=block_value)
e1.grid(row=0,column=3)

unblock_value=StringVar()

e2=Entry(window,textvariable=unblock_value)
add_button.grid(row=0, column=6)
e2.grid(row=1,column=3)

rm_button.grid(row=1, column=6)

view_block=Listbox(window,height=10,width=40)
view_block.grid(row=3,column=0,rowspan=10,columnspan=6)

sb1=Scrollbar(window)
sb1.grid(row=2,column=4,rowspan=20)

view_block.configure(yscrollcommand=sb1.set)
sb1.configure(command=view_block.yview)

view_button.grid(row=3,column=6)


window.mainloop()
