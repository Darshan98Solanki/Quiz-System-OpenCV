import cv2
import csv
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
import keyboard


class MCQ:
    def __init__(self, data):
        self.question = data[0]
        self.choice1 = data[1]
        self.choice2 = data[2]
        self.choice3 = data[3]
        self.choice4 = data[4]
        self.answer = int(data[5])
        self.userans = None

    def update(self, cur, bboxs, img):
        # print(bboxs)
        for x, bbox in enumerate(bboxs):
            x1, y1, x2, y2 = bbox
            if x1 << x2 and y1 << y2:
                if x1 < cur[0] < x2 and y1 < cur[1] < y2:
                    MCQ.userans = x + 1
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)
                    # print(self.userans)
                    return img


root = Tk()
root.geometry("700x580")
Label(root, text="Quiz System", font=("times new roman", 30, "bold"), ).pack()
f1 = LabelFrame(root)
f1.pack()
l1 = Label(f1)
l1.pack()

path = "mcq.csv"
with open(path, newline="\n") as f:
    reader = csv.reader(f)
    dataAll = list(reader)[1:]

mcqList = []
for i in dataAll:
    mcqList.append(MCQ(i))

enno = str(input("Enter Enrollment no : "))
Qno = 0
TotalQ = len(dataAll)
useranswer = [0] * TotalQ
print(useranswer)
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8)
img = None
score = 0

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if Qno < TotalQ:
        mcq = mcqList[Qno]

        img, bbox = cvzone.putTextRect(img, mcq.question, [30, 50], 1, 1, font=cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                       offset=20,
                                       border=5)

        if useranswer[Qno] == 1:
            img, bbox1 = cvzone.putTextRect(img, mcq.choice1, [30, 200], 1, 1, colorR=(0, 255, 0), colorT=(0, 0, 0),
                                            colorB=(71, 99, 255),
                                            font=cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                            offset=20,
                                            border=5)
        else:
            img, bbox1 = cvzone.putTextRect(img, mcq.choice1, [30, 200], 1, 1, font=cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                            offset=20,
                                            border=5)
        if useranswer[Qno] == 2:
            img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [380, 200], 1, 1, colorR=(0, 255, 0),
                                            colorT=(0, 0, 0),
                                            colorB=(71, 99, 255),
                                            font=cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                            offset=20,
                                            border=5)
        else:
            img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [380, 200], 1, 1, font=cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                            offset=20,
                                            border=5)

        if useranswer[Qno] == 3:
            img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [30, 350], 1, 1, colorR=(0, 255, 0), colorT=(0, 0, 0),
                                            colorB=(71, 99, 255),
                                            font=cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                            offset=20,
                                            border=5)
        else:
            img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [30, 350], 1, 1, font=cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                            offset=20,
                                            border=5)
        if useranswer[Qno] == 4:
            img, bbox4 = cvzone.putTextRect(img, mcq.choice4, [380, 350], 1, 1, colorR=(0, 255, 0),
                                            colorT=(0, 0, 0),
                                            colorB=(71, 99, 255),
                                            font=cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                            offset=20,
                                            border=5)
        else:
            img, bbox4 = cvzone.putTextRect(img, mcq.choice4, [380, 350], 1, 1, font=cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                            offset=20,
                                            border=5)

        if hands:
            lmlist = hands[0]['lmList']
            cursor = lmlist[8]
            length, info = detector.findDistance(lmlist[8][0:2], lmlist[12][0:2])
            if length < 40:
                img = MCQ.update(MCQ, cursor, [bbox1, bbox2, bbox3, bbox4], img)
                if MCQ.userans is not None:
                    time.sleep(.15)
                    useranswer[Qno] = MCQ.userans
                    if Qno < TotalQ - 1 and Qno != TotalQ + 1:
                        Qno += 1
                        print(useranswer, " ", Qno)
        # progress bar
        if Qno == TotalQ - 1 and useranswer[TotalQ - 1] != 0:
            barvalue = 20 + (580 // TotalQ) * TotalQ
        else:
            barvalue = 20 + (580 // TotalQ) * Qno
        cv2.rectangle(img, (20, 420), (barvalue, 460), (0, 255, 0), cv2.FILLED)
        cv2.rectangle(img, (20, 420), (600, 460), (255, 0, 255), 5)

        # cv2.imshow("img", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if (cv2.waitKey(1) & keyboard.is_pressed('f')) and Qno < TotalQ - 1 and Qno != TotalQ + 1:
            print("forward", Qno)
            Qno += 1
        if (cv2.waitKey(1) & keyboard.is_pressed('b')) and Qno > 0 and Qno != TotalQ + 1:
            print("backward", Qno)
            Qno -= 1
        if (cv2.waitKey(1) & keyboard.is_pressed('d')) and Qno > 0:
            Qno = TotalQ + 1
            print("Done", Qno)
            no = 0
            for mcq in mcqList:
                # print(useranswer[no], " ", mcq.answer)
                # print(type(useranswer[no]),type(mcq.answer))
                if useranswer[no] == mcq.answer:
                    score += 1
                    print(score)
                no += 1
            percentage = round((score / TotalQ) * 100, 2)
            with open("answers.csv", 'a') as csvfile:
                csvwrite = csv.writer(csvfile)
                csvwrite.writerow([enno, TotalQ, score, percentage])
            print(useranswer)
    if Qno == TotalQ + 1:
        img, _ = cvzone.putTextRect(img, "Quiz Is Completed", [160, 150], 2, 2, border=3)
        img, _ = cvzone.putTextRect(img, f'Your Score : {percentage}%', [160, 300], 2, 2, border=3)
    cv2.waitKey(1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img))
    l1['image'] = img
    root.update()
