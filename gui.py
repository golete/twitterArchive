import tkinter as tk

root = tk.Tk()
root.title("Select User Mentioned in Archive")

app_width = 410
app_height = 250

x_center = root.winfo_screenwidth()-app_width
y_center = root.winfo_screenheight()-app_height

font = "Helvetica", 14

root.geometry(f'{app_width}x{app_height}+{x_center//2}+{y_center//2}')
root.resizable(False, False)

def optionMenu(optionlist):

    def show():
        myLabel = tk.Label(root, text = clicked.get()).pack()

    clicked = tk.StringVar()
    clicked.set(optionlist[0])

    drop = tk.OptionMenu(root, clicked, *optionlist)
    drop.pack()

    bSubmit = tk.Button(root, text="Submit", font=font, command=root.quit)
    bSubmit.pack()

    root.mainloop()

    return optionlist.index(clicked.get())

def completeMenu(optionList):

    def update(data, box):
        box.delete(0, tk.END)
        for item in data:
            box.insert(tk.END, item)

    def fillout(event):
        myEntry.delete(0,tk.END)
        myEntry.insert(0, myList.get(tk.ANCHOR))

    def check(event):
        typed = myEntry.get()

        if typed == '':
            data = optionList
        else:
            data = [item for item in optionList if typed.lower() in item.lower()]
        update(data,myList)

    def select():
        result = myList.get(myList.curselection())
        global index
        index = optionList.index(result)
        root.quit()
        return index

    myLabel = tk.Label(root, text="Search:", font=font)
    myLabel.grid(row=0, column=0, padx=5, pady=5)

    myEntry = tk.Entry(root, width=33, font=font)
    myEntry.grid(row=0, column = 1, padx=0, pady=0)

    myList = tk.Listbox(root, width=30)
    myList.grid(row=1, column = 1, padx=0, pady=5)

    update(optionList,myList)

    myList.bind('<<ListboxSelect>>', fillout)
    myEntry.bind('<KeyRelease>', check)

    bSelect = tk.Button(root, text = "Select", font=font, padx=116, command=select)
    bSelect.grid(row=2, column=1, pady=5)

    root.mainloop()

    try:
        return index
    except:
        return -1
