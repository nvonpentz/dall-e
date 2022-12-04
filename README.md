# DALL E tool
A command line tool for generating DALL E images.

## Setup
Set up virtual env
```
virtualenv .venv
```

Activate virtualenv
```
source .venv/bin/activate
```

Install python dependences
```
pip install -r requirements.txt
```

Add a `.env` using `.env.example` as a template, replacing with real values.  Then add those variables to your environment.
```
source .env
```

## Using
Start the command line prompt
```
python dall-e.py
```

Generating an image with a prompt:
```
Enter a prompt to generate an image
⎊: rocky mountain range in the style of national geographic
--
Saved image in images/2022-12-04_12:25:37
Saved image in images/recent.png
--
Press enter to use the current prompt: "rocky mountain range in the style of national geographic"
Enter 'save' to save the previous image in the favorites folder.
⎊:
```

The images will be in the `images` folder and the names are timestamps.  The prompt used to generate the image is saved in the metadata of the file.
