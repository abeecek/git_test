#Flask project
 
# from flask import Flask 
# from datetime import datetime
# app = Flask(__name__)
#   
# @app.route("/")
# def index():
#     return ("Current datetime:{}".format(str(datetime.now())))
# if __name__ == "__main__":
#     app.run(host = "localhost")
      


#****************************************************************************************888

from datetime import datetime
import ctypes
import os
# import sys

from flask import Flask 
    
app = Flask(__name__)

@app.route("/")     #decorater
def index():
    return str(get_image_and_id())
    
@app.route("/change/<int:image_id>")
def change_screensaver(image_id):
    image_infos = get_image_and_id()
    image_name = image_infos[int(image_id) -1][1]
    screensaver(image_name)
    return "Screensaver changed to {}".format(image_name)

def get_image_and_id():
    images = os.listdir("images")
    image_infos = []
    print "Id image_name"
    for index,image_name in enumerate(images): 
        print index+1,image_name
        image_infos.append([index+1,image_name])
    return image_infos
    
def screensaver(image_name = ''):
    file_path = os.getcwd()
    image_path = os.path.join(file_path,"images",image_name)
    SETDESKWALLPAPER=20
    ctypes.windll.user32.SystemParametersInfoA(SETDESKWALLPAPER,
                                            0,
                                            image_path,
                                            0
                                            )

if __name__ == "__main__":
    app.run(host = "localhost", port=555)
	
print "Hello this is git test."
    
print "Hello this is git test"
    
    
    
    
    
    
    
    
#     NOTES:
#     int    | <int:variable>
#     float  | <float:variable>
#     str    | <variable