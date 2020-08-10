from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
import os
import tkinter.filedialog as fd
import threading



root = Tk()
img = ImageTk.PhotoImage(Image.open('22.jpg'))
root.iconphoto(False,img)
root.geometry("800x280")
root.title("ALGO_TEST")
root.config(bg = "white")



# Functions

def test_functions():
    print('It Works')


def allround_algo():

    a12 = entry_01.get("1.0", "end-1c")
    b = list(map(int,a12.split(",")))

    aa11 = search_algo.get()

    if aa11 == "Bubble sort":

        def bubble_sort(a):
            for i in range(len(a) - 1, 0, -1):
                for j in range(i):

                    if a[j] > a[j + 1]:
                        a[j], a[j + 1] = a[j + 1], a[j]
            search_output.delete('1.0', END)
            search_output.insert("end", a)
        bubble_sort(b)

    elif aa11 == "Selection Sort":

        def selection_sort(a):

            for i in range(len(a) - 1):
                min = i
                for j in range(i, len(a)):

                    if a[j] < a[min]:
                        min = j
                a[i], a[min] = a[min], a[i]
            search_output.delete('1.0', END)
            search_output.insert("end", a)
        selection_sort(b)

    elif aa11 == "Insertion Sort":

        def insertion_sort(alist):
            for i in range(1, len(alist)):
                temp = alist[i]
                j = i - 1
                while (j >= 0 and temp < alist[j]):
                    alist[j + 1] = alist[j]
                    j = j - 1
                alist[j + 1] = temp
            search_output.delete('1.0', END)
            search_output.insert("end", alist)

        insertion_sort(b)


    elif aa11 == "Linear Search":

        def linear_search():
            a = b
            elem = int(x.get())
            # print(a)
            for i in range(len(a)):
                if a[i]==elem:
                    random = f"The element {elem} is in the {i+1} position"

            search_output.delete('1.0', END)
            search_output.insert("end", random)


        w = Label(root,text="Enter the number you Wanna search-->",borderwidth=2,relief="groove",font=("comic sans ms", 10, "italic"))
        w.grid(row=0,column=2)

        x = Entry(root,borderwidth=2,relief="groove",font=("comic sans ms", 10, "italic"))
        x.grid(row=1,column=2)

        btn_2 = Button(root,text="SEARCH",borderwidth=2,relief="groove",font=("comic sans ms", 10, "italic"),command = linear_search)
        btn_2.grid(row=2,column=2)



    elif aa11 == "Binary Search":

        def binary_search():
            a = b
            elem = int(x.get())
            print(type(elem))
            l4 = 0
            print(len(a))
            u = len(a)-1
            m = int((l4 + u) / 2)

            while True:
                if elem == a[m]:

                    search_output.delete('1.0', END)
                    bq = f"The number {elem} you searched for is at {m+1} position"
                    search_output.insert("end", bq)
                    break

                elif elem > a[m]:
                    l4 = m
                    m = int((l4 + u) / 2)

                elif elem < a[m]:
                    u = m
                    m = int((l4 + u) / 2)

        thread_main_function_binary = threading.Thread(target=binary_search, daemon=True)

        w = Label(root, text="Enter the number you Wanna search-->", borderwidth=2, relief="groove",
                  font=("comic sans ms", 10, "italic"))
        w.grid(row=0, column=2)

        x = Entry(root, borderwidth=2, relief="groove", font=("comic sans ms", 10, "italic"))
        x.grid(row=1, column=2)

        btn_2 = Button(root, text="SEARCH", borderwidth=2, relief="groove", font=("comic sans ms", 10, "italic"),
                       command=binary_search)
        btn_2.grid(row=2, column=2)


def open_01():
    my_program = fd.askopenfilename()
    # Opens the program
    os.system('"%s"' % my_program)


def save_01():
    f = fd.asksaveasfile(mode='w',
                           filetypes=(('All Files', '*.*'), ('Python Files', '*.py'), ('Text Document', '*.txt')),
                           defaultextension=".txt")
    a09 = f"Data : {entry_01.get('1.0','end-1c')}\n Algorithm_Choosed = {search_algo.get()}\n Output = {search_output.get('1.0','end-1c')}"
    f.write(a09)
    f.close()


def dark_theme():
    root.config(bg="#233357")
    file_menu.config(bg="#233357",fg="white")
    dark_menu.config(bg="#233357", fg="white")
    label_1.config(bg="#233357",fg="#F29B18")
    label_3.config(bg="#233357",fg="#F29B18")
    label_2.config(bg="#233357",fg="#F29B18")
    entry_01.config(bg="#233357",fg="#F29B18")
    btn_1.config(bg="#233357",fg="#F29B18")
    search_output.config(bg="#233357",fg="#F29B18")



def restore_theme():
    root.config(bg="white")
    file_menu.config(bg="white", fg="black")
    dark_menu.config(bg="white", fg="black")
    label_1.config(bg="#D1D0CE", fg="black")
    label_3.config(bg="#D1D0CE", fg="black")
    label_2.config(bg="#D1D0CE", fg="black")
    entry_01.config(bg="white", fg="black")
    btn_1.config(bg="#D1D0CE", fg="black")
    search_output.config(bg="#D1D0CE", fg="black")


thread_open = threading.Thread(target=open_01,daemon=True)
thread_save = threading.Thread(target=save_01,daemon=True)
thread_main_function = threading.Thread(target=allround_algo,daemon=True)

# Tkinter Variable
data = StringVar()
search_var = StringVar()
search_output_1 = StringVar()

# Algorithms List
algorithms_list = ["Bubble sort","Selection Sort","Insertion Sort","Linear Search","Binary Search"]

# Menue_Widgets

main_menu = Menu(root)
file_menu = Menu(main_menu,tearoff=False)
file_menu.add_command(label="Open",command=open_01)
file_menu.add_command(label="Save",command=save_01)
file_menu.add_command(label="Exit",command=root.quit)
main_menu.add_cascade(label="File",menu=file_menu)

dark_menu =Menu(main_menu,tearoff=False)
dark_menu.add_command(label="Dark Theme",command=dark_theme)
dark_menu.add_command(label="Restore to defaults",command=restore_theme)
main_menu.add_cascade(label="Theme",menu=dark_menu)


root.config(menu=main_menu)

# Widgets

label_1 = Label(root,font=("comic sans ms", 10, "italic"),text="Enter the data -->>(Syntax : X,y,z,yt,z...)")
label_1.grid(row = 0,column=0,pady=10,padx=10)

entry_01 = Text(root,borderwidth=2,relief="groove",height=1,width=20,font=("comic sans ms", 10, "italic"))
entry_01.grid(row=0,column=1,pady=5,padx=6)

label_2 = Label(root,text="Select your Algorithm -->>",font=("comic sans ms", 10, "italic"))
label_2.grid(row =1, column= 0)

search_algo = Combobox(root,values=algorithms_list,height=5,width=25,font=("comic sans ms", 10, "italic"))
search_algo.grid(row=1,column=1,pady=6)
search_algo.current(0)


btn_1 = Button(root, text="RUN", width=10, command=allround_algo,font=("comic sans ms", 10, "italic"))
btn_1.grid(row=2,column=1)

label_3 = Label(root,text="Your Output is ---->>",font=("comic sans ms", 10, "italic"))
label_3.grid(row=3,column=0)

search_output = Text(root,borderwidth=2,relief="groove",height=5,width=30,font=("comic sans ms", 10, "italic"))
search_output.grid(row=3,column=1,pady=10)


root.mainloop()