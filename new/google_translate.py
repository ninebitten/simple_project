from tkinter import *
import googletrans
import textblob

from tkinter import ttk, messagebox
from googletrans import Translator


root = Tk()


root.title("Translator")
# root.iconbitmap('')
root.geometry("500x800")


def translate_it():
    
    translated_text.delete(1.0,END)
    try:
        
        
        #get language from dictionary keys
        for key, value in languages.item():
            if(value == original_combo.get()):
                from_language_key = key
                
        for key, value in languages.item():
            if(value == translated_combo.get()):
                to_language_key = key
                
                words = textblob.TextBlob(original_text.get(1.0, END))
                
                
                words = words.translate(from_lang=from_language_key, to=to_language_key)
                
                translated_text.insert(1.0, words)
        
    except Exception as e:
        messagebox.showerror("Translator", e)


def clear():
    
    
    original_text.delete(1,0, END)
    translated_text.delete(1,0, END)
    
# language_list = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,15,15,16,13,17,18,19,20,21,23,24,23,2,43,23,23,24,24,25,26)
#grab language list

languages = googletrans.LANGUAGES
# print(language)


language_list = list(languages.values())
print(language_list)



original_text = Text(root,height=10, width=40)
original_text.grid(row=0,column=0, pady=20,padx=10)
translate_button = Button(root, text="Translate!", font=("Helvetica", 24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)


translated_text = Text(root,height=10, width=40)
translated_text.grid(row=0,column=2, pady=20,padx=10)


#combo box


original_combo = ttk.Combobox(root,width=50,value=language_list)
original_combo.current(26)
original_combo.grid(row=1,column=0)





translated_combo = ttk.Combobox(root,width=50,value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1,column=2)



#clear button

clear_button = Button(root, text="clear", command=clear)
clear_button.grid(row=2,column=1)


root.mainloop()
