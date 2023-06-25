from fnmatch import filter
import os
from PIL import Image
from tkinter import Tk, Button, Label, filedialog, ttk

class GBatchCropApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gading's Batch Crop App v1.0-alpha")
        self.root.geometry("400x200")
        self.root.resizable(width=False, height=False)

        self.label = Label(self.root, text="Select the input directory:")
        self.label.pack(pady=10)

        self.select_button = Button(self.root, text="Select", command=self.select_directory)
        self.select_button.pack(pady=10)

        self.crop_button = Button(self.root, text="Crop", command=self.crop_images, state="disabled")
        self.crop_button.pack(pady=10)

        self.progBar = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progBar.pack(pady=10)

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
        w_ratio = 2*w_ratio
        h_ratio = 2*h_ratio
        m = self.threeDimensionalArray(4, tiles, tiles)
        for i in range(tiles): # columns
            for j in range(tiles): # rows
                m[i][j][0] = width*j if j != 2 else width*j-w_ratio
                m[i][j][1] = height*i if i != 2 else height*i-h_ratio
                m[i][j][2] = width*(j+1) if j == 2 else width*(j+1) + w_ratio
                m[i][j][3] = height*(i+1) if i == 2 else height*(i+1) + h_ratio
        
        # for i in range(tiles): # columns
        #     for j in range(tiles): # rows
        #         print(m[i][j])
        
        return m

    def scanImages(self, dir):
        file_list = os.listdir(dir)
        self.total_images = len(filter(file_list, '*.JPG'))
        print(self.total_images)
        return file_list

    def crop_images(self):
        output_directory = os.path.join(self.input_directory, "cropped")
        os.makedirs(output_directory, exist_ok=True)
        file_list = self.scanImages(self.input_directory)
        # image_extensions = (".JPG") #, ".jpeg", ".png"
        w = 640
        h = 360
        r1 = 16
        r2 = 9
        tiles = 3

        crop_dimensions_list = self.cropDimensionalArray(w, h, r1, r2, tiles)
        number_suffix = 1
        x = (self.total_images*(tiles**2)) / 300 # 300 is progress length
        
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
                self.progBar['value'] += x
        self.status_label.config(text="Cropping complete!")

if __name__ == "__main__":
    root = Tk()
    app = GBatchCropApp(root)
    root.mainloop()
