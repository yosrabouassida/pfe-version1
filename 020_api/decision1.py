# perception -> Decision ->Navigation
from flask import Flask
import requests
import time

# ----------------------------------
r = requests.get('http://0.0.0.0:5001/envoyerMsg')
print("temps d'execution de perception")
print(r.text)
execpercep = r.text
print("request received from perception module at ")
reqperception = time.time()
print(reqperception)
r1 = requests.get('http://0.0.0.0:5001/envoyerMsg1')
print("temps d'envoi de requete de perception vers decision")
reqperceptiondeci = reqperception - (float(r1.text))
print(reqperceptiondeci)
app = Flask(__name__)
print("debut decision")
d = time.time()
print("d")
print(d)


# -------------------------------------

from gluoncv import model_zoo, data, utils
import cv2
import mxnet as mx
import gluoncv as gcv



global b

def runDetector(fast=True):
    cap = cv2.VideoCapture(0)
    if fast == True:
        net = gcv.model_zoo.get_model('yolo3_mobilenet1.0_voc', pretrained=True)
    else:
        net = model_zoo.get_model('yolo3_darknet53_coco', pretrained=True)
    net.hybridize()
    while (True):
        ret, frame = cap.read()
        frame = mx.nd.array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).astype('uint8')
        rgb_nd, frame = gcv.data.transforms.presets.ssd.transform_test(frame, short=270, max_size=2700)
        class_IDs, scores, bounding_boxes = net(rgb_nd)
        img = gcv.utils.viz.cv_plot_bbox(frame, bounding_boxes[0], scores[0], class_IDs[0], thresh=0.5,
                                         class_names=net.classes)



        for i in range(len(scores[0])):
            score = float(scores[0][i].asnumpy())
            print(score)
            if (score > 0.5) :
                b = "stop"
                print(b)
                break




        gcv.utils.viz.cv_plot_image(img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

    cv2.destroyAllWindows()


@app.route("/", methods=['GET'])
def predict222():

    response = app.response_class(
        response=runDetector(fast=True),
        status=200
    )
    return response





@app.route("/2", methods=['GET'])
def predict777():
    response = app.response_class(
        response= b,
        status=200
    )
    return response

@app.route("/1", methods=['GET'])
def predict22():
    from gluoncv import model_zoo, data, utils
    import cv2
    import mxnet as mx
    import gluoncv as gcv
    def runDetector(fast=True):

        if fast == True:
            net = gcv.model_zoo.get_model('yolo3_mobilenet1.0_voc', pretrained=True)
        else:
            net = model_zoo.get_model('yolo3_darknet53_coco', pretrained=True)
        net.hybridize()

        while (True):
            fram1 = requests.get('http://0.0.0.0:5001/')
            fram1 = mx.nd.array(cv2.cvtColor(fram1, cv2.COLOR_BGR2RGB)).astype('uint8')
            rgb_nd, fram1 = gcv.data.transforms.presets.ssd.transform_test(fram1, short=270, max_size=2700)
            class_IDs, scores, bounding_boxes = net(rgb_nd)
            img = gcv.utils.viz.cv_plot_bbox(fram1, bounding_boxes[0], scores[0], class_IDs[0], thresh=0.5,
                                             class_names=net.classes)

            gcv.utils.viz.cv_plot_image(img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()

    response = app.response_class(
        response=runDetector(fast=True),
        status=200
    )
    return response


print("le module decision s'execute")
f = time.time()
print("f")
print(f)
execdeci = f - d
print("temps d'execution du module decision")
print(execdeci)


@app.route("/envoyerMsg", methods=['GET'])
def predict():
    k1 = time.time()
    response = app.response_class(
        response=str(k1),
        status=200
    )
    return response


@app.route("/envoyerMsg1", methods=['GET'])
def predict8():
    response = app.response_class(
        response=str(execdeci),
        status=200
    )
    return response


@app.route("/envoyerMsg2", methods=['GET'])
def predict1():
    response = app.response_class(
        response=str(reqperceptiondeci),
        status=200
    )
    return response


@app.route("/envoyerMsg3", methods=['GET'])
def predict2():
    response = app.response_class(
        response=str(execpercep),
        status=200
    )
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
