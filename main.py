import os
from PIL import Image, ImageTk
from tkinter import Tk, Button, Label, filedialog, Entry

class GBatchCropApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gading's Batch Crop App v1.0-alpha")
        self.root.geometry("400x150")

        self.label = Label(self.root, text="Select the input directory:")
        self.label.pack()

        self.select_button = Button(self.root, text="Select", command=self.select_directory)
        self.select_button.pack()

        self.crop_button = Button(self.root, text="Crop", command=self.crop_images, state="disabled")
        self.crop_button.pack()

        self.status_label = Label(self.root, text="")
        self.status_label.pack()

    def select_directory(self):
        self.input_directory = filedialog.askdirectory()
        if self.input_directory:
            self.status_label.config(text=f"Selected directory: {self.input_directory}")
            self.crop_button.config(state="normal")

    def threeDimensionalArray(self, coords_num=4, columns=3, rows=3):
        '''Construct a three-dimensional array from coordinates number, columns, and rows.'''
        x = [[[0 for _ in range(coords_num)] for _ in range(columns)] for _ in range(rows)]
        return x
    
    def cropDimensionalArray(self, width, height, w_ratio, h_ratio, tiles):
        '''
        Width: width of the cropped image (in pixels)
        Height: height of the cropped image (in pixels)
        W_ratio: width ratio of the cropped image 
        H_ratio: height ratio of the cropped image
        Tiles: number of tiles
        '''
        crop_dimensions_list = self.threeDimensionalArray(4, tiles, tiles)
        for i in range(tiles): # columns
            for j in range(tiles): # rows
                crop_dimensions_list[i][j][0] = width*j
                crop_dimensions_list[i][j][1] = height*i
                crop_dimensions_list[i][j][2] = width*(j+1) if j == 2 else width*(j+1)+(2*w_ratio)
                crop_dimensions_list[i][j][3] = height*(i+1) if i == 2 else height*(i+1)+(2*h_ratio)
        return crop_dimensions_list

    def crop_images(self):
        output_directory = os.path.join(self.input_directory, "cropped")
        os.makedirs(output_directory, exist_ok=True)
        file_list = os.listdir(self.input_directory)
        # image_extensions = (".JPG") #, ".jpeg", ".png"
        tiles = 3
        crop_dimensions_list = self.cropDimensionalArray(640, 360, 16, 9, tiles)
        number_suffix = 1
        for i in range(tiles):
            for j in range(tiles):
                self.crop_dimensions = tuple(crop_dimensions_list[i][j])
                for file_name in file_list:
                    if file_name.endswith(".JPG"):
                        file_path = os.path.join(self.input_directory, file_name)
                        try:
                            image = Image.open(file_path)
                            cropped_image = image.crop(self.crop_dimensions)
                            new_file_name = file_name.rstrip(".JPG")
                            new_file_name = new_file_name + "_" + str(number_suffix) + ".JPG"
                            output_path = os.path.join(output_directory, new_file_name)
                            cropped_image.save(output_path)
                        except (IOError, OSError):
                            pass
                number_suffix += 1
        self.status_label.config(text="Cropping complete!")

if __name__ == "__main__":
    root = Tk()
    app = GBatchCropApp(root)
    root.mainloop()
