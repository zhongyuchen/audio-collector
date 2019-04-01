import base64


def ToFile(txt, file):
    with open(txt, 'r') as fileObj:
        b64_string = fileObj.read()
        ori_image_data = base64.b64decode(b64_string)
        fout = open(file, 'wb')
        fout.write(ori_image_data)
        fout.close()


ToFile("input.txt", "output.wav")
