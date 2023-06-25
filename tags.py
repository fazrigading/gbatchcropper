import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=530
        height=130
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_123=tk.Label(root)
        GLabel_123["anchor"] = "center"
        GLabel_123["cursor"] = "watch"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_123["font"] = ft
        GLabel_123["fg"] = "#333333"
        GLabel_123["justify"] = "center"
        GLabel_123["text"] = "Gading's Batch Cropper 1.0-alpha"
        GLabel_123.place(x=20,y=30,width=258,height=32)

        GButton_365=tk.Button(root)
        GButton_365["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_365["font"] = ft
        GButton_365["fg"] = "#000000"
        GButton_365["justify"] = "center"
        GButton_365["text"] = "Crop"
        GButton_365.place(x=430,y=80,width=70,height=25)
        GButton_365["command"] = self.GButton_365_command

        GLineEdit_333=tk.Entry(root)
        GLineEdit_333["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_333["font"] = ft
        GLineEdit_333["fg"] = "#333333"
        GLineEdit_333["justify"] = "center"
        GLineEdit_333["text"] = "Width"
        GLineEdit_333.place(x=20,y=80,width=70,height=25)

        GLineEdit_932=tk.Entry(root)
        GLineEdit_932["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_932["font"] = ft
        GLineEdit_932["fg"] = "#333333"
        GLineEdit_932["justify"] = "center"
        GLineEdit_932["text"] = "Height"
        GLineEdit_932.place(x=100,y=80,width=70,height=25)

        GLineEdit_562=tk.Entry(root)
        GLineEdit_562["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_562["font"] = ft
        GLineEdit_562["fg"] = "#333333"
        GLineEdit_562["justify"] = "center"
        GLineEdit_562["text"] = "Shift1"
        GLineEdit_562.place(x=220,y=80,width=70,height=25)

        GLineEdit_512=tk.Entry(root)
        GLineEdit_512["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_512["font"] = ft
        GLineEdit_512["fg"] = "#333333"
        GLineEdit_512["justify"] = "center"
        GLineEdit_512["text"] = "Shift2"
        GLineEdit_512.place(x=300,y=80,width=70,height=25)

        GButton_859=tk.Button(root)
        GButton_859["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_859["font"] = ft
        GButton_859["fg"] = "#000000"
        GButton_859["justify"] = "center"
        GButton_859["text"] = "Select Dir"
        GButton_859.place(x=430,y=30,width=70,height=25)
        GButton_859["command"] = self.GButton_859_command

    def GButton_365_command(self):
        print("command")


    def GButton_859_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
