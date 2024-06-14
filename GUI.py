from tkinter import *
from PIL import Image, ImageTk
import action
import speech_to_text


root = Tk()
root.title("Virtual Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="#171616")


# functions
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, 'User--->'+ user_val+"\n")

    if bot_val != None:
        text.insert(END, "BOT <---"+ str(bot_val)+"\n")
    if bot_val == "Okey sir":
        root.destroy()


def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, 'User--->'+ send+"\n")

    if bot != None:
        text.insert(END, "BOT <---"+ str(bot)+"\n")
    if bot == "Okey sir":
        root.destroy()


def del_text():
    text.delete('1.0', "end")

def on_entry_click(event):
    if entry.get() == "Ask from me":
        entry.delete(0, "end")
        entry.insert(0, "")

def on_focusout(event):
    if entry.get() == "":
        entry.insert(0, "Ask from me")

#frame
frame = LabelFrame(root, padx=100, pady = 7, borderwidth=3, relief="raised")
frame.config(bg="#EAE7E7")
frame.grid(row = 0, column = 1, padx = 55, pady = 10)

#text label
text_label = Label (frame, text="Virtual Assistant", font=("Kanit", 14, "bold"), bg="#356696")
text_label.grid(row = 0, column = 0, padx = 20, pady = 10 )


#image
image = ImageTk.PhotoImage(Image.open("image/4416482-removebg-preview.png"))
image_label = Label(frame, image=image)
image_label.grid(row = 1, column = 0, pady = 20)

#input a text_area
text = Text(root, font=("courier", 10, "bold"), bg="#356696")
text.grid(row = 2, column = 0)
text.place(x = 100, y = 375, width = 375, height = 100)


#enrty text_area
entry = Entry(root, justify=CENTER, fg="#2D2D2D")
entry.insert(0, "Ask from me")
entry.bind('<FocusIn>', on_entry_click) 
entry.bind('<FocusOut>', on_focusout) 
entry.place(x=100, y=500, width=375, height=30)

#buttons
Button1 = Button(root, text="Ask" , bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID , command=ask)
Button1.place(x=70, y=575)

Button2 = Button(root, text="Send" , bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID , command=send)
Button2.place(x=400, y=575)

Button3 = Button(root, text="Delete" , bg="#356696", pady=16, padx=40, borderwidth=3, relief=SOLID , command=del_text)
Button3.place(x=230, y=575)




root.mainloop()