from twitter import Twitter
import TwitterAPI
import config

class Step:
  def __init__(self,datas,config):
    self.datas = datas
    self.step = len(datas)-1
    self.twitter = Twitter(config)
    f=open("/Users/kazuto/projects/Python/Twitter/step.csv")
    self.count =int(f.read())
  def delivery(self,template):
    self.twitter.tweet(template)

  def first_delivery(self,image,template):
    self.twitter.image_tweet(template,image)

  def current_step_count(self):
    if self.step <= self.count:
      self.count = 0
      return
    self.count += 1

  def update(self):
    with open("/Users/kazuto/projects/Python/Twitter/step.csv","w") as f:
      self.count = str(self.count)
      f.write(self.count)
