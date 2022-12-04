import openai
import os
import requests
import random
import datetime


class DallE:
    def __init__(self):
        self.prompt = None
        self.file_name = None
        self.image_content = None

    def start_repl(self):
        print("Enter a prompt to generate an image with DALL E.")
        # Set up the REPL loop
        while True:
            # Prompt the user for input
            if self.prompt:
                print('Press enter to use the current prompt: "{}"'.format(self.prompt))
            if self.image_content:
                print(
                    "Enter 'save' to save the previous image in the favorites folder."
                )
            user_input = input("⎊: ")
            print("--")

            # Evaluate the user's input
            self.process_user_input(user_input)
            print("--")

    def process_user_input(self, user_input):
        if user_input == "save":
            # Save previous image to favorites
            if not self.file_name or not self.image_content:
                file_path = "images/favorites/{}".format(self.file_name)
                self.write_image_file(file_path, self.image_content, self.prompt)
                print("No image to save.")

        elif user_input == "quit":
            # Quit
            print("Exiting program.")
            return
        elif user_input != "":
            # User the user input as the prompt
            self.prompt = user_input

        image_url = self.generate_image(self.prompt)
        self.download_image(image_url, self.prompt)

    def generate_image(self, prompt):
        response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
        return response["data"][0]["url"]

    def download_image(self, image_url, prompt):
        # Fetch image and store content in memory
        response = requests.get(image_url)
        self.image_content = response.content

        # Generate a name for the file
        self.file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

        # Save image in images folder
        file_path = "images/{}".format(self.file_name)
        self.write_image_file(file_path, self.image_content, prompt)

        # Also cache image as "recent.png" for easier lookup
        file_path = "images/recent.png".format(self.file_name)
        self.write_image_file(file_path, self.image_content, prompt)

    def write_image_file(self, file_path, content, prompt):
        with open(file_path, "wb") as f:
            f.write(self.image_content)
        os.setxattr(file_path, "user.prompt", bytes(prompt, "utf-8"))
        print("Saved image in", file_path)


if __name__ == "__main__":
    openai.api_key = os.environ["OPENAI_KEY"]
    dalle = DallE()
    dalle.start_repl()
