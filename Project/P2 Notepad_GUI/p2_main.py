
import tkinter
from tkinter import *
from tkinter import font
from tkinter import filedialog
import os
import datetime
from datetime import *


file_name = None

root = Tk()
root.title("Untitled file")
root.geometry('400x400')


textarea = Text(root)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
aboutmenu = Menu(menubar, tearoff=0)
formatmenu = Menu(menubar, tearoff=0)
editmenu = Menu(menubar, tearoff=0)
statsmenu = Menu(menubar, tearoff=0)
thememunu = Menu(menubar, tearoff=0)
scrollbar = Scrollbar(textarea)


color_dict = {
    'Light Default': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Red': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#d3b774', '#474747'),
    'Night Blue': ('#ededed', '#6b9dc2')
}


def change_theme(choose_theme):
    fg_color, bg_color = choose_theme[0], choose_theme[1]
    textarea.config(background=bg_color, fg=fg_color)


def word_count():
    text = textarea.get('1.0', END)
    words = text.split()
    top = Toplevel(root)
    top.geometry('200x50')
    top.title('Word Count')
    counting = Label(top, text=f'Total Word count : {len(words)}')
    counting.pack()
    exit_button = Button(top, text='Close', command=lambda: top.destroy())
    exit_button.pack()


def char_count():
    text = textarea.get('1.0', END)
    top = Toplevel(root)
    top.geometry('200x50')
    top.title('Character Count')
    counting = Label(top, text=f'Total Character count : {len(text)}')
    counting.pack()
    exit_button = Button(top, text='Close', command=lambda: top.destroy())
    exit_button.pack()


def date_modified():
    if file_name:
        if os.path.isfile(file_name):
            last_modified_date = datetime.fromtimestamp(
                os.path.getmtime(file_name))
        else:
            last_modified_date = 0
    else:
        return
    top = Toplevel(root)
    top.geometry('300x50')
    top.title('Last date modified')
    counting = Label(top, text=f'last date modified : {last_modified_date}')
    counting.pack()
    exit_button = Button(top, text='Close', command=lambda: top.destroy())
    exit_button.pack()


def date_created():
    if file_name:
        if os.path.isfile(file_name):
            last_modified_date = datetime.fromtimestamp(
                os.path.getctime(file_name))
        else:
            last_modified_date = 0
    else:
        return
    top = Toplevel(root)
    top.geometry('300x50')
    top.title('Date created')
    counting = Label(top, text=f'date created : {last_modified_date}')
    counting.pack()
    exit_button = Button(top, text='Close', command=lambda: top.destroy())
    exit_button.pack()


def new_file(event=None):
    global file_name
    root.title('Untitled file')
    file_name = None
    textarea.delete('1.0', END)
    textarea.update()


def open_file(event=None):
    global file_name
    file_name = filedialog.askopenfilename(title="Select a file to open", filetypes=(
        ("txt files", "*.txt"), ("all files", "*.*")))
    if file_name == "":
        file_name = None
    else:
        root.title(os.path.basename(file_name))
        textarea.delete(1.0, END)
        textarea.update()
        file = open(file_name, "r")
        textarea.insert(1.0, file.read())
        file.close()


def save_file(event=None):
    global file_name

    if file_name == None:
        # Save as new file
        file_name = filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                                 defaultextension=".txt",
                                                 filetypes=[("All Files", "*.*"),
                                                            ("Text Documents", "*.txt")])

        if file_name == "":
            file_name = None
        else:
            # Try to save the file
            file = open(file_name, "w")
            file.write(textarea.get(1.0, END))
            file.close()

            # Change the window title
            root.title(os.path.basename(file_name))

    else:
        file = open(file_name, "w")
        file.write(textarea.get(1.0, END))
        file.close()


def saveas_file():
    global file_name
    file_name = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[
        ("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file_name == "":
        file_name = None
    else:
        # Try to save the file
        file = open(file_name, "w")
        file.write(textarea.get(1.0, END))
        file.close()

        # Change the window title
        root.title(os.path.basename(file_name))


def end_program(event=None):
    root.destroy()


def copy_file():
    textarea.event_generate('<<Copy>>')


def cut_file():
    textarea.event_generate('<<Cut>>')


def paste_file():
    textarea.event_generate('<<Paste>>')


idx = '1.0'
idr = '1.0'
lastidr = END
search = 1


def highlight_text(txt):
    textarea.tag_remove('found', '1.0', END)
    if txt:
        global search
        global idx
        global idr
        global lastidr
        idx = textarea.search(txt, idx, nocase=1, stopindex=END)
        if not idx:
            idx = '1.0'
            idx = textarea.search(txt, idx, nocase=1, stopindex=END)
            if not idx:
                idx = '1.0'
                search = 0
                return
        lastidx = '%s+%dc' % (idx, len(txt))
        textarea.tag_add('found', idx, lastidx)
        idr = idx
        lastidr = lastidx
        idx = lastidx
        textarea.see(idx)
        textarea.tag_config('found', background='blue', foreground='white')


def find_file(event=None):
    top = Toplevel(root)
    top.geometry('400x200')
    top.title("Find")
    find_label = Label(top, text='Find what')
    find_label.grid(row=0, column=0)
    txt_input = Entry(top, width=30, borderwidth=5)
    txt_input.grid(row=0, column=2, columnspan=3, padx=10, pady=10)
    find_button = Button(top, text='Find next',
                         command=lambda: highlight_text(txt_input.get()))
    find_button.grid(row=0, column=8)
    exit_button = Button(top, text='Cancel', command=lambda: exit_file(top))
    exit_button.grid(row=1, column=8, columnspan=1)
    top.protocol("WM_DELETE_WINDOW", lambda: exit_file(top))


def replace_text(idr, lastidr, txt_replace, txt_find):
    global search
    if search == 0:
        return
    textarea.tag_remove('replace', '1.0', END)
    if (txt_find and txt_replace):
        textarea.delete(idr, lastidr)
        textarea.update()
        textarea.insert(idr, txt_replace)

        lastidr = '% s+% dc' % (idr, len(txt_replace))

        # overwrite 'Found' at idx
        textarea.tag_add('found', idr, lastidr)
        idr = lastidr

        # mark located string as red
        textarea.tag_config('found', foreground='white',
                            background='blue')


def replaceall_text(txt_replace, txt_find):
    textarea.tag_remove('found', '1.0', END)
    if (txt_replace and txt_find):
        ida = '1.0'
        while 1:
            ida = textarea.search(txt_find, ida, nocase=1,
                                  stopindex=END)
            if not ida:
                break
            lastida = '% s+% dc' % (ida, len(txt_find))

            textarea.delete(ida, lastida)
            textarea.insert(ida, txt_replace)

            lastida = '% s+% dc' % (ida, len(txt_replace))
            textarea.tag_add('found', ida, lastida)
            ida = lastida

        # mark located string as red
        textarea.tag_config('found', foreground='white', background='blue')


def exit_file(top):
    textarea.tag_remove('found', '1.0', END)
    top.destroy()


def find_replace_file(event=None):
    top = Toplevel(root)
    top.geometry('400x200')
    top.title("Find")

    find_label = Label(top, text='Find what')
    find_label.grid(row=0, column=0)

    replace_label = Label(top, text='Replace with')
    replace_label.grid(row=2, column=0)

    txt_input_find = Entry(top, width=30, borderwidth=5)
    txt_input_find.grid(row=0, column=2,
                        columnspan=3, padx=10, pady=10)

    txt_input_replace = Entry(top, width=30, borderwidth=5)
    txt_input_replace.grid(row=2, column=2,
                           columnspan=3, padx=10, pady=10)

    find_button = Button(top, text='Find next',
                         command=lambda: highlight_text(txt_input_find.get()))
    find_button.grid(row=0, column=8, columnspan=1)

    replace_button = Button(top, text='Replace',
                            command=lambda: replace_text(idr, lastidr, txt_input_replace.get(), txt_input_find.get()))
    replace_button.grid(row=1, column=8, columnspan=1)

    replaceall_button = Button(top, text='Replace All',
                               command=lambda: replaceall_text(txt_input_replace.get(), txt_input_find.get()))
    replaceall_button.grid(row=2, column=8, columnspan=1)

    exit_button = Button(top, text='Cancel', command=lambda: exit_file(top))
    exit_button.grid(row=3, column=8, columnspan=1)
    top.protocol("WM_DELETE_WINDOW", lambda: exit_file(top))


def font_changer(top_font, font_name, font_size):
    if font_name and font_size:
        # font_ch = tkinter.font(family=font_name, size=font_size)
        textarea.configure(font=(font_name, font_size))
    top_font.destroy()


def font_editor():
    font_names = list(tkinter.font.families())
    top = Toplevel(root)
    top.geometry('380x200')
    top.title("Font")

    def font_name_change(event):
        font_display = Label(top, text=font_name_list.get(
            font_name_list.curselection())).place(x=20, y=0, width=100)

    def font_no_change(event):
        font_display_no = Label(top, text=font_no_list.get(
            font_no_list.curselection())).place(x=140, y=0, width=100)

    font_name = StringVar()
    font_name.set('Font Name')
    font_display = Label(top, text="Font type").place(x=20, y=0, width=100)
    font_name_list = Listbox(top, exportselection=0)
    font_name_list.place(x=20, y=20, width=100, height=150)
    for font in font_names:
        font_name_list.insert(END, font)
    scrollbar_font_name = Scrollbar(font_name_list)
    scrollbar_font_name.pack(side=RIGHT, fill=Y)
    font_name_list.config(yscrollcommand=scrollbar_font_name.set)
    scrollbar_font_name.config(command=font_name_list.yview)
    font_name_list.bind('<<ListboxSelect>>',
                        font_name_change)

    font_no = StringVar()
    font_no.set('Font size')
    font_display_no = Label(top, text='Font Size').place(x=140, y=0, width=100)
    font_no_list = Listbox(top, exportselection=0)
    font_no_list.place(x=140, y=20, width=100, height=150)
    for size in range(2, 30):
        font_no_list.insert(END, 2*size)
    scrollbar_font_no = Scrollbar(font_no_list)
    scrollbar_font_no.pack(side=RIGHT, fill=Y)
    font_no_list.bind('<<ListboxSelect>>',
                      font_no_change)
    font_no_list.config(yscrollcommand=scrollbar_font_no.set)
    scrollbar_font_no.config(command=font_no_list.yview)

    ok_button = Button(top, text='OK', command=lambda: font_changer(top,
                                                                    font_name_list.get(
                                                                        font_name_list.curselection()), font_no_list.get(
                                                                        font_no_list.curselection()))).place(x=280, y=50, width=75)
    exit_button = Button(top, text='Cancel', command=lambda: top.destroy()).place(
        x=280, y=75, width=75)


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
textarea.grid(sticky=N + E + S + W)

filemenu.add_command(label='New', command=new_file, accelerator='Ctrl+N')
filemenu.add_command(label='Open', command=open_file, accelerator='Ctrl+O')
filemenu.add_command(label='Save', command=save_file, accelerator='Ctrl+S')
filemenu.add_command(label='Save as', command=saveas_file)
filemenu.add_command(label='Exit', command=end_program, accelerator='Ctrl+Q')
menubar.add_cascade(label='File', menu=filemenu)
root.bind('<Control-n>', new_file)
root.bind('<Control-o>', open_file)
root.bind('<Control-s>', save_file)
root.bind('<Control-q>', end_program)
root.bind('<Control-N>', new_file)
root.bind('<Control-O>', open_file)
root.bind('<Control-S>', save_file)
root.bind('<Control-Q>', end_program)


editmenu.add_command(label='Copy', command=copy_file, accelerator='Ctrl+C')
editmenu.add_command(label='Cut', command=cut_file, accelerator='Ctrl+X')
editmenu.add_command(label='Paste', command=paste_file, accelerator='Ctrl+P')
editmenu.add_command(label='Find', command=find_file, accelerator='Ctrl+F')
editmenu.add_command(label='Find and replace',
                     command=find_replace_file, accelerator='Ctrl+R')
menubar.add_cascade(label='Edit', menu=editmenu)
root.bind('<Control-f>', find_file)
root.bind('<Control-r>', find_replace_file)
root.bind('<Control-F>', find_file)
root.bind('<Control-R>', find_replace_file)


statsmenu.add_command(label='Word Count', command=word_count)
statsmenu.add_command(label='Character Count', command=char_count)
statsmenu.add_command(label='Date Created', command=date_created)
statsmenu.add_command(label='Date Modified', command=date_modified)
menubar.add_cascade(label='Stats', menu=statsmenu)

formatmenu.add_command(label='Font...', command=font_editor)
menubar.add_cascade(label='Format', menu=formatmenu)


thememunu.add_command(label='Light Default',
                      command=lambda: change_theme(color_dict['Light Default']))
thememunu.add_command(label='Light Plus',
                      command=lambda: change_theme(color_dict['Light Plus']))
thememunu.add_command(
    label='Dark', command=lambda: change_theme(color_dict['Dark']))
thememunu.add_command(
    label='Red', command=lambda: change_theme(color_dict['Red']))
thememunu.add_command(
    label='Monokai', command=lambda: change_theme(color_dict['Monokai']))
thememunu.add_command(label='Night Blue',
                      command=lambda: change_theme(color_dict['Night Blue']))
menubar.add_cascade(label='Theme', menu=thememunu)


root.config(menu=menubar)

scrollbar.pack(side=RIGHT, fill=Y)
menubar.add_separator()
scrollbar.config(command=textarea.yview)
textarea.config(yscrollcommand=scrollbar.set)


def statusbar_updator(event):
    global statusbar
    statusbar.destroy()
    statusbar = Label(
        root, text=f"Words : {len(textarea.get(1.0, END).split())}      |    Characters : {int(len(textarea.get(1.0, END))-1)}", bd=1, relief=SUNKEN, anchor=W)
    statusbar.place(relx=0.0,
                    rely=1.0,
                    anchor='sw')


global statusbar
statusbar = Label(
    root, text=f"Words : {len(textarea.get(1.0, END).split())}      |    Characters : {int(len(textarea.get(1.0, END)))-1}", bd=1, relief=SUNKEN, anchor=W)
statusbar.place(relx=0.0,
                rely=1.0,
                anchor='sw')
root.bind('<Key>', statusbar_updator)


root.mainloop()
