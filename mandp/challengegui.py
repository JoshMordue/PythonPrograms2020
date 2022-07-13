import tkinter

mainWindow = tkinter.Tk()

mainWindowPadding = 8

mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = mainWindowPadding

keys = [[('C', 1), ('CE', 2)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)]]

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

keypad = tkinter.Frame(mainWindow)
keypad.grid(row=1, column=0, sticky='nsew')

row = 0

for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keypad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky='ew')
        col += 1
    row += 1

mainWindow.update()
mainWindow.minsize(keypad.winfo_width() + mainWindowPadding, result.winfo_height() + keypad.winfo_height())
mainWindow.maxsize(keypad.winfo_width() + 50 + mainWindowPadding, result.winfo_height() + 50 + keypad.winfo_height())
mainWindow.mainloop()
