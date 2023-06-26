from fnmatch import filter as fnfilter
import os
from PIL import Image
from tkinter import Tk, Button, Label, filedialog, ttk

# TODO:
# - Add Input Fields: width, height, ratio, and custom "cropped" folder name.

class GBatchCropApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gading's Batch Crop App v1.1-alpha")
        self.root.geometry("500x250")
        self.root.resizable(width=False, height=False)

        self.label = Label(self.root, text="Select the input directory:")
        self.label.pack(pady=10)

        self.select_button = Button(self.root, text="Select", command=self.select_directory)
        self.select_button.pack(pady=10)

        self.crop_button = Button(self.root, text="Crop", command=self.crop_images, state="disabled")
        self.crop_button.pack(pady=10)

        self.progBar = ttk.Progressbar(self.root, length=400)
        self.progBar.pack(pady=10)

        self.image_status = Label(self.root, text="0 of 0 images cropped")
        self.image_status.pack(pady=5)

        self.status_label = Label(self.root, text="Waiting for input...")
        self.status_label.pack(pady=5)

    def set_img_resolution(self, w, h, r1, r2, t):
        self.w = w
        self.h = h
        self.r1 = r1
        self.r2 = r2
        self.tiles = t
        return self.w, self.h, self.r1, self.r2, self.tiles

    def select_directory(self):
        self.input_directory = filedialog.askdirectory()
        if self.input_directory:
            self.status_label.config(text=f"Selected directory: {self.input_directory}")
            self.crop_button.config(state="normal")
            self.scanImages(self.input_directory)
            w, h, r, s, t = self.set_img_resolution(720, 480, 3, 2, 3)
            self.crop_dimensions_list = self.cropDimensionalArray(w, h, r, s, t)
            self.number_suffix = 1
            self.total_cropped_images = self.total_images*(self.tiles**2) # 300 is progress length
            self.progBar['maximum'] = self.total_cropped_images
            self.image_status['text'] = "0 of {} images cropped".format(self.total_cropped_images)

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
        w_ratio = 10*w_ratio
        h_ratio = 10*h_ratio
        m = self.threeDimensionalArray(4, tiles, tiles)
        for i in range(tiles): # columns
            for j in range(tiles): # rows
                m[i][j][0] = width*j if j != 2 else width*j-w_ratio
                m[i][j][1] = height*i if i != 2 else height*i-h_ratio
                m[i][j][2] = width*(j+1) if j == 2 else width*(j+1) + w_ratio
                m[i][j][3] = height*(i+1) if i == 2 else height*(i+1) + h_ratio
        return m

    def scanImages(self, dir):
        self.file_list = os.listdir(dir)
        self.total_images = len(fnfilter(self.file_list, '*.JPG'))
        print(self.total_images)

    def crop_images(self):
        folder_name = "cropped"
        output_directory = os.path.join(self.input_directory, "cropped")
        os.makedirs(output_directory, exist_ok=True)
        # image_extensions = (".jpg", ".jpeg", ".png")
        
        for i in range(self.tiles):
            for j in range(self.tiles):
                self.crop_dimensions = tuple(self.crop_dimensions_list[i][j])
                for file_name in self.file_list:
                    if file_name.endswith(".JPG"):
                        file_path = os.path.join(self.input_directory, file_name)
                        try:
                            image = Image.open(file_path)
                            cropped_image = image.crop(self.crop_dimensions)
                            new_file_name = file_name.rstrip(".JPG")
                            new_file_name = new_file_name + "_" + str(self.number_suffix) + ".JPG"
                            output_path = os.path.join(output_directory, new_file_name)
                            cropped_image.save(output_path)
                        except (IOError, OSError):
                            pass
                self.number_suffix += 1
                self.root.update_idletasks()
                self.progBar['value'] += self.total_images
                self.image_status['text'] = "{} of {} images cropped".format(int(self.progBar['value']), self.total_cropped_images)
                self.root.after(100)
        self.status_label.config(text="Cropping complete!")

if __name__ == "__main__":
    root = Tk()
    app = GBatchCropApp(root)
    root.mainloop()
