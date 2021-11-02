import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxhands=2, detectionCon=0.65, trackCon=0.5):
        """
        初始化参数
        :param mode: 是否输入静态图像
        :param maxhands: 检测到手的最大数量
        :param detectionCon: 检测手的置信度
        :param trackCon: 追踪手的置信度
        """
        self.mode = mode
        self.maxhands = maxhands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxhands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        """
        检测手掌
        :param img:要识别的一帧图像
        :param draw:是否对手的标志点进行绘图
        :return:绘画完成的一帧图像
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, personDraw=True):
        """
        检测手的标志点
        :param img: 要识别的一帧图像
        :param handNo: 手的编号
        :param personDraw: 是否对手的标志点进行个性化绘图
        :return: 手的21个标志点位置
        """
        lmList = []
        if self.results.multi_hand_landmarks:
            myhand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myhand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if personDraw:
                    cv2.circle(img, (cx, cy), int(w / 50), (255, 0, 255), cv2.FILLED)
        return lmList


if __name__ == "__main__":

    pTime = 0  # 开始时间初始化

    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img, draw=True)
        lmList = detector.findPosition(img, personDraw=False)
        if len(lmList) != 0:
            pass
            # print(lmList[4])  # 大拇指最上部点的坐标

        res = ""

        img = cv2.flip(img, 1)
        cv2.putText(img, res, (10, 70), cv2.QT_FONT_BLACK, 1,
                    (0, 0, 255), 1)
        cv2.imshow("Image", img)
        cv2.waitKey(1)