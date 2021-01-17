
# K-STEP
![k-step](/images/k_step.png)
# Description
KーSTEPは、LステップというLINEの配信サービスの「ステップシナリオ配信」を参考にして、当ブログ「Kazugramming」のTwitter botにもステップ配信を導入をしました。LINE Notfy APIを用いて、ステップ配信開始日とステップ配信終了日を通知をすることで管理をしています。また、crontabファイル内にジョブを設定をして、決まった時刻に配信ができる様に制御をしています。
# Demo
<img src="/images/k-step2.png" width="500px" height="300px">
<img src="/images/k-step3.png" width="500px" height="300px">
<img src="/images/k-step4.png" width="500px" height="300px">
<img src="/images/k-step5.png" width="500px" height="300px">

# Install
  下記のコマンドを実行してください。<br><br>
  ```
    $ git clone https://github.com/kazutotakeuchi-32/k-step.git
  ```
# Requirements
  - Python 3.8.3
  - conda 4.8.3
  - requests 2.24.0
  - requests-oauthlib 1.3.0
  - TwitterAPI 2.6.2.1
  - LINENotifyAPI
