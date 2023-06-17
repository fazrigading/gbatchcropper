import os
from PIL import Image
from tkinter import Tk, Button, Label, filedialog, Entry


class GBatchCropApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Batch Crop App")

        self.label = Label(self.root, text="Select the input directory:")
        self.label.pack()

        self.select_button = Button(self.root, text="Select", command=self.select_directory)
        self.select_button.pack()

        self.crop_button = Button(self.root, text="Crop", command=self.crop_images, state="disabled")
        self.crop_button.pack()

        self.status_label = Label(self.root, text="")
        self.status_label.pack()

        self.input_directory = None
        self.crop_dimensions = None

    def select_directory(self):
        self.input_directory = filedialog.askdirectory()
        if self.input_directory:
            self.crop_button.config(state="normal")
            self.status_label.config(text=f"Selected directory: {self.input_directory}")

    def crop_images(self):
        output_directory = os.path.join(self.input_directory, "cropped")
        os.makedirs(output_directory, exist_ok=True)

        file_list = os.listdir(self.input_directory)
        image_extensions = (".jpg", ".jpeg", ".png")

        for file_name in file_list:
            if file_name.lower().endswith(image_extensions):
                file_path = os.path.join(self.input_directory, file_name)
                try:
                    image = Image.open(file_path)
                    cropped_image = image.crop(self.crop_dimensions)
                    output_path = os.path.join(output_directory, file_name)
                    cropped_image.save(output_path)
                except (IOError, OSError):
                    pass

        self.status_label.config(text="Cropping complete!")

        self.crop_button.config(state="disabled")
        self.input_directory = None
        self.crop_dimensions = None

    def set_crop_dimensions(self):
        CropDimensionsDialog(self.root, self)


class CropDimensionsDialog:
    def __init__(self, root, app):
        self.app = app

        self.dialog = Tk()
        self.dialog.title("Set Crop Dimensions")

        self.label = Label(self.dialog, text="Enter the crop dimensions (left, top, right, bottom):")
        self.label.pack()

        self.entry = Entry(self.dialog)
        self.entry.pack()

        self.confirm_button = Button(self.dialog, text="Confirm", command=self.confirm_crop_dimensions)
        self.confirm_button.pack()

    def confirm_crop_dimensions(self):
        dimensions = self.entry.get().split(",")
        if len(dimensions) == 4:
            try:
                self.app.crop_dimensions = tuple(map(int, dimensions))
                self.app.crop_button.config(state="normal")
                self.dialog.destroy()
            except ValueError:
                pass


if __name__ == "__main__":
    root = Tk()
    app = GBatchCropApp(root)
    root.mainloop()
