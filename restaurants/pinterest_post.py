import base64
import json
import requests
import os

class Pinterest:


    def get_token(self,token_name):
        access_token = os.getenv('PWD') + '/access_tokens.sh'
        f = open(access_token, 'r+')
        lines = f.readlines()
        for line in lines:
            tokens = line.strip().split('=')
            if tokens[0] == token_name:
                return tokens[1].strip()
        return "ERR NOT FOUND"

    def __init__(self):
        self.access_token = self.get_token("PINTEREST_ACCESS_TOKEN")
        self.board_id = self.get_token("PINTEREST_BOARD_ID")
        self.user = 'sourabhs1919'
        self.board_name = 'Qeats-app'
#TODO: CRIO_TASK_MODULE_PINTEREST_SHARE
# As part of this module you are expected to complete the publish_photo_msg function
# Tasks:
# 1) You need to register as pinterest developer to obtain app_id & app_secret
# 2) Obtain an access token using Postman method and store it in access_tokens.sh
# 3) Obtain Pinterest board ID by creating a Pinterest Board using the Pinterest Create Board API
#    (https://developers.pinterest.com/docs/api/boards/) and store it in access_tokens.sh
# 4) Enter board_id & access_token in access_tokens.sh - IMPORTANT step
#    PINTEREST_BOARD_ID=board_id
#    PINTEREST_ACCESS_TOKEN=access_token
# 5) Complete the publish_photo_msg() function. This function should publish a pin with
#    the given message and photo. The post should be published to the board you have created
#    in the earlier step
# 6) Manually verify the pin created and submit the code
#
# NOTE: The Pinterest API has a rate limit of 10 requests/hour. If you exceed
#       this limit, you can either wait until the rate counter resets or create
#       a new board and use it to test your implementation.

# Args:
#   1) message   -> string message to be posted
#   2) image_url -> publicly accessible url of the image to be posted

# write your code below
    def publish_photo_msg(self, message, url):
        host = 'https://api.pinterest.com/boards/' + str(self.user) + '/' + str(self.board_name) + '/pins/' 
        data = {
            "url" : url,
            "note" : message,
            "access_token" : self.access_token,
            "id" : self.board_id,
            "link": None
        }
        r = requests.post(url=host, data=data)
        return r
if __name__ == '__main__':
    pinterest = pinterest()
    img_url2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/T%C3%BCrk_Kahvesi_-_Bakir_Cezve.jpg/1200px-T%C3%BCrk_Kahvesi_-_Bakir_Cezve.jpg"
    msg1 = "Fav Of SS"
    img_url1 = "https://images.news18.com/ibnlive/uploads/2016/10/coffee-feautred-1.jpg"
    msg2 = "Second Fav Of SS"
    pinterest.publish_photo_msg(msg1,img_url1)
