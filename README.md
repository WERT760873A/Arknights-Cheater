# Arknights-Cheater 
### 本软件仅供个人学习研究使用，请在下载24小时之后删除。
### 禁止对其宣传，宣传后对鹰角网络造成的经济损失后果自负。
封号我不管，~~我已经爽够了（划掉~~

明日方舟破解 / Arknights-Cheater 

利用 mitmproxy 来实现对明日方舟数据的中间人攻击，从而修改部分我们希望修改的数据。
通过设置PAC代理的方式可以支持任意设备、模拟器使用，支持多个用户同时使用。

代码和想法基于[GhostStar/Arknights-Armada](https://github.com/GhostStar/Arknights-Armada "GhostStar/Arknights-Armada")

## 主要功能

- 全干员满级、满潜、满精、满信赖。
- 自定义干员。
- 支持龙门。
- 支持代理指挥。
- 防沉迷破解。

## 配置mitmproxy
此破解方法在安卓7.0以上中受限制(iOS安装描述文件后全版本都可以)，如果你是安卓7.0以上，请参考:
- 解决方法1：~~使用安卓7.0以下版本的手机。~~
- 解决方式2：Root手机，安装 Xposed + JustTrustMe。
- 解决方式3：不Root，使用 VirtualXposed、太极等 + JustTrustMe。或使用安卓内模拟器 如:VMOS等。

请在手机或模拟器中完成以下配置：
1. 确保手机或模拟器和电脑在同一局域网下。

2. 进入手机或模拟器WLAN(Wi-Fi)设置配置手机代理。<br>安卓：修改网络--高级选项--代理--手动<br>iOS：HTTP代理--配置代理--手动<br>将服务器和端口设置为mitmproxy所监听的端口和主机ip。<br>保存/储存

 _例如此时我的电脑和手机处于同一局域网下，电脑的ip为192.168.1.48，端口在12450上开放。_![](https://i0.hdslb.com/bfs/article/318e9a0abec227de118d118144271d7611032704.jpg)
 _安卓操作_![](https://i0.hdslb.com/bfs/article/ec7e3ed3fb3b1bb3df5cf24a33922cd39e6c04a7.jpg)
 _iOS操作_

3. 进入网站 http://mitm.it 下载证书(iOS为描述文件)并安装。<br>iOS多一步：设置--通用--关于本机--证书信任设置--mitmproxy--打开<br>_(此步必须在上一步完成后且电脑端开启着mitmproxy或运行着脚本时候进行)_
![](https://i0.hdslb.com/bfs/article/3c6435bb30b234adfd323673e590dd8c10909bc0.jpg)
_安卓操作_
![](https://i0.hdslb.com/bfs/article/e478d1bc37a358899d670a6bb2f9744dcff51abe.jpg)
_iOS操作_
## 使用说明

1. 下载<br/>[mitmdump.exe](https://mitmproxy.org/downloads/)<br/>[character_table.json](https://github.com/Kengxxiao/ArknightsGameData/blob/master/zh_CN/gamedata/excel/character_table.json)<br/>[skin_table.json](https://github.com/Kengxxiao/ArknightsGameData/blob/master/zh_CN/gamedata/excel/skin_table.json)<br/>放入脚本同级目录。

2. 执行 ArknightsCheater.exe。

3. 按照 ArknightsCheater 配置用户数据。

4.  ArknightsCheater 启动按钮启动 mitmproxy。

5. 信任Windows防火墙。

6. 按照 ArknightsCheater 在手机或模拟器中信任mitmproxy证书(进入网站 http://mitm.it/ 下载)。

7. 进入游戏 ~~享受快乐。~~

#### 注：
- 编队中不能出现相同装载ID的干员,且装载ID不能大于所拥有的干员数；修改编队后，需要手动在游戏主界面编队选中编队中某一干员，随便修改其技能并且返回到主界面来达到修改效果。
- 有时候 mitmdump.exe 会卡住，这时候需要重新启动。

#### Debug模式：
此模式下

>用户等级，理智上限<br/>干员精英等级，等级，专精等级，潜能等级

不受限制(最大为PYQT最大值999999999)

![Arknights-Cheater](https://i.loli.net/2020/08/20/PFgQDLvE64yzBnM.png)
_图为1.0版本_
