print("ArknightsCheater:启动mitmproxy成功，请按帮助内操作继续。")
import mitmproxy.http
from mitmproxy import ctx, http
import copy,time,json

html_notice='<html><head><meta name="viewport"content="width=device-width, initial-scale=1, minimum-scale=1"/><title>公告</title><link rel="stylesheet"href="https://ak-fs.hypergryph.com/announce/assets/css/preannouncement.css"></head><body><div class="container"><h2 class="head-title">破解用户须知</h2><div class="content">提供一种绕过服务器的破解方法，通过中间人攻击修改服务器递交的数据，<s>从而做到自欺欺人。</s><br>本软件仅供个人学习研究使用，请在下载24小时之后删除。<br>禁止对其宣传，宣传后对鹰角网络造成的经济损失后果自负。<br>一个单机游戏你也作弊，你在现实得多自卑啊!<br><img src="https://i.loli.net/2020/08/17/flOCIAto1VEgHpT.png"></div></div></body></html>'
Debug = True
entryGame=True
Servers = ["ak-gs.hypergryph.com", "gs.arknights.jp", "ak-gs-localhost.hypergryph.com",
           "ak-as-localhost.hypergryph.com"]

class Cheat:
    def __init__(self):
        self.squadFormation = {}
        self.squadFormationID = 0
        self.userData=json.loads(open('.\data.json', 'r', encoding='UTF-8').read())

    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host not in Servers and False is Debug:
            flow.response = http.HTTPResponse.make(404)
        if flow.request.host == "ak-gs-localhost.hypergryph.com":
            flow.request.host = "ak-gs.hypergryph.com"
            flow.request.port = 8443
        elif flow.request.host == "ak-as-localhost.hypergryph.com":
            flow.request.host = "ak-as.hypergryph.com"
            flow.request.port = 9443

    def request(self, flow):
        if flow.request.host in Servers and flow.request.path.startswith("/quest/battleStart"):
            data = flow.request.get_content()
            print('ArknightsCheater:战斗开始 >>>')
            j = json.loads(data)
            if not j['squad']==None:
                for i, d in enumerate(j['squad']['slots']):
                    if d is not None:
                        d['skillIndex'] = self.userData['chars'][str(d['charInstId'])]['defaultSkillIndex']
            flow.request.set_content(json.dumps(j).encode())
        elif flow.request.host in Servers and flow.request.path.startswith("/campaign/battleStart"):
            data = flow.request.get_content()
            print('ArknightsCheater:龙门战斗开始 >>>')
            j = json.loads(data)
            if not j['squad']==None:
                for i, d in enumerate(j['squad']['slots']):
                    if d is not None:
                        d['skillIndex'] = self.userData['chars'][str(d['charInstId'])]['defaultSkillIndex']
            flow.request.set_content(json.dumps(j).encode())
        elif flow.request.host in Servers and flow.request.path.startswith("/quest/squadFormation"):
            data = flow.request.get_content()
            self.squadFormation = flow.request.headers['uid']
            j = json.loads(data)
            self.squadFormation = {copy.deepcopy(j['squadId']): {'slots': copy.deepcopy(j['slots'])}}
            for i, d in enumerate(j['slots']):
                if j['slots'][i] is not None:
                    j['slots'][i]['skillIndex'] = self.userData['chars'][str(j['slots'][i]['charInstId'])]['defaultSkillIndex']
            flow.request.set_content(json.dumps(j).encode())
        elif flow.request.host not in Servers and Debug is False:
            flow.response = http.HTTPResponse.make(404)

    def response(self, flow: mitmproxy.http.HTTPFlow):
        global entryGame
        if flow.request.url.startswith("https://ak-fs.hypergryph.com/announce/Android/preannouncement.meta.json") or flow.request.url.startswith("https://ak-fs.hypergryph.com/announce/IOS/preannouncement.meta.json"):
            entryGame=True
        if flow.request.url.startswith("https://ak-as.hypergryph.com:9443/online/v1/ping"):
            j=json.loads(flow.response.get_text())
            if entryGame:
                flow.response.set_text('{"result":0,"message":"OK","interval":5400,"timeLeft":-1,"alertTime":600}')
                entryGame=False
            else:
                flow.response = http.HTTPResponse.make(404)
            if j['message'][:6]=='您已达到本日':
                print('ArknightsCheater-防沉迷破解: 您已达到本日在线时长上限或不在可游戏时间范围内，破解后仍可以继续游戏，但请合理安排游戏时间。')
            else:
                s = j['timeLeft']
                h = int(s/3600)
                m = int((s-h*3600)/60)
                ss = int(s-h*3600-m*60)
                print('ArknightsCheater-防沉迷破解: 游戏剩余时间 '+str(h)+'小时'+str(m)+'分钟' + str(ss)+'秒 修改为 不限制，但请合理安排游戏时间。')
        if flow.request.url.startswith("https://ak-fs.hypergryph.com/announce/Android/preannouncement/231.html") or flow.request.url.startswith("https://ak-fs.hypergryph.com/announce/IOS/preannouncement/231.html"):
            flow.response.set_text(html_notice)
        if flow.request.url.startswith("https://ak-gs.hypergryph.com:8443/account/syncStatus"):
            j=json.loads(flow.response.get_text())
            j['playerDataDelta']['modified']['status']['resume']=self.userData['resume']
            flow.response.set_text(json.dumps(j))
        if flow.request.host in Servers and flow.request.path.startswith("/account/syncData"):
            text = flow.response.get_text()
            j = json.loads(text)
            print('ArknightsCheater:' + j['user']['status']['nickName'] + '#' + flow.request.headers['uid'] + ' 初始化...')   
            j['user']['status']['uid']=str(self.userData['uid'])
            j['user']['status']['nickName']=self.userData['nickName']
            j['user']['status']['nickNumber']=str(self.userData['nickNumber'])
            j['user']['status']['level']=self.userData['level']
            j['user']['status']['ap']=self.userData['ap']
            j['user']['status']['maxAp']=self.userData['maxAp']
            j['user']['status']['resume']=self.userData['resume']
            j['user']['status']['secretary']=self.userData['secretary']
            j['user']['status']['secretarySkinId']=self.userData['secretarySkinId']
            j['user']['status']['gold']=self.userData['item']['gold']
            j['user']['status']['diamondShard']=self.userData['item']['diamondShard']
            j['user']['status']['androidDiamond']=self.userData['item']['androidDiamond']
            j['user']['status']['iosDiamond']=self.userData['item']['iosDiamond']
            j['user']['status']['practiceTicket']=self.userData['item']['practiceTicket']
            j['user']['status']['lggShard']=self.userData['item']['lggShard']
            j['user']['status']['hggShard']=self.userData['item']['hggShard']
            j['user']['status']['gachaTicket']=self.userData['item']['gachaTicket']
            j['user']['status']['tenGachaTicket']=self.userData['item']['tenGachaTicket']
            j['user']['troop']['chars']=self.userData['chars']
            print('ArknightsCheater:载入成功，共%s个干员' % str(len(j['user']['troop']['chars'])))
            print('')
            flow.response.set_text(json.dumps(j))
        if flow.request.host in Servers and flow.request.path.startswith("/quest/squadFormation"):
            text = flow.response.get_text()
            print('ArknightsCheater:设置编队 >>>')
            j = json.loads(text)
            squadId=str(j['playerDataDelta']['modified']['troop']['squads'])[2:3]
            j['playerDataDelta']['modified']['troop']['squads'][squadId]= self.squadFormation[squadId]
            flow.response.set_text(json.dumps(j))
        if flow.request.host not in Servers and Debug is False:
            flow.response = http.HTTPResponse.make(404)
            
addons = [
    Cheat()
]
