from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import time
root = Tk()

root.title('Text Editor')
root.geometry('800x700+500+300')
root.resizable(True, True)
root.configure(background='#D8D8D8')




frame_button = Frame(root)
frame_button.pack(fill=X, expand=True)
frame_text = Frame(root)
frame_text.pack(fill=BOTH, expand=True)
menu_1 = Menu(root)
root.config(menu=menu_1)
#Button

def number_of_words():
    words = []
    for word in text_area.get('1.0', END).split():
        words.append(word)
    label_num_of_words['text'] = len(words)



button_text = Button(frame_button, text='Number of words: ', fg='#000', activeforeground='#FF0040',\
                                        command=number_of_words)

button_text.pack(side=LEFT)

label_num_of_words = Label(frame_button, bg='#fff', fg='#000', padx=10)
label_num_of_words.pack(side=LEFT)
#Button Most popular word

def most_popular_word():
    dictWord = dict()
    for word in text_area.get('1.0', END).split():
        if word in dictWord:
            dictWord[word] += 1
        else:
            dictWord[word] = 0
    if len(dictWord) > 0:
        label_mostpopularword['text'] = min(dictWord.items(), key=lambda x: (-x[1], x[0]))[0]
    else:
        label_mostpopularword['text'] = 'No words'

button_mostpopularword = Button(frame_button, text='Most popular word: ', fg='#000', activeforeground='#FF0040',\
                                                                            command=most_popular_word)
button_mostpopularword.pack(side=LEFT)

label_mostpopularword = Label(frame_button, bg='#fff', fg='#000')
label_mostpopularword.pack(side=LEFT)


#File
def texteditor_quit():
    user_answer = messagebox.askokcancel(title='Quit', message='Do you want to quit?')
    if user_answer:
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title='Choose file', filetypes=(('Text documents (*.txt)', '*.txt'), \
                                                                            ('All documents', '*.*')))
    if file_path:
        text_area.delete('1.0', END)
        text_area.insert('1.0', open(file_path, encoding='utf-8').read())

def save_file():
    file_save = filedialog.asksaveasfilename(filetypes=(('Text documents (*.txt)', '*.txt'), \
                                                                            ('All documents', '*.*')))
    fout = open(file_save, 'w', encoding='utf-8')
    text = text_area.get('1.0', END)
    fout.write(text)
    fout.close()

file_menu = Menu(menu_1, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=texteditor_quit)
menu_1.add_cascade(label='File', menu=file_menu)
#Theme


def about_program():
    messagebox.showinfo(title='About notepad', message='Program Text Editor, Version 0.1, Тая, привет')


def change_theme(theme):
    text_area['bg'] = theme_colors[theme]['text_bg']
    text_area['fg'] = theme_colors[theme]['text_fg']
    text_area['insertbackground'] = theme_colors[theme]['cursor']
    text_area['selectbackground'] = theme_colors[theme]['select']


theme_menu = Menu(menu_1, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label='Light Theme', command=lambda: change_theme ('light'))
theme_menu_sub.add_command(label='Dark Theme', command=lambda: change_theme ('dark'))
theme_menu.add_cascade(label='Theme', menu=theme_menu_sub)
theme_menu.add_command(label='About program', command=about_program)
menu_1.add_cascade(label='Help', menu=theme_menu)

theme_colors = {
    'dark':
    {
    'text_bg' : '#343D46',
    'text_fg' : '#fff',
    'cursor' : '#EDA756',
    'select' : '#4E5A65',
    },
    'light':
    {
    'text_bg' : '#fff',
    'text_fg' : '#000',
    'cursor' : '#8000ff',
    'select' : '#777',
    }

}

#Text
text_area = Text(frame_text, bg=theme_colors['dark']['text_bg'], fg=theme_colors['dark']['text_fg'],\
                                                padx=15, pady=12, wrap=WORD, \
                                                insertbackground=theme_colors['dark']['cursor'],\
                                                selectbackground=theme_colors['dark']['select'],\
                                                spacing3=10,\
                                                font=('Courier New', 15))
text_area.pack(fill=BOTH, expand=True, side=LEFT)

scroll = Scrollbar(frame_text, command=text_area.yview)
scroll.pack(fill=Y, side=LEFT)
text_area.config(yscrollcommand=scroll.set)


root.mainloop()
