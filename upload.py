import tornado.web
import tornado.ioloop
from random import randint
import extractData
import os
import json
from pprint import pprint


def generateRandomName():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789_-"
    name = ""
    random = 0
    for i in range(20):
        random = randint(0, len(chars)-1)
        # print(random)
        name = name+chars[random]
    return name

# def compareValues(dict):


class uploadImgHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files["fileImage"]
        for f in files:
            fileName, extension = f.filename.split(".")
            fileName = generateRandomName()
            # print("hello file name ", fileName, " hello extension ", extension)

            fh = open(f"upload/{fileName}.{extension}", "wb")
            # fh = open(f"upload/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()

        # testing.testing(f.filename)
        res = extractData.getDataFromFile(fileName+"."+extension)
        pprint(res['dict'])
        r = json.dumps(res)
        self.write(r)
        # self.write(f"http://localhost:8080/img/{f.filename}")

    def get(self):
        self.render("index.html")


if (__name__ == "__main__"):
    app = tornado.web.Application([
        ("/", uploadImgHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler, {'path': 'upload'})
    ])

    app.listen(5000)
    print("Listening on port 5000")
    tornado.ioloop.IOLoop.instance().start()
