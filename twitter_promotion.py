from twitter import Twitter
import TwitterAPI
import config
from step import Step
from db import k_step
import requests
import urllib.request
import datetime

def delivery_period():
  now = datetime.datetime.now()
  last_day= now + datetime.timedelta(len(k_step['articles']))
  last_day = last_day.strftime("%Y年%m月%d日")
  first_day = now.strftime("%Y年%m月%d日")
  return {'first_day':first_day,'last_day':last_day}

def notify_template(periop):
  first_day = "\nステップ配信始まりました。\n配信タイトル:「{0}」\n開始日:{1}\n終了日:{2}".format(k_step['name'],periop['first_day'],periop['last_day'])
  last_day  = "\nステップ配信終了しました。\n配信タイトル:「{0}」".format(k_step['name'])
  return {'first_day':first_day,'last_day':last_day}


def notify(count,step,temp):
  url ="https://notify-api.line.me/api/notify"
  # notifyのトークン(Bearer認証)
  access_token="notifyトークン"
  headers = {'Authorization': 'Bearer ' + access_token}
  image="/Users/kazuto/projects/Python/Twitter/k_step.png"
  if count == 0:
    message = temp['first_day']
  elif step <= count:
    message = temp['last_day']
  else:
    return

  payload = {'message': message}
  files = {'imageFile': open(image, "rb")}
  r = requests.post(url, headers=headers, params=payload, files=files)

def notice(count,step):
  periop = delivery_period()
  temp=notify_template(periop)
  notify(count,step,temp)


def step_delivery():
  step = Step(k_step['articles'],config)
  if step.count == 0 :
    step.first_delivery(k_step['image'],k_step['first_temp'])
  notice(step.count,step.step)
  step.delivery(k_step['articles'][step.count]['temp'])
  step.current_step_count()
  step.update()

step_delivery()
