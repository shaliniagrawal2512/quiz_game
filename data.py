import requests
class QuestionData():
    def __init__(self):
        pass
    
    def get_question(self):
        data=requests.get("https://opentdb.com/api.php?amount=50&type=boolean")
        final_data=data.json()
        return final_data["results"]
        