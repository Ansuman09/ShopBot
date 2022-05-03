from tkinter import *
from chat import get_response,bot_name
from PIL import ImageTk,Image

BG_GRAY='#ABB289'
BG_COLOR='#17202A'
TEXT_COLOR='#EAECEE'

FONT='Helvetica 14'
FONT_BOLD='Helvetica 13 bold'

class ChatApplication():

    def __init__(self):
        self.window=Tk()
        self.setup_main_window()

    def run(self):
        self.window.mainloop()

    def setup_main_window(self):
        self.window.title('Chat')
        self.window.resizable(height=False,width=False)
        self.window.configure(height=550,width=470,bg=BG_COLOR)

        #Label is a class of Tkinter and we can use it via its import
        head_label=Label(self.window,bg=BG_COLOR,fg=TEXT_COLOR,
                         text='Good Day!',font=FONT_BOLD,pady=10)
        head_label.place(relwidth=1)

        #heading
        line=Label(self.window,width=450,bg=BG_GRAY)
        line.place(relwidth=1,rely=0.07,relheight=0.012)

        #text_widget
        self.text_widget=Text(self.window,width=20,height=2,fg=TEXT_COLOR,bg='#069A8E',
                              font=FONT,padx=7,pady=5)
        self.text_widget.place(relheight=.745,relwidth=1,rely=0.08)
        self.text_widget.configure(cursor='arrow',state=DISABLED)

        #scrollbar
        scrollbar=Scrollbar(self.window)
        scrollbar.place(relheight=.75,relx=.974,rely=.08)
        scrollbar.configure(command=self.text_widget.yview)

        #bottom label
        bottom_label=Label(self.window,bg=BG_GRAY,height=80)
        bottom_label.place(relwidth=1,rely=0.82)

        #message entry
        self.msg_entry=Entry(bottom_label,bg='#F9FFA4',fg='black',font=FONT)
        self.msg_entry.place(relwidth=74,relheight=0.06,rely=0.008,relx=0.01)
        self.msg_entry.focus()
        self.msg_entry.bind('<Return>',self.on_enter_pressed) #active when return key i.e. ENTER is pressed

        # create the button
        send_button=Button(bottom_label,bg=BG_GRAY,text='send',font=FONT_BOLD,width=20,
                           command=lambda: self.on_enter_pressed(None))
        send_button.place(relx=.8,rely=0.008,relheight=0.06,relwidth=0.2)

    def on_enter_pressed(self,event):
        msg=self.msg_entry.get()
        self.insert_message(msg,'You')

    def insert_message(self,msg,sender):
        if not msg:
            return

        self.msg_entry.delete(0,END)
        msg1=f'{sender}: {msg}\n\n'
        self.text_widget.configure(state=NORMAL) #this so that we can send message to the text box after the function is actiavted
        self.text_widget.insert(END,msg1)
        self.text_widget.configure(state=DISABLED) #disable again

        self.msg_entry.delete(0,END)
        msg2=f'{bot_name}: {get_response(msg)}\n\n'
        self.text_widget.configure(state=NORMAL) #this so that we can send message to the text box after the function is actiavted
        self.text_widget.insert(END,msg2)
        self.text_widget.configure(state=DISABLED) #disable again


if __name__=='__main__':
    app=ChatApplication()
    app.run()

