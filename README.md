# Arknights-Cheater 
### 本软件仅供个人学习研究使用，请在下载24小时之后删除。
### 禁止对其宣传，宣传后对鹰角网络造成的经济损失后果自负。
封号我不管，~~我已经爽够了（划掉~~

明日方舟破解 / Arknights-Cheater 

利用 mitmproxy 来实现对明日方舟数据的中间人攻击，从而修改部分我们希望修改的数据。
通过设置PAC代理的方式可以支持任意设备、模拟器使用，支持多个用户同时使用。

## 主要功能

- 全干员满级、满潜、满精、满信赖。
- 自定义干员。
- 支持龙门。
- 支持代理指挥。
- 防沉迷破解。

## 使用说明

1. 下载<br/>[mitmdump.exe](https://mitmproxy.org/downloads/)<br/>[character_table.json](https://github.com/Kengxxiao/ArknightsGameData/blob/master/zh_CN/gamedata/excel/character_table.json)<br/>[skin_table.json](https://github.com/Kengxxiao/ArknightsGameData/blob/master/zh_CN/gamedata/excel/skin_table.json)<br/>放入脚本同级目录。

2. 执行 ArknightsCheater.exe。

3. 按照 ArknightsCheater 配置用户数据。

4.  ArknightsCheater 启动按钮启动 mitmproxy

5. 信任Windows防火墙。

6. 按照 ArknightsCheater 在手机或模拟器中信任mitmproxy证书(进入网站 http://mitm.it/ 下载)。

7. 进入游戏 ~~享受快乐。~~

#### 注：
- BUG:当干员装载ID和CharId不同时或干员装载ID大于原来本有的干员数时，会同步失败。<br/>如果注重这个推荐使用[老版本](https://github.com/Tao0Lu/Arknights-Cheater-Bat "老版本")
- 有时候 mitmdump.exe 会卡住，这时候需要重新启动。
- 此方法在安卓7.0以上中受限制(iOS安装描述文件后全版本都可以)，如果你是安卓7.0以上，请参考:<br/>解决方法1：~~使用安卓7.0以下版本的手机。~~<br/>解决方式2：Root手机，安装 Xposed + JustTrustMe。<br/>解决方式3：不Root，使用 VirtualXposed、太极等 + JustTrustMe。或将游戏安装到安卓内模拟器 如:VMOS等。

#### Debug模式：
此模式下

>用户等级，理智上限 
>干员精英等级，等级，专精等级，潜能等级

不受限制(最大为PYQT最大值999999999)