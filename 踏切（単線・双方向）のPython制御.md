# 第1段階　まず点滅させるだけ

テストです。

## レイアウトスクリプト
```py
def vrmevent(obj,ev,param):　　　　　　　　defineの意味
    toruo.activate(obj, ev,param)
    if ev == 'init':
        obj.SetEventKeyDown('A')
        obj.SetEventKeyDown('Z')
        toruo.jump_toruo(0)　　　#←注意 0番とは位置0番という意味。保存位置を先にきっちりしておくこと。
        obj.SetEventTimer(0.5)　　　　　間隔の秒数をぶっこむ
        dummy = 1
    elif ev == 'broadcast':
        dummy = 1
    elif ev == 'timer':　　　　　　　タイマーイベントを指す。　
        global sw　　　　　　　　　　グローバル変数としてつかうために定義　　　　
        tr1 = obj.GetTrain(4)       編成を取得する
        tr2 = obj.GetTrain(110)
        ca1 = tr1.GetCar(0)　　　　　車両を編成から取得する
        ca2 = tr2.GetCar(0)
        if sw == 0:
          ca1.SetOptionDisp(0, True)
          ca1.SetOptionDisp(1, False)
          ca2.SetOptionDisp(0, True)
          ca2.SetOptionDisp(1, False)
          sw = 1
        else:
          ca1.SetOptionDisp(1, True)
          ca1.SetOptionDisp(0, False)
          ca2.SetOptionDisp(1, True)
          ca2.SetOptionDisp(0, False)
          sw = 0
```
<br/>
<br/>
<br/>

# 第2段階　自動センサー踏んだら動きなさいバージョン

## レイアウトのスクリプト
```py
#LAYOUT
import vrmapi
import toruo

sw1=0
sw2=0

def vrmevent(obj,ev,param):
    toruo.activate(obj, ev,param)
    if ev == 'init':
        obj.SetEventKeyDown('A')
        obj.SetEventKeyDown('Z')
        toruo.jump_toruo(0)
        obj.SetEventTimer(0.5)
        dummy = 1
    elif ev == 'broadcast':
        dummy = 1
    elif ev == 'timer':
        global sw1
        global sw2
        tr1 = obj.GetTrain(4)
        tr2 = obj.GetTrain(110)
        ca1 = tr1.GetCar(0)
        ca2 = tr2.GetCar(0)
        if sw2 == 1:
         if sw1 == 0:
           ca1.SetOptionDisp(0, True)
           ca1.SetOptionDisp(1, False)
           ca2.SetOptionDisp(0, True)
           ca2.SetOptionDisp(1, False)
           sw1 = 1
         else:
           ca1.SetOptionDisp(1, True)
           ca1.SetOptionDisp(0, False)
           ca2.SetOptionDisp(1, True)
           ca2.SetOptionDisp(0, False)
           sw1 = 0
        else:
           ca1.SetOptionDisp(0, False)
           ca1.SetOptionDisp(1, False)
           ca2.SetOptionDisp(0, False)
           ca2.SetOptionDisp(1, False)
        dummy = 1
    elif ev == 'time':
        dummy = 1
    elif ev == 'after':
        dummy = 1
    elif ev == 'frame':
        dummy = 1
    elif ev == 'keydown':
        if param['keycode'] == 'A':
            toruo.setshakemode(True)
        if param['keycode'] == 'Z':
            toruo.setshakemode(False)
        dummy = 1
```

## ●閉じる方の自動センサー
```py
import vrmapi
def vrmevent_8(obj,ev,param):
    if ev == 'init':
        dummy = 1
    elif ev == 'broadcast':
        dummy = 1
    elif ev == 'timer':
        dummy = 1
    elif ev == 'time':
        dummy = 1
    elif ev == 'after':
        dummy = 1
    elif ev == 'frame':
        dummy = 1
    elif ev == 'catch':
        global sw2
        sw2=1
        dummy = 1
```

## ●通過後開く方の自動センサー
```py

import vrmapi
def vrmevent_19(obj,ev,param):
    if ev == 'init':
        dummy = 1
    elif ev == 'broadcast':
        dummy = 1
    elif ev == 'timer':
        dummy = 1
    elif ev == 'time':
        dummy = 1
    elif ev == 'after':
        dummy = 1
    elif ev == 'frame':
        dummy = 1
    elif ev == 'catch':
        global sw2
        sw2=0
        dummy = 1
```

# 第3段階　単線・双方向で踏切制御

## レイアウトスクリプト
変更なし

## 踏切閉じる側の両方のセンサー
```py
import vrmapi
def vrmevent_8(obj,ev,param):
    if ev == 'init':
        dummy = 1
    elif ev == 'broadcast':
        dummy = 1
    elif ev == 'timer':
        dummy = 1
    elif ev == 'time':
        dummy = 1
    elif ev == 'after':
        dummy = 1
    elif ev == 'frame':
        dummy = 1
    elif ev == 'catch':
        if obj.GetForward() == 1: #←ここが追加した部分　もしセンサーが順方向で検出したらという意味
         global sw2
         sw2=1
         dummy = 1
```
## 踏切開く側の両方のセンサー
```py
import vrmapi
def vrmevent_19(obj,ev,param):
    if ev == 'init':
        dummy = 1
    elif ev == 'broadcast':
        dummy = 1
    elif ev == 'timer':
        dummy = 1
    elif ev == 'time':
        dummy = 1
    elif ev == 'after':
        dummy = 1
    elif ev == 'frame':
        dummy = 1
    elif ev == 'catch':
        if obj.GetForward() == 1: #←ここが追加した部分　もしセンサーが順方向で検出したらという意味
         global sw2
         sw2=0
         dummy = 1
```
