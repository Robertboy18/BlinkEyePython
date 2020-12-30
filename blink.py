# enter the python file names seperated by a space
file = input("Please enter the file name : ").split()
pyautogui.press('down') # automatically goes to the next cell
pyautogui.hotkey('ctrl', 'enter') # executes the following cell


def run_pgm(runfile):
  """
  This function executes another python file from a python file.
  
  Params: runfile
  
  Return : None
  
  """
  with open(runfile,"r") as cmp:
    exec(cmp.read())


duration_n = 1000   # Set Duration To 1 second
frequency_n = 1000  # Set Frequency To 1000 Hertz

engine = pyttsx3.init() # initalize the engine

# enter the python file names seperated by a space
file = input("Please enter the file name : ").split()

#Initializing the face and eye cascade classifiers from xml files
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

#Variable store execution state
first_read = True

#Starting the video capture
cap = cv2.VideoCapture(0)
ret,img = cap.read()
check = False
count = 0
k = False
engine.say("Press q to stop the program from running by clicking on the video frame and then pressing q else just continue")
engine.runAndWait()


while ret and not check:
    ret,img = cap.read()
    #Coverting the recorded image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #Applying filter to remove impurities
    gray = cv2.bilateralFilter(gray,5,1,1)

    #Detecting the face for region of image to be fed to eye classifier
    faces = face_cascade.detectMultiScale(gray, 1.3, 5,minSize=(200,200))
    if(len(faces)>0):
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

            #roi_face is face which is input to eye classifier
            roi_face = gray[y:y+h,x:x+w]
            roi_face_clr = img[y:y+h,x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_face,1.3,5,minSize=(50,50))

            #Examining the length of eyes object for eyes
            if(len(eyes)>=2):
                #Check if program is running for detection 
                if(first_read):
                    engine.say("Eyes Detected")
                    engine.runAndWait()
                    cv2.putText(img, "Eyes detected", (100,100), cv2.FONT_HERSHEY_PLAIN, 3,(0,255,0),2)
                    k = True
                else:
                    cv2.putText(img, "Eyes open!", (100,100), cv2.FONT_HERSHEY_PLAIN, 3,(0,255,0),2)
            else:
                if(first_read):
                    #To ensure if the eyes are present before starting
                    cv2.putText(img, "No eyes detected", (100,100), cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255),2)
                else:
                    #This will print on console and restart the algorithm
                    #pyautogui.press('down')  
                    #pyautogui.hotkey('ctrl', 'enter')
                    print("Blink detected")
                    count += 1
                    #pyautogui.keyDown('down')
                    cv2.waitKey(1500)
                    #t = True
                    if count == 1:
                        engine.say("One more blink left to run the program")
                    if count == 2:
                        print("Running the Program")
                        engine.say("Blinked Twice")
                        engine.say("Running the requested Python file")
                        engine.runAndWait()
                        winsound.Beep(frequency_n, duration_n)
                        for i in file: # run if there are multiple python files
                            # each program will be runned sequentially
                            run_pgm(i)
                        check = True
                    else:
                        pass
                    first_read=True
            
    else:
        cv2.putText(img,"No face detected",(100,100),cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0),2)

    #Controlling the algorithm with keys
    if check == True:
        break
    else:
        pass
    cv2.imshow('img',img)
    a = cv2.waitKey(1)
    if(a==ord('q') or a == ord('Q')):
        break
    elif(k and first_read):
        #This will start the detection
        first_read = False
cap.release()
cv2.destroyAllWindows()