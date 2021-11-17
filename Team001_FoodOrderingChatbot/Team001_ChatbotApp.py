from tkinter import *
from Team001_Main import get_response, bot_name
from PIL import Image, ImageTk

class ChatBot:

    def __init__(self):
        self.window = Tk()
        self._design_window()

    def  run(self):
        self.window.mainloop()

    def _design_window(self):
        self.window.title("001's Food Ordering Chatbot")
        self.window.resizable(width=False,height=False)
        self.window.configure(width=900,height=750,bg='white')

        #Create a heading label
        head_label = Label(self.window, bg='#17202A', fg='white',
                           text="~Welcome to 001's Food Ordering ChatBot~",font='#EAECEE 14',pady=10)
        head_label.place(relwidth=1)
        
        #Create a label to explain the instructions
        Instruction_label = Label(self.window,width=450,bg='grey',fg='white',text="Basic Instructions:\n1. To order, please enter the code of the food.\
For orders with more than one item,please add a space in between (e.g. 0 1).\n2. To check your order, please enter 'myorder'.\n3. To confirm your order, please enter 'confirm'.\n4. \
To cancel your order, please enter 'cancel' and the code of the food to be cancelled (e.g. cancel 0).\n5. To exit, please enter 'x'."
                                  ,font='arial 10',justify='left')
        Instruction_label.place(relwidth=1,rely=0.06,relheight=0.16)

        #text widget
        self.text_widget = Text(self.window,width=20,height=2,bg='black',fg='white',
                                font='arial 14', padx=5,pady=5)
        self.text_widget.place(relheight=0.675,relwidth=1,rely=0.22)
        self.text_widget.configure(cursor="arrow",state=DISABLED)

        #Create a scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1,relx=0.98)
        scrollbar.configure(command=self.text_widget.yview)

        #Create a line to separate the text widget and bottom part
        divider = Label(self.window,width=450,bg='grey')
        divider.place(relwidth=1,rely=0.89,relheight=0.012)

        #bottom part
        bottom_box = Label(self.window,bg='Black',height=80)
        bottom_box.place(relwidth=1,rely=0.9)

        #Creat a message entry box
        self.msg_entry = Entry(bottom_box,bg="white", fg='black', font='arial 14')
        self.msg_entry.place(relwidth=0.74,relheight=0.04,rely=0.01,relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>",self._on_enter_pressed)

        #Create a button
        send_button=Button(bottom_box,text="Send>>>", font='arial 14', width=20,bg='grey',
                           command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77,rely=0.01,relheight=0.04,relwidth=0.22)

        
    def _on_enter_pressed(self,event):
        msg = self.msg_entry.get()
        
        self._insert_message(msg,"You")

    def _insert_message(self,msg,sender):
        #import and resize profile picture for user and chatbot
        Chatbot_Image=Image.open('Team001_ChatbotPic.png')
        User_Image=Image.open('Team001_UserPic.png')
        resized_Chatbot_image= Chatbot_Image.resize((30,30), Image.ANTIALIAS)
        resized_User_image= User_Image.resize((30,30), Image.ANTIALIAS)
        self.photoImg=ImageTk.PhotoImage(resized_Chatbot_image)
        self.photoImg2=ImageTk.PhotoImage(resized_User_image)

        if not msg:
            return
        if msg=="x" or msg=="X":
            self.window.destroy()

        #insert user's messages in the text widget
        self.msg_entry.delete(0,END)
        msg1 = f"{sender}: \n{msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.image_create(END,image=self.photoImg2)
        msg11=self.text_widget.insert(END,msg1)
        self.text_widget.configure(state=DISABLED)

        #insert chatbot's messages in the text widget
        msg2 = f"{bot_name}: \n{get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.image_create(END,image=self.photoImg)
        self.text_widget.insert(END,msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)
        
        

if __name__ == "__main__":
    app = ChatBot()
    app.run()

