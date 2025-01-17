import customtkinter as ctk
from prompt_enhancer import enhance_prompt
from image_generator import ImageGenerator

class ThumbnailEnhancer(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.image_generator = ImageGenerator()

        # Window setup
        self.title("Thumbnail Prompt Enhancer")
        self.geometry("800x800")
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)

        # Create input frame
        input_frame = ctk.CTkFrame(self)
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        input_frame.grid_columnconfigure(0, weight=1)

        # Create input box
        self.input_box = ctk.CTkEntry(input_frame, placeholder_text="Enter your prompt here...")
        self.input_box.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Create generate button
        self.generate_button = ctk.CTkButton(input_frame, text="Generate", command=self.generate_thumbnail)
        self.generate_button.grid(row=0, column=1, padx=10, pady=10)

        # Create status label
        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.grid(row=1, column=0, padx=10, pady=5)

    def generate_thumbnail(self):
        input_prompt = self.input_box.get()
        if not input_prompt:
            self.status_label.configure(text="Please enter a prompt!")
            return

        print("Starting generation process...")
        self.status_label.configure(text="Enhancing prompt...")
        self.generate_button.configure(state="disabled")
        self.update()

        try:
            # Step 1: Enhance the prompt
            enhanced_prompt = enhance_prompt(input_prompt)
            print("\nEnhanced Prompt:")
            print(enhanced_prompt)
            
            # Step 2: Generate image
            self.status_label.configure(text="Generating image with Flux...")
            self.update()
            
            success, message = self.image_generator.generate_image(enhanced_prompt)
            
            if success:
                print("\nImage generation successful!")
                self.status_label.configure(text="Image saved successfully!")
            else:
                print(f"\nImage generation failed: {message}")
                self.status_label.configure(text=f"Failed: {message}")

        except Exception as e:
            print(f"Error: {str(e)}")
            self.status_label.configure(text=f"Error: {str(e)}")
        finally:
            self.generate_button.configure(state="normal")
            self.after(2000, self.quit)  # Close after 2 seconds

if __name__ == "__main__":
    app = ThumbnailEnhancer()
    app.mainloop()