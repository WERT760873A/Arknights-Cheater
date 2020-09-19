print('ArknightsCheater:启动mitmproxy成功，请按帮助内操作继续。')
import mitmproxy.http
from mitmproxy import ctx, http
import copy,time,json

html_notice='<html><head><meta name="viewport"content="width=device-width, initial-scale=1, minimum-scale=1"/><title>公告</title><link rel="stylesheet"href="https://ak-fs.hypergryph.com/announce/assets/css/preannouncement.css"></head><body><div class="container"><h2 class="head-title">破解用户须知</h2><div class="content">提供一种绕过服务器的破解方法，通过中间人攻击修改服务器递交的数据，<s>从而做到自欺欺人。</s><br>本软件仅供个人学习研究使用，请在下载24小时之后删除。<br>禁止对其宣传，宣传后对鹰角网络造成的经济损失后果自负。<br>一个单机游戏你也作弊，你在现实得多自卑啊!<br><img src="https://i.loli.net/2020/08/17/flOCIAto1VEgHpT.png"></div></div></body></html>'
Debug=True
entryGame=True
isInit=False
isFCM=True
userData=json.loads(open('.\data.acdata', 'r', encoding='UTF-8').read())
isInit=userData['init']
isFCM=userData['fcm']
userIsMinors=False
Servers = ["ak-gs.hypergryph.com", "ak-as.hypergryph.com","gs.arknights.jp", "ak-gs-localhost.hypergryph.com",
           "ak-as-localhost.hypergryph.com"]

class Cheat:
    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host not in Servers and Debug is False:
            flow.response = http.HTTPResponse.make(404)
        if flow.request.host == "ak-gs-localhost.hypergryph.com":
            flow.request.host = "ak-gs.hypergryph.com"
            flow.request.port = 8443
        elif flow.request.host == "ak-as-localhost.hypergryph.com":
            flow.request.host = "ak-as.hypergryph.com"
            flow.request.port = 9443

    def request(self, flow):
        if not isInit:
            if flow.request.host in Servers and flow.request.path.startswith("/quest/battleStart"):
                data = flow.request.get_content()
                print('ArknightsCheater:战斗开始 >>>')
                j = json.loads(data)
                print(j['squad']['slots'])
                print(userData['squads'][str(j['squad']['squadId'])]['slots'])
                if not j['squad']==None:
                    j['squad']['slots']=userData['squads'][str(j['squad']['squadId'])]['slots']
                flow.request.set_content(json.dumps(j).encode())
            elif flow.request.host in Servers and flow.request.path.startswith("/campaign/battleStart"):
                data = flow.request.get_content()
                print('ArknightsCheater:龙门战斗开始 >>>')
                j = json.loads(data)
                if not j['squad']==None:
                    j['squad']['slots']=userData['squads'][str(j['squad']['squadId'])]['slots']
                flow.request.set_content(json.dumps(j).encode())
            elif flow.request.host in Servers and flow.request.path.startswith("/quest/squadFormation"):
                data = flow.request.get_content()
                j = json.loads(data)
                j['slots'] = userData['squads'][str(j['squadId'])]['slots']
                flow.request.set_content(json.dumps(j).encode())
            elif flow.request.host not in Servers and Debug is False:
                flow.response = http.HTTPResponse.make(404)

    def response(self, flow: mitmproxy.http.HTTPFlow):
        global entryGame,userIsMinors
        if isInit:
            if flow.request.host in Servers and flow.request.path.startswith("/account/syncData"):
                text = flow.response.get_text()
                j = json.loads(text)
                print(j['user']['troop']['chars'])
                item=[{
                    'gold': j['user']['status']['gold'],
                    'diamondShard': j['user']['status']['diamondShard'],
                    'androidDiamond': j['user']['status']['androidDiamond'],
                    'iosDiamond': j['user']['status']['iosDiamond'],
                    'practiceTicket': j['user']['status']['practiceTicket'],
                    'lggShard': j['user']['status']['lggShard'],
                    'hggShard': j['user']['status']['hggShard'],
                    'gachaTicket': j['user']['status']['gachaTicket'],
                    'tenGachaTicket': j['user']['status']['tenGachaTicket']
                }]
                data=[{
                    'userIsMinors':str(userIsMinors).lower(),
                    'uid': j['user']['status']['uid'],
                    'nickName': j['user']['status']['nickName'],
                    'nickNumber': j['user']['status']['nickNumber'],
                    'level': j['user']['status']['level'],
                    'ap': j['user']['status']['ap'],
                    'maxAp': j['user']['status']['maxAp'],
                    'resume': 'Ta什么都没有留下',
                    'secretary':j['user']['status']['secretary'],
                    'secretarySkinId':j['user']['status']['secretarySkinId'],
                    'item':item[0],
                    'chars':j['user']['troop']['chars'],
                    'squads':j['user']['troop']['squads']
                }]
                f=open('.\datafromgame.acdata', 'w', encoding='UTF-8')
                f.write(str(data).replace('{\'"','{"').replace('}\'}','}}').replace('\'','"').replace('""','').replace('None','null')[1:-1])
                f.close
                print('initFinished')
        if flow.request.url.startswith("https://ak-fs.hypergryph.com/announce/Android/preannouncement.meta.json") or flow.request.url.startswith("https://ak-fs.hypergryph.com/announce/IOS/preannouncement.meta.json"):
            entryGame=True
        if flow.request.host in Servers and flow.request.path.startswith("/online/v1/ping") and isFCM:
            j=json.loads(flow.response.get_text())
            if 'timeLeft' in j:
                if not j['timeLeft']==-1:
                    userIsMinors=True
            if entryGame:
                flow.response.set_text('{"result":0,"message":"OK","interval":5400,"timeLeft":-1,"alertTime":600}')
                entryGame=False
            else:
                flow.response = http.HTTPResponse.make(404)
            if j['message'][:6]=='您已达到本日':
                userIsMinors=True
                print('ArknightsCheater-防沉迷破解: 您已达到本日在线时长上限或不在可游戏时间范围内，破解后仍可以继续游戏，但请合理安排游戏时间。')
            else:
                s = j['timeLeft']
                h = int(s/3600)
                m = int((s-h*3600)/60)
                ss = int(s-h*3600-m*60)
                print('ArknightsCheater-防沉迷破解: 游戏剩余时间 '+str(h)+'小时'+str(m)+'分钟' + str(ss)+'秒 修改为 不限制，但请合理安排游戏时间。')
        if flow.request.url.startswith("https://ak-fs.hypergryph.com/announce/Android/preannouncement/231.html") or flow.request.url.startswith("https://ak-fs.hypergryph.com/announce/IOS/preannouncement/231.html") and not isInit:
            flow.response.set_text(html_notice)
        if flow.request.host in Servers and flow.request.path.startswith("/account/syncStatus") and not isInit:
            j=json.loads(flow.response.get_text())
            j['playerDataDelta']['modified']['status']['resume']=userData['resume']
            flow.response.set_text(json.dumps(j))
        if flow.request.host in Servers and flow.request.path.startswith("/account/syncData") and not isInit:
            text = flow.response.get_text()
            j = json.loads(text)
            print('ArknightsCheater:' + j['user']['status']['nickName'] + '#' + flow.request.headers['uid'] + ' 初始化...')   
            j['user']['status']['uid']=str(userData['uid'])
            j['user']['status']['nickName']=userData['nickName']
            j['user']['status']['nickNumber']=str(userData['nickNumber'])
            j['user']['status']['level']=userData['level']
            j['user']['status']['ap']=userData['ap']
            j['user']['status']['maxAp']=userData['maxAp']
            j['user']['status']['secretary']=userData['secretary']
            j['user']['status']['secretarySkinId']=userData['secretarySkinId']
            j['user']['status']['gold']=userData['item']['gold']
            j['user']['status']['diamondShard']=userData['item']['diamondShard']
            j['user']['status']['androidDiamond']=userData['item']['androidDiamond']
            j['user']['status']['iosDiamond']=userData['item']['iosDiamond']
            j['user']['status']['practiceTicket']=userData['item']['practiceTicket']
            j['user']['status']['lggShard']=userData['item']['lggShard']
            j['user']['status']['hggShard']=userData['item']['hggShard']
            j['user']['status']['gachaTicket']=userData['item']['gachaTicket']
            j['user']['status']['tenGachaTicket']=userData['item']['tenGachaTicket']
            j['user']['troop']['chars']=userData['chars']
            print('ArknightsCheater:载入成功，共%s个干员' % str(len(j['user']['troop']['chars'])))
            print('')
            flow.response.set_text(json.dumps(j))
        if flow.request.host in Servers and flow.request.path.startswith("/quest/squadFormation") and not isInit:
            text = flow.response.get_text()
            print('ArknightsCheater:设置编队 >>>')
            j = json.loads(text)
            squadId=str(j['playerDataDelta']['modified']['troop']['squads'])[2:3]
            j['playerDataDelta']['modified']['troop']['squads'][squadId]['slots']= userData['squads'][squadId]['slots']
            flow.response.set_text(json.dumps(j))
        if flow.request.host not in Servers and Debug is False:
            flow.response = http.HTTPResponse.make(404)
            
addons = [
    Cheat()
]
