import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Gading's Batch Cropper 1.0-alpha")
        #setting window size
        width=550
        height=150
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        res_label=tk.Label(root)
        res_label["cursor"] = "arrow"
        ft = tkFont.Font(size=12)
        res_label["font"] = ft
        res_label["fg"] = "#333333"
        res_label["justify"] = "left"
        res_label["text"] = "Resolution"
        res_label.place(x=20,y=20,width=80,height=30)

        crop_button=tk.Button(root)
        crop_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(size=10)
        crop_button["font"] = ft
        crop_button["fg"] = "#000000"
        crop_button["justify"] = "center"
        crop_button["text"] = "Crop"
        crop_button.place(x=450,y=50,width=70,height=25)
        crop_button["command"] = self.GButton_365_command

        field_width=tk.Entry(root)
        field_width["borderwidth"] = "1px"
        ft = tkFont.Font(size=10)
        field_width["font"] = ft
        field_width["fg"] = "#333333"
        field_width["justify"] = "center"
        field_width["text"] = "Width"
        field_width.place(x=20,y=50,width=70,height=25)

        GLineEdit_932=tk.Entry(root)
        GLineEdit_932["borderwidth"] = "1px"
        ft = tkFont.Font(size=10)
        GLineEdit_932["font"] = ft
        GLineEdit_932["fg"] = "#333333"
        GLineEdit_932["justify"] = "center"
        GLineEdit_932["text"] = "Height"
        GLineEdit_932.place(x=100,y=50,width=70,height=25)

        GLineEdit_562=tk.Entry(root)
        GLineEdit_562["borderwidth"] = "1px"
        ft = tkFont.Font(size=10)
        GLineEdit_562["font"] = ft
        GLineEdit_562["fg"] = "#333333"
        GLineEdit_562["justify"] = "center"
        GLineEdit_562["text"] = "W_Ratio"
        GLineEdit_562.place(x=190,y=50,width=70,height=25)

        GLineEdit_512=tk.Entry(root)
        GLineEdit_512["borderwidth"] = "1px"
        ft = tkFont.Font(size=10)
        GLineEdit_512["font"] = ft
        GLineEdit_512["fg"] = "#333333"
        GLineEdit_512["justify"] = "center"
        GLineEdit_512["text"] = "H_Ratio"
        GLineEdit_512.place(x=270,y=50,width=70,height=25)

        GButton_859=tk.Button(root)
        GButton_859["bg"] = "#f0f0f0"
        ft = tkFont.Font(size=10)
        GButton_859["font"] = ft
        GButton_859["fg"] = "#000000"
        GButton_859["justify"] = "center"
        GButton_859["text"] = "Select Dir"
        GButton_859.place(x=370,y=50,width=70,height=25)
        GButton_859["command"] = self.GButton_859_command

        GLabel_282=tk.Label(root)
        GLabel_282["cursor"] = "arrow"
        ft = tkFont.Font(size=12)
        GLabel_282["font"] = ft
        GLabel_282["fg"] = "#333333"
        GLabel_282["justify"] = "left"
        GLabel_282["text"] = "Aspect Ratio"
        GLabel_282.place(x=190,y=20,width=84,height=30)

    def GButton_365_command(self):
        print("command")


    def GButton_859_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
