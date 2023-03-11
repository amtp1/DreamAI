import json

import requests
from loguru import logger

API_KEY = "AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw"
STYLE_URL = "https://paint.api.wombo.ai/api/styles/"

def createToken():
    s = requests.Session()
    r = s.post("https://firebaseinstallations.googleapis.com/v1/projects/paint-prod/installations",
            headers={"Content-Type": "application/json", "x-goog-api-key": API_KEY}, json={
            "appId": "1:181681569359:web:277133b57fecf57af0f43a",
            "authVersion": "FIS_v2",
            "sdkVersion": "w:0.5.1",
    })
    r2 = s.post("https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={}".format(API_KEY))
    return r2.json() if r.status_code == 200 else r.status_code

def createTask(token):
    r = requests.post("https://paint.api.wombo.ai/api/tasks",
                      headers={"authorization": "bearer " + str(token), "Content-Type": "text/plain;charset=UTF-8"},
                      json={"premium": False})
    return r.json() if r.status_code == 200 else r.status_code

def createArt(token, id, options={"display_freq": 10, "prompt": "example", "style": 3}):
    r = requests.put("https://paint.api.wombo.ai/api/tasks/{}".format(id),
                     headers={"authorization": "bearer " + str(token), "Content-Type": "text/plain;charset=UTF-8"},
                     json={"input_spec": options})
    return r

def getStyles():
    try:
        response = requests.get(url=STYLE_URL)
        styles = json.loads(response.text)
        return styles
    except Exception as e:
        return None

def getStyleNameById(id: int):
    styles = getStyles()
    if styles:
        for style in styles:
            if style.get('id') == id:
                return style.get('name')
    else:
        return None

def fetchState(token: str, task_id: str):
    r = requests.get("https://paint.api.wombo.ai/api/tasks/{}".format(task_id),
                     headers={"authorization": "bearer " + str(token)})
    return r

def generateImage(prompt: str, style_id: int):
    token = createToken()['idToken']
    task = createTask(token)
    createArt(token, task['id'], {"display_freq": 10, "prompt": prompt, "style": style_id})
    while True:
        fetchRes = fetchState(token, task['id'])
        if "completed" in fetchRes.json()['state']:
            return fetchRes.json()
