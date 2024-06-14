# Code Setup
You will need several things set up before you can even begin to start coding.

## Folder Structure
You should create a folder for your bot project. \
open this folder in your code editor. \

## Files and virtual environment
Virtual environments are a way to keep your project dependencies separate from other projects. \
To create a virtual environment, open a terminal in your project folder and run the following command:
```bash
python -m venv .venv
```
This will create a folder called `.venv` in your project folder. \
Once you have created the virtual environment, your code editor should prompt you choose this environment for this project. \
If not, you can activate the virtual environment by running the following command in your terminal:
```bash
source .venv/bin/activate
```
You should see `(.venv)` at the beginning of your terminal prompt. \
You can deactivate the virtual environment by running the following command in your terminal:
```bash
deactivate
```
Note: you will need to activate the virtual environment every time you open a new terminal window. **
so it is recommended to use the terminal in your code editor, 
and choose the virtual environment for this project. so evey time you open a new terminal window in your code editor, it will automatically activate the virtual environment. \
Note: **you should never commit the `.venv` folder to your git repository.**


Once you have set up the virtual environment, you will want to create 2 files in your project folder:
- `main.py` - this is where your bot code will go.
- `.env` - this is where you will store your bot token. \

inside the `.env` file, you should have the following:
```env
DISCORD_TOKEN="your-bot-token-here"
```

## Installing dependencies
You will need to install the following dependencies for your bot:
- `pycord` - the library we will be using to interact with the discord api.
```bash
pip install py-cord
```
- `python-dotenv` - a library to read the `.env` file.
```bash
pip install python-dotenv
```

#### *Alternatively*

You can create a `requirements.txt` file in your project folder with the following:
```txt
py-cord~=2.5.0
python-dotenv==1.0.1
```
and then run the following command in your terminal:
```bash
pip install -r requirements.txt
```
Now you are year to start coding your bot. \

