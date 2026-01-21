import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1)

timer = 0
stateResult = False
startGame = False
score = [0, 0]  # el pc y el jugador
imgAi = None

while True:
    imgBG = cv2.imread('Resources/BG.png')
    success, img = cap.read()
    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]

    # detectar manos
    hands, img = detector.findHands(imgScaled)

    if startGame:
        if stateResult is False:
            timer = time.time() - initalTime
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            if timer > 3:
                stateResult = True
                timer = 0

                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)

                    # detectar jugada del jugador
                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1
                    if fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2
                    if fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3

                    randoNumber = random.randint(1, 3)
                    imgAi = cv2.imread(f'Resources/{randoNumber}.png', cv2.IMREAD_UNCHANGED)

                    # mostrar la jugada del ordenador
                    imgBG = cvzone.overlayPNG(imgBG, imgAi, (149, 310))

                    # gana el jugador
                    if (playerMove == 1 and randoNumber == 3) or \
                       (playerMove == 2 and randoNumber == 1) or \
                       (playerMove == 3 and randoNumber == 2):
                        score[1] += 1

                    # gana el pc
                    if (playerMove == 3 and randoNumber == 1) or \
                       (playerMove == 1 and randoNumber == 2) or \
                       (playerMove == 2 and randoNumber == 3):
                        score[0] += 1

                    print(f"Jugador: {playerMove}, IA: {randoNumber}, Marcador: {score}")

    imgBG[234:654, 795:1195] = imgScaled

    # mostrar imagen del pc si existe
    if stateResult and imgAi is not None:
        imgBG = cvzone.overlayPNG(imgBG, imgAi, (149, 310))

    # mostrar marcador
    cv2.putText(imgBG, str(score[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(score[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    cv2.imshow('BG', imgBG)
    cv2.imshow("scaled", imgScaled)

    key = cv2.waitKey(1)

    if key == ord('s'):  # iniciar juego
        startGame = True
        initalTime = time.time()
        stateResult = False
        # no reiniciar marcador aqu

    if key == ord('r'):  # reiniciar marcador
        score = [0, 0]

    if key == ord('q'):  # salir
        break

cap.release()
cv2.destroyAllWindows()
