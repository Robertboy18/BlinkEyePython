# BlinkEyePython
<hr>
<img src = "https://www.researchgate.net/profile/Zoran_Duric/publication/220939414/figure/fig1/AS:305653995327488@1449884999025/Subject-with-clearly-distinct-and-consistent-eye-blink-transition-states.png">
<hr>
This project was created just for fun during a chat with some of the other interns in the Microsoft Group. One of them suggested an idea Imagine blinking to compile.

This sparked my interest and after doing some research I finally created this file which does the same exact thing except its a double blink to run. It's not completely full proof yet but feel free to open issues and suggest more ideas on how to make it a fullproof project.
<hr>

**Important Modules to Install**
```python
# Import the required modules
import pyttsx3 # text to speech
import pyautogui # keyboard control
import winsound # sound
import numpy as np
import cv2
```
<hr>

**Blinking Eye Detection Reference and important files to add**

Reference: [Github link](https://github.com/infoaryan/Eye-blink-detection-game)
<hr>

**Compile and Run**

Step 1 : Add these two relevant files to the same folder the python/jupyter-notebook is in.
  Files 1.1 haarcascade_eye_tree_eyeglasses.xml
  Files 1.2 haarcascade_frontalface_default.xml

Step 2 (Skip to step 3 if running on terminal or as a python file) : If running in Jupyter Notebook, execute the first 5 cells only. The following 5th cell is this ( Save the python files in the same folder as the rest of the xml files and the main python file/jupyter notebook.) Enter the names with the .py extension seperated by space.
```python
# enter the python file names seperated by a space
file = input("Please enter the file name : ").split()
pyautogui.press('down') # automatically goes to the next cell
pyautogui.hotkey('ctrl', 'enter') # executes the following cell
```

Example : hello.py redd.py intern.py

Step 3 : Enter the python file names again with the .py extension seperated by space.

Step 4 : Minimize the video capture tab/ keep it open

Step 5 : There will be 3 voice memos each explaining the command.

Step 6 : After the eyes are detected and a first blink is captured a prompt message will be spoken which asks for another blink , if one chooses not to blink, press q to exit or just continue programming in the side.

Step 7 : Double blink to run the file (give it a 1 second break between each blink as cv2 is a bit slow in capturing successive frames and doing detection)

Step 8 : Voila all the programs run sequentially, if your python files contain input prompts enter the required value and see the magic on it compiling all the rest of the files on its own.
<hr>

**Spoiler**

Again this was just a fun project and am open to suggestions on how to edit this and make it full proof and add more features.

<hr>
- Robert
