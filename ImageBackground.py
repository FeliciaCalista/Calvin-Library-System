from PIL import Image, ImageTk

class ImageBG:
    def __init__(self, root, canvas, image_path='BACKGROUND.png'):
        self.root = root
        self.canvas = canvas                                                 

        self.image_path = image_path                                                          # Replace with your image file path
        self.load_and_resize_image()                                                                # Load and resize the image

        self.image_on_canvas = self.canvas.create_image(0, 0, anchor='nw', image=self.image_tk)     # Display the image on the canvas

        self.root.bind("<Configure>", self.on_resize)                                               # Bind the <Configure> event to resize the image when the window is resized


    def load_and_resize_image(self):
        image = Image.open(self.image_path)                                                         # Open the image using PIL
        
        self.image_width = self.root.winfo_width()                                                  # Get the current size of the root window
        self.image_height = self.root.winfo_height()
        
        resized_image = image.resize((self.image_width, self.image_height), Image.LANCZOS)          # Resize the image to fit the window size
        self.image_tk = ImageTk.PhotoImage(resized_image)


    def on_resize(self, event):                                                                     # Update the size of the image when the window is resized
        self.load_and_resize_image()                                                                # Reload the image to fit the new size
        self.canvas.config(width=event.width, height=event.height)                                  # Resize the canvas
        self.canvas.create_image(0, 0, anchor='nw', image=self.image_tk)                            # Update the image