#perception -> Decision ->Navigation
from flask import Flask

import time



app = Flask(__name__)



@app.route('/1')
def hello_world():
    return "hello from perception module"



@app.route("/envoyerMsg1",methods=['GET'])
def predict1():
    k=time.time()
    response = app.response_class(
        response=str(k),
        status=200
    )
    return response


def predict():
    import cv2

    cap = cv2.VideoCapture(0)

    currentFrame = 0
    while (True):

        ret, frame = cap.read()

        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        currentFrame += 1

    cap.release()
    cv2.destroyAllWindows()


@app.route("/",methods=['GET'])
def predict2():
    response = app.response_class(
        response=predict(),
        status=200
    )
    return response




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
