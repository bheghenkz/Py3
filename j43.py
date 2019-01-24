# -*- coding: utf-8 -*-

from linepy import *
from datetime import datetime, timedelta
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib, parse, pafy, youtube_dl
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()

line = LINE('EBjL7rXlYszjTwlSHBw6.FtB1G3Yw/H75w5VCRpKRzG.Si+7yzQfWkLM5CVu9tX3CMm4rNJZSHDs2GWgFcxJQIE=')
#======================JOFEN=#
kiker1 = LINE('EBoB5CAFbqdJdOZYl788.7UX+KrSxmk03gbovvvoE2a.kXMR8rgfmwZL0GHB2MyyZ9jJXydRxu8SYPMmsftd9tk=')
#======================KIKER1=#
kiker2 = LINE('EBlo9NVRaeejwzzyAjx1.p/xpb9qUstdRrEIx+9+Dmq.E6nnAGJ56b8BKdxkY2OyO1AKeipnGf529M3waFzWld4=')
#======================KIKER2=#
kiker3 = LINE('EBogAB8axupJyN8ZFeZ0.X866NFvDoKXu/7SYGPXF0a.BCXb2W5rnlekGPmEO0GE5mzw5EBs1WQip4jfAyfZghU=')
#======================KIKER3=#
kiker4 = LINE('EBJqfXdJzlk8UEa3cPvc.dZh3s/8BdZ61dUkLUv5r7a.5xBhcB1PZLdJ4KjBUXdKLICvTxCQeKS11o875wTt8lk=')
#======================KIKER4=#
kiker5 = LINE('EBjL7rXlYszjTwlSHBw6.FtB1G3Yw/H75w5VCRpKRzG.Si+7yzQfWkLM5CVu9tX3CMm4rNJZSHDs2GWgFcxJQIE=')
kiker5.log("Timeline Token : " + str(kiker5.tl.channelAccessToken))
#
readOpen = codecs.open("read.json","r","utf-8")
#adminOpen = codecs.open("admin.json","r","utf-8")
msg_dict = {}
msg_dict1 = {}

lineMID = line.profile.mid
kiker1MID = kiker1.profile.mid
kiker2MID = kiker2.profile.mid
kiker3MID = kiker3.profile.mid
kiker4MID = kiker4.profile.mid

lineProfile = line.getProfile()
kiker1Profile = kiker1.getProfile()
kiker2Profile = kiker2.getProfile()
kiker3Profile = kiker3.getProfile()
kiker4Profile = kiker4.getProfile()

lineSettings = line.getSettings()
kiker1Settings = kiker1.getSettings()
kiker2Settings = kiker2.getSettings()
kiker3Settings = kiker3.getSettings()
kiker4Settings = kiker4.getSettings()

oepoll = OEPoll(line)
oepoll1 = OEPoll(kiker1)
oepoll2 = OEPoll(kiker2)
oepoll3 = OEPoll(kiker3)
oepoll4 = OEPoll(kiker4)
read = json.load(readOpen)
#======================================================#
assist = [line,kiker1,kiker2,kiker3,kiker4]
admin = ["u7d36f5837c96fa1ef95b9bdcacf92b66"]
admin = [line,kiker1,kiker2,kiker3,kiker4]
Bots = [line,kiker1,kiker2,kiker3,kiker4]
mid = line.getProfile().mid
Amid = kiker1.getProfile().mid
Bmid = kiker2.getProfile().mid
Cmid = kiker3.getProfile().mid
Dmid = kiker4.getProfile().mid
tokenz= {}
admin = []
list = []
wordban = []
ls = []
#==============================================================================#
settings = {
    "AddstickerTag": {
        "sid": "18687390",
        "spkg": "1520987",
        "status": False
            },
    "stk":{},
    "autoAdd": False,
    "autoJoin": False,
    "autoJoinTicket": True,
    "autoLeave": False,
#    "autoResponMessage": "Woi @!, gak usah tag tag -_-",
    "autoResponMessage": "Woi gak usah tag tag -_-",
    "likeOn": True,
    "vezacvp":"",
    "JOFEN":"",
    "Timeline": False,
   'autoCancel': False,
   'contact': False,
    "checkContact": False,
    "ghost": False,
    "talkban": False,
    "talkban":{},
    "talkblacklist":{},
    "autoRead": False,
    "Comment": "αυтσℓιкє\njØƒ€и\n🎬- ᴊᴏꜰᴇɴ ʙᴏᴛꜱ\n⪓Sϻilᴇ𝕓☢ts⪔ ",
    "commentOn": False,
    "commentBlack":{},
    "wblacklist": False,
    "wblack": False,
    "dblack": False,
   'leaveRoom':False,
    "blacklist":{}, 
    "cancelinvite": False,
    "inviteprotect": False,
    "linkprotect": False,
    "protect": False,
    "projoin": False,
    "projs": True,
    "mid":{},
    "Sider":{},
    "pname":{},
    "pro_name":{},  
    "datectMention": False,
    "datectMention2": False,
    "dblacklist": False,
   'changePicture':{},
   'invite':{},
    "displayName":{},
    "changeGroupPicture":[],
    "lang":"JP",
    "unsendMessage": False,
    "checkSticker": False,
    "Sambutan": False,
    "Jembutan": False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

settings1 = {
    "changePictureProfile": {
        "kiker1": {},
        "kiker2": {},
        "kiker3": {},
        "kiker4": {},
    }
}


read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

cctv = {
    "cyduk":{},
    "point":{},
    "MENTION":{},
    "sidermem":{}
}

bc = {
    "txt": {},
    "mid": {},
    "img": False
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

myProfile["displayName"] = lineProfile.displayName
myProfile["displayName"] = kiker1Profile.displayName
myProfile["displayName"] = kiker2Profile.displayName
myProfile["displayName"] = kiker3Profile.displayName

myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["statusMessage"] = kiker1Profile.statusMessage
myProfile["statusMessage"] = kiker2Profile.statusMessage
myProfile["statusMessage"] = kiker3Profile.statusMessage

myProfile["pictureStatus"] = lineProfile.pictureStatus
myProfile["pictureStatus"] = kiker1Profile.pictureStatus
myProfile["pictureStatus"] = kiker2Profile.pictureStatus
myProfile["pictureStatus"] = kiker3Profile.pictureStatus
#==============================================================================#

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    line.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                line.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMentionV2(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMessage(to, Message, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes._from = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
#Footer
def sendMessageWithFooter(to, text):
	line.reissueUserTicket()
	wildan = line.getProfile()
	ticket = "http://line.me/ti/p/"+line.getUserTicket().id
	pict = "http://dl.profile.line-cdn.net/"+wildan.pictureStatus
	name = wildan.displayName
	wildanGanteng = {"AGENT_ICON": pict,
	    "AGENT_NAME": name,
	    "AGENT_LINK": ticket
	}
	line.sendMessage(to, text, contentMetadata=wildanGanteng)

def sendMessageWithFooter1(to, text):
	kiker1.reissueUserTicket()
	wildan = kiker1.getProfile()
	ticket = "http://line.me/ti/p/"+kiker1.getUserTicket().id
	pict = "http://dl.profile.line-cdn.net/"+wildan.pictureStatus
	name = wildan.displayName
	wildanGanteng = {"AGENT_ICON": pict,
	    "AGENT_NAME": name,
	    "AGENT_LINK": ticket
	}
	kiker1.sendMessage(to, text, contentMetadata=wildanGanteng)

def sendMessageWithFooter2(to, text):
	kiker2.reissueUserTicket()
	wildan = kiker2.getProfile()
	ticket = "http://line.me/ti/p/"+kiker2.getUserTicket().id
	pict = "http://dl.profile.line-cdn.net/"+wildan.pictureStatus
	name = wildan.displayName
	wildanGanteng = {"AGENT_ICON": pict,
	    "AGENT_NAME": name,
	    "AGENT_LINK": ticket
	}
	kiker2.sendMessage(to, text, contentMetadata=wildanGanteng)

def sendMessageWithFooter3(to, text):
	kiker3.reissueUserTicket()
	wildan = kiker3.getProfile()
	ticket = "http://line.me/ti/p/"+kiker3.getUserTicket().id
	pict = "http://dl.profile.line-cdn.net/"+wildan.pictureStatus
	name = wildan.displayName
	wildanGanteng = {"AGENT_ICON": pict,
	    "AGENT_NAME": name,
	    "AGENT_LINK": ticket
	}
	kiker3.sendMessage(to, text, contentMetadata=wildanGanteng)

def sendMessageWithFooter4(to, text):
	kiker4.reissueUserTicket()
	wildan = kiker4.getProfile()
	ticket = "http://line.me/ti/p/"+kiker4.getUserTicket().id
	pict = "http://dl.profile.line-cdn.net/"+wildan.pictureStatus
	name = wildan.displayName
	wildanGanteng = {"AGENT_ICON": pict,
	    "AGENT_NAME": name,
	    "AGENT_LINK": ticket
	}
	kiker4.sendMessage(to, text, contentMetadata=wildanGanteng)

def sendMentionFooter(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Meka Finee "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    line.sendMessage(to, textx, {'AGENT_NAME':'  ✰feŇa✰  ', 'AGENT_LINK': 'line://ti/p/~{}'.format(line.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + line.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[Mention {} User]\n╠ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[ {} ]".format(str(line.getGroup(to).name))
                except:
                    pass
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def changeVideoAndPictureProfile(pict, vids):
        try:
            files = {'file': open(vids, 'rb')}
            obs_params = line.genOBSParams({'oid': lineMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4', 'name': 'Hello_World.mp4'})
            data = {'params': obs_params}
            r_vp = line.server.postContent('{}/talk/vp/upload.nhn'.format(str(line.server.LINE_OBS_DOMAIN)), data=data, files=files)
            if r_vp.status_code != 201:
                return "Failed update profile"
            line.updateProfilePicture(pict, 'vp')
            return "Success update profile"
        except Exception as e:
            raise Exception("Error change video and picture profile %s"%str(e))

def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def helpmessage():
    helpMessage = "╔══[нєℓρ мєѕѕαgє]" + "\n" + \
                  "╠ Help" + "\n" + \
                  "╠ Translate" + "\n" + \
                  "╠ TextToSpeech" + "\n" + \
                  "╠══[ Status Command ]" + "\n" + \
                  "╠ Restart" + "\n" + \
                  "╠ Runtime" + "\n" + \
                  "╠ Speed" + "\n" + \
                  "╠ Status" + "\n" + \
                  "╠ About" + "\n" + \
                  "╠══[ Settings Command ]" + "\n" + \
                  "╠ AutoAdd「On/Off」" + "\n" + \
                  "╠ AutoJoin「On/Off」" + "\n" + \
                  "╠ AutoLeave「On/Off」" + "\n" + \
                  "╠ AutoRead「On/Off」" + "\n" + \
                  "╠ CheckSticker「On/Off」" + "\n" + \
                  "╠ DetectMention「On/Off」" + "\n" + \
                  "╠══[ Self Command ]" + "\n" + \
                  "╠ Me" + "\n" + \
                  "╠ MyMid" + "\n" + \
                  "╠ MyName" + "\n" + \
                  "╠ MyBio" + "\n" + \
                  "╠ MyPicture" + "\n" + \
                  "╠ MyVideoProfile" + "\n" + \
                  "╠ MyCover" + "\n" + \
                  "╠ Mybot" + "\n" + \
                  "╠ Botpict" + "\n" + \
                  "╠ Blocklist" + "\n" + \
                  "╠ Pendinglist" + "\n" + \
                  "╠ Memberlist" + "\n" + \
                  "╠ Grouplist" + "\n" + \
                  "╠ Friendlist" + "\n" + \
                  "╠ StealContact「Mention」" + "\n" + \
                  "╠ StealMid「Mention」" + "\n" + \
                  "╠ StealName「Mention」" + "\n" + \
                  "╠ StealBio「Mention」" + "\n" + \
                  "╠ StealPicture「Mention」" + "\n" + \
                  "╠ StealVideoProfile「Mention」" + "\n" + \
                  "╠ StealCover「Mention」" + "\n" + \
                  "╠ CloneProfile「Mention」" + "\n" + \
                  "╠ RestoreProfile" + "\n" + \
                  "╠ Changename:" + "\n" + \
                  "╠ Changebio:" + "\n" + \
                  "╠══[ Group Command ]" + "\n" + \
                  "╠ adminadd" + "\n" + \
                  "╠ admin remove" + "\n" + \
                  "╠ adminlist" + "\n" + \
                  "╠ GroupCreator" + "\n" + \
                  "╠ GroupId" + "\n" + \
                  "╠ GroupName" + "\n" + \
                  "╠ GroupPicture" + "\n" + \
                  "╠ Gurl" + "\n" + \
                  "╠ GroupTicket「On/Off」" + "\n" + \
                  "╠ GroupList" + "\n" + \
                  "╠ GroupMemberList" + "\n" + \
                  "╠ GroupInfo" + "\n" + \
                  "╠ Kick" + "\n" + \
                  "╠ Hacked" + "\n" + \
                  "╠ Papay" + "\n" + \
                  "╠ @bye" + "\n" + \
                  "╠ Crash" + "\n" + \
                  "╠ Welcome on/off" + "\n" + \
                  "╠ Minggat on/off" + "\n" + \
                  "╠══[ Special Command ]" + "\n" + \
                  "╠ Broadcast" + "\n" + \
                  "╠ Mimic「On/Off」" + "\n" + \
                  "╠ MimicList" + "\n" + \
                  "╠ MimicAdd「Mention」" + "\n" + \
                  "╠ MimicDel「Mention」" + "\n" + \
                  "╠ Mentil" + "\n" + \
                  "╠ Invitegroupcall" + "\n" + \
                  "╠ Changepictureprofile" + "\n" + \
                  "╠ Lurking" + "\n" + \
                  "╠ Bintit on/off" + "\n" + \
                  "╠══[ Protect Group ]" + "\n" + \
                  "╠ Link on/off" + "\n" + \
                  "╠ Invite on/off" + "\n" + \
                  "╠ Protect on/off" + "\n" + \
                  "╠ Cancel on/off" + "\n" + \
                  "╠ Ghost on/off" + "\n" + \
                  "╠══[ Media Command ]" + "\n" + \
                  "╠ Kalender" + "\n" + \
                  "╠ Checklocation" + "\n" + \
                  "╠ CheckDate「Date」" + "\n" + \
                  "╠ InstagramInfo「UserName」" + "\n" + \
                  "╠ InstagramPost「UserName」" + "\n" + \
                  "╠ SearchYoutube「Search」" + "\n" + \
                  "╠ SearchMusic「Search」" + "\n" + \
                  "╠ SearchLyric「Search」" + "\n" + \
                  "╠ SearchImage「Search」" + "\n" + \
                  "╠ ScreenshootWebsite「LinkURL」" + "\n" + \
                  "╚══[     Ｈｅｌｌｏ Ｗｏｒｌｄ      ]"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   "╔══[ T E X T   T O   S P E E C H ]" + "\n" + \
                         "╠ af : Afrikaans" + "\n" + \
                         "╠ sq : Albanian" + "\n" + \
                         "╠ ar : Arabic" + "\n" + \
                         "╠ hy : Armenian" + "\n" + \
                         "╠ bn : Bengali" + "\n" + \
                         "╠ ca : Catalan" + "\n" + \
                         "╠ zh : Chinese" + "\n" + \
                         "╠ zh-cn : Chinese (Mandarin/China)" + "\n" + \
                         "╠ zh-tw : Chinese (Mandarin/Taiwan)" + "\n" + \
                         "╠ zh-yue : Chinese (Cantonese)" + "\n" + \
                         "╠ hr : Croatian" + "\n" + \
                         "╠ cs : Czech" + "\n" + \
                         "╠ da : Danish" + "\n" + \
                         "╠ nl : Dutch" + "\n" + \
                         "╠ en : English" + "\n" + \
                         "╠ en-au : English (Australia)" + "\n" + \
                         "╠ en-uk : English (United Kingdom)" + "\n" + \
                         "╠ en-us : English (United States)" + "\n" + \
                         "╠ eo : Esperanto" + "\n" + \
                         "╠ fi : Finnish" + "\n" + \
                         "╠ fr : French" + "\n" + \
                         "╠ de : German" + "\n" + \
                         "╠ el : Greek" + "\n" + \
                         "╠ hi : Hindi" + "\n" + \
                         "╠ hu : Hungarian" + "\n" + \
                         "╠ is : Icelandic" + "\n" + \
                         "╠ id : Indonesian" + "\n" + \
                         "╠ it : Italian" + "\n" + \
                         "╠ ja : Japanese" + "\n" + \
                         "╠ km : Khmer (Cambodian)" + "\n" + \
                         "╠ ko : Korean" + "\n" + \
                         "╠ la : Latin" + "\n" + \
                         "╠ lv : Latvian" + "\n" + \
                         "╠ mk : Macedonian" + "\n" + \
                         "╠ no : Norwegian" + "\n" + \
                         "╠ pl : Polish" + "\n" + \
                         "╠ pt : Portuguese" + "\n" + \
                         "╠ ro : Romanian" + "\n" + \
                         "╠ ru : Russian" + "\n" + \
                         "╠ sr : Serbian" + "\n" + \
                         "╠ si : Sinhala" + "\n" + \
                         "╠ sk : Slovak" + "\n" + \
                         "╠ es : Spanish" + "\n" + \
                         "╠ es-es : Spanish (Spain)" + "\n" + \
                         "╠ es-us : Spanish (United States)" + "\n" + \
                         "╠ sw : Swahili" + "\n" + \
                         "╠ sv : Swedish" + "\n" + \
                         "╠ ta : Tamil" + "\n" + \
                         "╠ th : Thai" + "\n" + \
                         "╠ tr : Turkish" + "\n" + \
                         "╠ uk : Ukrainian" + "\n" + \
                         "╠ vi : Vietnamese" + "\n" + \
                         "╠ cy : Welsh" + "\n" + \
                         "╚══[ Jangan Typo ]" + "\n" + "\n\n" + \
                          "Contoh : ˢᴬᵞ-ᴵᴰ ᶠᴱᴺᴰᵞ ᴶᴱᴸᴱˣ"
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate =    "╔══[ T R A N S L A T E ]" + "\n" + \
                       "╠ af : afrikaans" + "\n" + \
                       "╠ sq : albanian" + "\n" + \
                       "╠ am : amharic" + "\n" + \
                       "╠ ar : arabic" + "\n" + \
                       "╠ hy : armenian" + "\n" + \
                       "╠ az : azerbaijani" + "\n" + \
                       "╠ eu : basque" + "\n" + \
                       "╠ be : belarusian" + "\n" + \
                       "╠ bn : bengali" + "\n" + \
                       "╠ bs : bosnian" + "\n" + \
                       "╠ bg : bulgarian" + "\n" + \
                       "╠ ca : catalan" + "\n" + \
                       "╠ ceb : cebuano" + "\n" + \
                       "╠ ny : chichewa" + "\n" + \
                       "╠ zh-cn : chinese (simplified)" + "\n" + \
                       "╠ zh-tw : chinese (traditional)" + "\n" + \
                       "╠ co : corsican" + "\n" + \
                       "╠ hr : croatian" + "\n" + \
                       "╠ cs : czech" + "\n" + \
                       "╠ da : danish" + "\n" + \
                       "╠ nl : dutch" + "\n" + \
                       "╠ en : english" + "\n" + \
                       "╠ eo : esperanto" + "\n" + \
                       "╠ et : estonian" + "\n" + \
                       "╠ tl : filipino" + "\n" + \
                       "╠ fi : finnish" + "\n" + \
                       "╠ fr : french" + "\n" + \
                       "╠ fy : frisian" + "\n" + \
                       "╠ gl : galician" + "\n" + \
                       "╠ ka : georgian" + "\n" + \
                       "╠ de : german" + "\n" + \
                       "╠ el : greek" + "\n" + \
                       "╠ gu : gujarati" + "\n" + \
                       "╠ ht : haitian creole" + "\n" + \
                       "╠ ha : hausa" + "\n" + \
                       "╠ haw : hawaiian" + "\n" + \
                       "╠ iw : hebrew" + "\n" + \
                       "╠ hi : hindi" + "\n" + \
                       "╠ hmn : hmong" + "\n" + \
                       "╠ hu : hungarian" + "\n" + \
                       "╠ is : icelandic" + "\n" + \
                       "╠ ig : igbo" + "\n" + \
                       "╠ id : indonesian" + "\n" + \
                       "╠ ga : irish" + "\n" + \
                       "╠ it : italian" + "\n" + \
                       "╠ ja : japanese" + "\n" + \
                       "╠ jw : javanese" + "\n" + \
                       "╠ kn : kannada" + "\n" + \
                       "╠ kk : kazakh" + "\n" + \
                       "╠ km : khmer" + "\n" + \
                       "╠ ko : korean" + "\n" + \
                       "╠ ku : kurdish (kurmanji)" + "\n" + \
                       "╠ ky : kyrgyz" + "\n" + \
                       "╠ lo : lao" + "\n" + \
                       "╠ la : latin" + "\n" + \
                       "╠ lv : latvian" + "\n" + \
                       "╠ lt : lithuanian" + "\n" + \
                       "╠ lb : luxembourgish" + "\n" + \
                       "╠ mk : macedonian" + "\n" + \
                       "╠ mg : malagasy" + "\n" + \
                       "╠ ms : malay" + "\n" + \
                       "╠ ml : malayalam" + "\n" + \
                       "╠ mt : maltese" + "\n" + \
                       "╠ mi : maori" + "\n" + \
                       "╠ mr : marathi" + "\n" + \
                       "╠ mn : mongolian" + "\n" + \
                       "╠ my : myanmar (burmese)" + "\n" + \
                       "╠ ne : nepali" + "\n" + \
                       "╠ no : norwegian" + "\n" + \
                       "╠ ps : pashto" + "\n" + \
                       "╠ fa : persian" + "\n" + \
                       "╠ pl : polish" + "\n" + \
                       "╠ pt : portuguese" + "\n" + \
                       "╠ pa : punjabi" + "\n" + \
                       "╠ ro : romanian" + "\n" + \
                       "╠ ru : russian" + "\n" + \
                       "╠ sm : samoan" + "\n" + \
                       "╠ gd : scots gaelic" + "\n" + \
                       "╠ sr : serbian" + "\n" + \
                       "╠ st : sesotho" + "\n" + \
                       "╠ sn : shona" + "\n" + \
                       "╠ sd : sindhi" + "\n" + \
                       "╠ si : sinhala" + "\n" + \
                       "╠ sk : slovak" + "\n" + \
                       "╠ sl : slovenian" + "\n" + \
                       "╠ so : somali" + "\n" + \
                       "╠ es : spanish" + "\n" + \
                       "╠ su : sundanese" + "\n" + \
                       "╠ sw : swahili" + "\n" + \
                       "╠ sv : swedish" + "\n" + \
                       "╠ tg : tajik" + "\n" + \
                       "╠ ta : tamil" + "\n" + \
                       "╠ te : telugu" + "\n" + \
                       "╠ th : thai" + "\n" + \
                       "╠ tr : turkish" + "\n" + \
                       "╠ uk : ukrainian" + "\n" + \
                       "╠ ur : urdu" + "\n" + \
                       "╠ uz : uzbek" + "\n" + \
                       "╠ vi : vietnamese" + "\n" + \
                       "╠ cy : welsh" + "\n" + \
                       "╠ xh : xhosa" + "\n" + \
                       "╠ yi : yiddish" + "\n" + \
                       "╠ yo : yoruba" + "\n" + \
                       "╠ zu : zulu" + "\n" + \
                       "╠ fil : Filipino" + "\n" + \
                       "╠ he : Hebrew" + "\n" + \
                       "╚══[ Jangan Typo ]" + "\n" + "\n\n" + \
                         "Contoh : ˢᴬᵞ-ᴵᴰ ᶠᴱᴺᴰᵞ ᴶᴱᴸᴱˣ"
    return helpTranslate
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
               line.sendMessage(op.param1,"нαℓσ {} \nтяιмαкαѕιн ѕυ∂αн α∂∂\n💋 σρєи σя∂єя ѕєℓfвσт  💋\n http://line.me/ti/p/~jofe_na\n http://line.me/ti/p/~zudistira89".format(str(line.getContact(op.param1).displayName)))
                
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            if mid in op.param3:
                if op.param2 in Bots:
                    line.acceptGroupInvitation(op.param1)
            if Amid in op.param3:
                if op.param2 in Bots:
                    kiker1.acceptGroupInvitation(op.param1) 
            if Bmid in op.param3:
                if op.param2 in Bots:
                    kiker2.acceptGroupInvitation(op.param1)
            if Cmid in op.param3:
                if op.param2 in Bots:
                    kiker3.acceptGroupInvitation(op.param1)
            if Dmid in op.param3:
                if op.param2 in Bots:
                    kiker4.acceptGroupInvitation(op.param1)
            if mid in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in admin:
                        line.acceptGroupInvitation(op.param1)
                        dan = line.getContact(op.param2)
                        tgb = line.getGroup(op.param1)
                        sendMentionFooter(op.param1, "@!, Thx for invited Me".format(str(tgb.name)),[op.param2])
                        line.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                        line.sendContact(op.param1, op.param2)
                    else:
                        pass

        if op.type == 13:
            print (" [ 13 ] AUTO LEAVE")
            if mid in op.param3:
                if settings["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in admin:
                        line.acceptGroupInvitation(op.param1)
                        ginfo = line.getGroup(op.param1)
                        line.sendMessage(op.param1,"Sorry! I am Leave\n" + str(ginfo.name))
                        line.leaveGroup(op.param1)
                    else:
                        pass
        
        if op.type == 55:
            print ("[ 55  ] READ BL")
            if op.param2 in settings["blacklist"]:
                random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 26:
            print ("[ 26 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}

            if msg.contentType == 1:
                    path = line.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n╠ Sticker ID : {}".format(stk_id)
                   ret_ += "\n╠ Sticker Version : {}".format(stk_ver)
                   ret_ += "\n╠ Sticker Package : {}".format(pkg_id)
                   ret_ += "\n╠ Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = line.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if settings["checkSticker"] == True:
                    msg.contentType = 0
                    line.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n?Link Sticker?" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])

        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = line.getGroup(at)
                                ariftj = line.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ariftj.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ariftj.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                line.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                line.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = line.getGroup(at)
                                ariftj = line.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "╔══[ Pesan Dihapus ]"
                                ret_ += "\n╠ Pengirim : {}".format(str(ariftj.displayName))
                                ret_ += "\n╠  Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n╠  Waktu Ngirim' : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n╠  Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n╚══[ Finish ]"
                                line.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = line.getGroup(at)
                                ariftj = line.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "╔══[ Sticker Dihapus ]"
                                ret_ += "\n╠ Pengirim : {}".format(str(ariftj.displayName))
                                ret_ += "\n╠ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n╠ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                ret_ += "\n╚══[ Finish ]"
                                line.sendMessage(at, str(ret_))
                                line.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
            print ("[ 26 ] tlakban")
            msg = op.message
            if settings["talkban"] == True:
             if msg._from in settings["talkblacklist"]:
                    line.sendMessage(msg.to,line.getContact(msg._from).displayName + " jgn ngomong")
                    line.kickoutFromGroup(msg.to,[msg._from])

        if op.type == 26:
            print ("[ 26 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                elif text.lower() in wordban:
                  	 line.sendMessage(to, "Maaf, {} termasuk dalam wordban.".format(str(text)))
                  	 line.kickoutFromGroup(to, [sender])    

            if msg.contentType == 16:
                if settings["likeOn"] == True:
                    url = msg.contentMetadata["postEndUrl"]
                    daftarLike = [1001,1002,1003,1004,1005,1006]
                    likeType = random.choice(daftarLike)
                    kiker5.likePost(url[25:58], url[66:], likeType)
                    kiker5.createComment(url[25:58], url[66:], settings["Comment"])

        if op.type == 25:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        line.sendMessage(msg.to,"It's included in a blacklist already〄1�7")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        line.sendMessage(msg.to,"I decided not to make a comment〄1�7")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        line.sendMessage(msg.to,"It was eliminated from a blacklist〄1�7")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        line.sendMessage(msg.to,"It isn't included in a blacklist〄1�7")
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        line.sendMessage(msg.to,"It's included in a blacklist already.〄1�7")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        line.sendMessage(msg.to,"It was added to the blacklist.〄1�7")
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        line.sendMessage(msg.to,"It was eliminated from a blacklist〄1�7")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        line.sendMessage(msg.to,"It isn't included in a blacklist〄1�7")

            if msg.contentType == 13:
                if settings['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = line.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             line.sendMessage(msg.to, _name + " вєяα∂α ∂ι gяσυρ ιиι")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 kiker4.findAndAddContactsByMid(target)
                                 kiker4.inviteIntoGroup(msg.to,[target])
                                 kiker4.sendMessage(msg.to,"Invite " + _name)
                                 settings['invite'] = False
                                 break                              
                             except:             
                                      line.sendMessage(msg.to,"Error")
                                      settings['invite'] = False
                                      break

        if op.type == 25:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return


                if "join" in msg.text.lower():
                     if settings["autoJoinTicket"] == True:
                         link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                         links = link_re.findall(text)
                         n_links = []
                         for l in links:
                             if l not in n_links:
                                 n_links.append(l)
                         for ticket_id in n_links:
                             group = line.findGroupByTicket(ticket_id)
                             line.acceptGroupInvitationByTicket(group.id,ticket_id)
                             kiker1.acceptGroupInvitationByTicket(group.id,ticket_id)
                             kiker2.acceptGroupInvitationByTicket(group.id,ticket_id)
                             kiker3.acceptGroupInvitationByTicket(group.id,ticket_id)
                             kiker4.acceptGroupInvitationByTicket(group.id,ticket_id)
                             line.sendMessage(to, "вєянαѕιℓ мαѕυк кє ∂αℓαм gяσυρ %s" % str(group.name))
#==============================================================================#
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    line.sendMessage(to, str(helpMessage))
                    line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~bheghenkz2', 'type': 'mt', 'subText': "  ✰feŇa✰  ", 'a-installUrl': 'https://line.me/ti/p/~bheghenkz2', 'a-installUrl': ' https://line.me/ti/p/~bheghenkz2', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~bheghenkz2', 'i-linkUri': 'https://line.me/ti/p/~bheghenkz2', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~bheghenkz2'}, contentType=19)
                elif text.lower() == 'texttospeech':
                    helpTextToSpeech = helptexttospeech()
                    line.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'translate':
                    helpTranslate = helptranslate()
                    line.sendMessage(to, str(helpTranslate))
                elif text.lower() == 'crash':
                     line.sendContact(to, "ue142372725c854ff24742b5ef2168006',")
                elif text.lower() == '@bye':
                      if msg.toType == 2:
                         line.sendMessage(to, " GσσԃႦყҽ  -,-")
                         line.leaveGroup(to)
                elif msg.text.lower().startswith("changename: "):
                       separate = msg.text.split(" ")
                       string = msg.text.replace(separate[0] + " ","")
                       if len(string) <= 10000000000:
                         profile = line.getProfile()
                         profile.displayName = string
                         line.updateProfile(profile)
                         sendMessageWithFooter(to,"chαngєd " + string + "")

                elif msg.text.lower().startswith("changebio: "):
                       separate = msg.text.split(" ")
                       string = msg.text.replace(separate[0] + " ","")
                       if len(string) <= 10000000000:
                         profile = line.getProfile()
                         profile.statusMessage = string
                         line.updateProfile(profile)
                         sendMessageWithFooter(msg.to,"chαngєd " + string)
                elif msg.text.lower().startswith("bot1name: "):
                       separate = msg.text.split(" ")
                       string = msg.text.replace(separate[0] + " ","")
                       if len(string) <= 10000000000:
                         profile = kiker1.getProfile()
                         profile.displayName = string
                         kiker1.updateProfile(profile)
                         sendMessageWithFooter1(to,"chαngєd " + string + "")
                elif msg.text.lower().startswith("bot2name: "):
                       separate = msg.text.split(" ")
                       string = msg.text.replace(separate[0] + " ","")
                       if len(string) <= 10000000000:
                         profile = kiker2.getProfile()
                         profile.displayName = string
                         kiker2.updateProfile(profile)
                         sendMessageWithFooter2(to,"chαngєd " + string + "")
                elif msg.text.lower().startswith("bot3name: "):
                       separate = msg.text.split(" ")
                       string = msg.text.replace(separate[0] + " ","")
                       if len(string) <= 10000000000:
                         profile = kiker3.getProfile()
                         profile.displayName = string
                         kiker3.updateProfile(profile)
                         sendMessageWithFooter3(to,"chαngєd " + string + "") 
                elif msg.text.lower().startswith("bot4name: "):
                       separate = msg.text.split(" ")
                       string = msg.text.replace(separate[0] + " ","")
                       if len(string) <= 10000000000:
                         profile = kiker4.getProfile()
                         profile.displayName = string
                         kiker4.updateProfile(profile)
                         sendMessageWithFooter4(to,"chαngєd " + string + "") 

                elif msg.text.lower().startswith("fbroadcast "):
                        sep = text.split(" ")
                        txt = text.replace(sep[0] + " ","")
                        contacts = line.getAllContactIds()
                        for contact in contacts:
                                sendMessageWithFooter(contact, "[ Broadcast ]\n{}".format(str(txt)))
                        sendMessageWithFooter(to, "Berhasil broadcast ke {} teman".format(str(len(contacts))))

                elif msg.text.lower().startswith("broadcast "):
                            if sender in lineMID:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                groups = line.groups
                                for group in groups:
                                    sendMessageWithFooter(group, "[ вяσα∂¢αѕт ]\n{}".format(str(txt)))
                                sendMessageWithFooter(to, "вєянαѕιℓ вяσα∂¢αѕт кє {} gяσυρ".format(str(len(groups))))

                elif text.lower() == 'pendinglist': 
                          if msg.toType == 2:
                              group = line.getGroup(to)
                              ret_ = "╔══[ ρєи∂ιиg ℓιѕт ]"
                              no = 0 + 1
                              if group.invitee is None or group.invitee == []:
                                  sendMessageWithFooter(to, "тι∂αк α∂α ρєи∂ιиgαи")
                                  return
                              else:
                                  for pen in group.invitee:
                                      ret_ += "\n╠ {}. {}".format(str(no), str(pen.displayName))
                                      no += 1
                                  ret_ += "\n╚══[ Total {} ]".format(str(len(group.invitee)))
                                  sendMessageWithFooter(to, str(ret_))

                elif text.lower() == 'blocklist': 
                            blockedlist = line.getBlockedContactIds()
                            kontak = line.getContacts(blockedlist)
                            ret_ = "╔══[ Block List ]"
                            no = 0 + 1
                            for ids in kontak:
                                ret_ += "\n╠ {}. {}".format(str(no), str(ids.displayName))
                                no += 1
                            ret_ += "\n╚══[ Total {} Block ]".format(str(len(kontak)))
                            sendMessageWithFooter(to, str(ret_))

                elif text.lower() == 'memberlist': 
                            if msg.toType == 2:
                                group = line.getGroup(to)
                                ret_ = "╔══[ Member List ]"
                                no = 0 + 1
                                for mem in group.members:
                                    ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                                    no += 1
                                ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                                sendMessageWithFooter(to, str(ret_))

                elif text.lower() == 'flist':
                            contactlist = line.getAllContactIds() 
                            kontak = line.getContacts(contactlist)
                            ret_ = "╔══[ Friends List ]"
                            no = 0 + 1
                            for ids in kontak:
                                ret_ += "\n╠ {}. {}".format(str(no), str(ids.displayName))
                                no += 1
                            ret_ += "\n╚══[ Total {} Friends ]".format(str(len(kontak)))
                            sendMessageWithFooter(to, str(ret_))
                elif msg.text.lower().startswith("bc3"):
                        	wildan = text.split("|")
                        	bc["txt"] = wildan[1];bc["mid"] = wildan[2];bc["img"] = True
                        	sendMessageWithFooter(to, "Silahkan kirim gambar.")
                elif msg.text.lower().startswith("infomem "):
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = line.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = line.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "🃏"+ str(no) + ". " + mem.displayName
                                sendMessageWithFooter(to,"🃏Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n🃏Total %i Members🃏" % len(G.members))
                            except: 
                                pass 

                elif msg.text.lower().startswith("finfo "):
                        sep = text.split(" ")
                        query = text.replace(sep[0] + " ","")
                        contacts = line.getAllContactIds()
                        try:
                            listContact = contacts[int(query)-1]
                            contact = line.getContact(listContact)
                            #cover = line.getProfileCoverURL(listContact)
                            result = "╔══[ Details Profile ]"
                            result += "\n╠ Display Name : @!"
                            result += "\n╠ Mid : {}".format(contact.mid)
                            result += "\n╠ Status Message : {}".format(contact.statusMessage)
                            result += "\n╠ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            #result += "\n╠ Cover : {}".format(str(cover))
                            result += "\n╚══[ Finish ]"
                            line.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            sendMentionFooter(to, result, [contact.mid])
                        except Exception as error:
                                logError(error)
#===========Token======
                elif text.lower() == 'token win10':
                   req = requests.get(url = 'https://api.eater.host/WIN10')
                   a = req.text
                   b= json.loads(a)
                   link = b['result'][0]['linktkn']
                   qrz = b['result'][0]['linkqr']
                   tokenz['{}'.format(msg._from)]= link
                   line.sendMessage(msg.to, '{}'.format(qrz))
                elif text.lower() == 'token ipad':
                   req = requests.get(url = 'https://api.eater.pw/IOSIPAD')
                   a = req.text
                   b= json.loads(a)
                   link = b['result'][0]['linktkn']
                   qrz = b['result'][0]['linkqr']
                   tokenz['{}'.format(msg._from)]= link
                   line.sendMessage(msg.to, '{}'.format(qrz))
                elif text.lower() == 'token desktopwin':
                   req = requests.get(url = 'https://api.eater.pw/DESKTOPWIN')
                   a = req.text
                   b= json.loads(a)
                   link = b['result'][0]['linktkn']
                   qrz = b['result'][0]['linkqr']
                   tokenz['{}'.format(msg._from)]= link
                   line.sendMessage(msg.to, '{}'.format(qrz))
                elif text.lower() == 'token desktopmac':
                   req = requests.get(url = 'https://api.eater.pw/DESKTOPMAC')
                   a = req.text
                   b= json.loads(a)
                   link = b['result'][0]['linktkn']
                   qrz = b['result'][0]['linkqr']
                   tokenz['{}'.format(msg._from)]= link
                   line.sendMessage(msg.to, '{}'.format(qrz))
                elif text.lower() == 'token chrome':
                   req = requests.get(url = 'https://api.eater.pw/CHROMEOS')
                   a = req.text
                   b= json.loads(a)
                   link = b['result'][0]['linktkn']
                   qrz = b['result'][0]['linkqr']
                   tokenz['{}'.format(msg._from)]= link
                   line.sendMessage(msg.to, '{}'.format(qrz)) 
                elif text.lower() == 'token done':
                   a = tokenz['{}'.format(msg._from)]
                   req = requests.get(url = '{}'.format(a))
                   b = req.text
                   line.sendMessage(msg.to, '{}'.format(b))
#============#
                elif "addbots" in msg.text.lower():
                     line.findAndAddContactsByMid(Amid)
                     line.findAndAddContactsByMid(Bmid)
                     line.findAndAddContactsByMid(Cmid)
                     line.findAndAddContactsByMid(Dmid)
                     sendMessageWithFooter(msg.to,'Done')

                     kiker1.findAndAddContactsByMid(mid)
                     kiker1.findAndAddContactsByMid(Bmid)
                     kiker1.findAndAddContactsByMid(Cmid)
                     kiker1.findAndAddContactsByMid(Dmid)
                     sendMessageWithFooter1(msg.to,'Done')

                     kiker2.findAndAddContactsByMid(mid)
                     kiker2.findAndAddContactsByMid(Amid)
                     kiker2.findAndAddContactsByMid(Cmid)
                     kiker2.findAndAddContactsByMid(Dmid)
                     sendMessageWithFooter2(msg.to,'Done')

                     kiker3.findAndAddContactsByMid(mid)
                     kiker3.findAndAddContactsByMid(Amid)
                     kiker3.findAndAddContactsByMid(Bmid)
                     kiker3.findAndAddContactsByMid(Dmid)
                     sendMessageWithFooter3(msg.to,'Done')

                     kiker4.findAndAddContactsByMid(mid)
                     kiker4.findAndAddContactsByMid(Amid)
                     kiker4.findAndAddContactsByMid(Bmid)
                     kiker4.findAndAddContactsByMid(Cmid)
                     sendMessageWithFooter4(msg.to,'Done')

#==============================================================================#
                elif text.lower() == 'ban':
                 settings["wblacklist"] = True
                 sendMessageWithFooter(msg.to,"send the target contents")
                elif text.lower() == 'unban':
                 settings["dblacklist"] = True
                 sendMessageWithFooter(msg.to,"sєnd thє untαrgєt cσntєnt")
                elif text.lower() == 'banlist':
                  if settings["blacklist"] == {}:
                    sendMessageWithFooter(msg.to,"иσ вℓα¢кℓιѕт")
                  else:
                    sendMessageWithFooter(msg.to,"вℓα¢кℓιѕт")
                    mc = ""
                    for mi_d in settings["blacklist"]:
                        mc += "\nвαиℓιѕт\n\n" +line.getContact(mi_d).displayName + "\n"
                    sendMessageWithFooter(msg.to,mc)
                elif text.lower() == 'clearban':
                   settings["blacklist"] = {}
                   sendMessageWithFooter(msg.to,"вℓα¢кℓιѕт тєℓαн ∂ι вєяѕιнкαи")
                elif text.lower() == 'mati-kau':
                  if msg.toType == 2:
                    group = line.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in settings["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        sendMessageWithFooter(msg.to,"There wasn't a blacklist user")
                        return
                    for jj in matched_list:
                        try:
                            klist=[line,kiker1,kiker2,kiker3,kiker4]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass

                elif "tlakban" in msg.text.lower():
                  if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["talkblacklist"][target] = True
                            group = line.getContact(target)
                            sendMessageWithFooter(msg.to,group.displayName + " Succes Add to Talkban")
                        except:
                            sendMessageWithFooter(msg.to,"Error")
                  else:
                    settings["talkblacklist"] = True
                    sendMessageWithFooter(msg.to,"Send a contact to talkban")

                elif "untlakban" in msg.text.lower():
                  if 'MENTION' in msg.contentMetadata.keys()!=None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["talkblacklist"][target]
                            group = line.getContact(target)
                            sendMessageWithFooter(msg.to,group.displayName + " Delete From Talkban")
                        except:
                            group = line.getContact(target)
                            sendMessageWithFooter(msg.to,group.displayName + " Not In Talkban")
                elif text.lower() == 'tban':
                 settings["talkblacklist"] = True
                 sendMessageWithFooter(msg.to,"send the target contents")
                elif text.lower() == 'untban':
                 settings["dblacklist"] = True
                 sendMessageWithFooter(msg.to,"sєnd thє untαrgєt cσntєnt")
                elif text.lower() == 'jepite':
                 settings["invite"] = True
                 sendMessageWithFooter(msg.to,"Send Contact")
#==================WORDBAN#
                elif text.lower() == "wbanlist":
                	if wordban not in [[]]:
                		no = 1
                		wordbans = "[ Word Ban ]\n"
                		for word in wordban:
                			wordbans+="\n{}. {}".format(str(no),str(word))
                			no+=1
                		wordbans+="\n\n[ Finish ]"
                		sendMessageWithFooter(to, str(wordbans))
                	if wordban == []:
                		sendMessageWithFooter(to, "Tidak ada wordban saat ini.")
                elif text.lower().startswith("addwban: "):
                	word = text.replace("addwban: ","")
                	if word not in wordban:
                		wordban.append(word)
                		sendMessageWithFooter(to, "Sukses menambahkan {} ke dalam wordban.".format(str(word)))
                	else:
                		sendMessageWithFooter(to, "{} sudah ada didalam wordban.".format(str(word)))
                elif text.lower().startswith("delwban: "):
                	word = text.replace("delwban: ","")
                	if word in wordban:
                		wordban.remove(word)
                		sendMessageWithFooter(to, "Sukses menghapus {} dari wordban.".format(str(word)))
                	else:
                		sendMessageWithFooter(to, "{} tidak ada didalam wordban.".format(str(word)))
#======================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    line.sendMessage(to, "ρℓєα¢є ωαιтιиg")
                    elapsed_time = time.time() - start
                    sendMessageWithFooter(to,format(str(elapsed_time)))
                elif text.lower() == 'restart':
                    sendMessageWithFooter(to, "ℓєα¢є ωαιтιиg")
                    sendMessageWithFooter(to, "∂σиє яєѕтαятιиg")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    sendMessageWithFooter(to, "тнє вσт нαѕ вєєи яυииιиg {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u7d36f5837c96fa1ef95b9bdcacf92b66"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╔══[ About Self ]"
                        ret_ += "\n╠ Line : {}".format(contact.displayName)
                        ret_ += "\n╠ Group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ Friend : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blocked : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ About Selfbot ]"
                        ret_ += "\n╠ Version : јόғέή Test"
                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                        ret_ += "\n╚══[ Ｈｅｌｌｏ Ｗｏｒｌｄ ]"
                        sendMessageWithFooter(to, str(ret_))
                    except Exception as e:
                        sendMessageWithFooter(msg.to, str(e))
                elif text.lower() == 'myprofile': 
                     contact = line.getContact(sender)
                     #cover = line.getProfileCoverURL(sender)
                     result = "╔══[ Details Profile ]"
                     result += "\n╠ Display Name : @!"
                     result += "\n╠ Mid : {}".format(contact.mid)
                     result += "\n╠ Status Message : {}".format(contact.statusMessage)
                     result += "\n╠ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                     #result += "\n╠ Cover : {}".format(str(cover))
                     result += "\n╚══[ Finish ]"
                     line.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                     sendMentionFooter(to, result, [sender])
#==============================================================================#
                elif text.lower() == 'status':
                    try:
                        ret_ = "╔══[ Status ]"
                        if settings["autoAdd"] == True: ret_ += "\n╠ Auto Add ✅"
                        else: ret_ += "\n╠ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠ Auto Join ✅"
                        else: ret_ += "\n╠ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠ Auto Leave ✅"
                        else: ret_ += "\n╠ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠ Auto Read ✅"
                        else: ret_ += "\n╠ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n╠ Check Sticker ✅"
                        else: ret_ += "\n╠ Check Sticker ❌"
                        if settings["datectMention"] == True: ret_ += "\n╠ Detect Mention ✅"
                        else: ret_ += "\n╠ Detect Mention ❌"
                        if settings["datectMention2"] == True: ret_ += "\n╠ Detect Mention2 ✅"
                        else: ret_ += "\n╠ Detect Mention2 ❌"
                        if settings["protect"] == True: ret_ += "\n╠ Protect group ✅"
                        else: ret_ += "\n╠ Protect group ❌"
                        if settings["projoin"] == True: ret_ += "\n╠ Projoin group ✅"
                        else: ret_ += "\n╠ ProJoin group ❌"
                        if settings["linkprotect"] == True: ret_ += "\n╠ Link protect ✅"
                        else: ret_ += "\n╠ Link protect ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n╠ Protect invite ✅"
                        else: ret_ += "\n╠ Protect invite ❌"
                        if settings["cancelinvite"] == True: ret_ += "\n╠ Cancel members ✅"
                        else: ret_ += "\n╠ Cancel members ❌"
                        if settings["ghost"] == True: ret_ += "\n╠ Kicker ✅"
                        else: ret_ += "\n╠ Kicker ❌"
                        if settings["talkban"] == True: ret_ += "\n╠ Tlakblack ✅"
                        else: ret_ += "\n╠ Tlakblack ❌"
                        if settings["unsendMessage"] == True: ret_ += "\n╠ Unsend Message ✅"
                        else: ret_ += "\n╠ Unsend Message ❌"
                        ret_ += "\n╚══[ Status ]"
                        sendMessageWithFooter(to, str(ret_))
                    except Exception as e:
                        sendMessageWithFooter(msg.to, str(e))
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαктιfкαи αυтσ α∂∂ ")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgиσктιfкαи αυтσ α∂∂ ")
                elif text.lower() == 'autojoin on':
                    settings["autoJoin"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαтιfкαи αυтσ נσιи ")
                elif text.lower() == 'autojoin off':
                    settings["autoJoin"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgиσкαтιfкαи αυтσ נσιи ")
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαктιfкαи αυтσ ℓєανє")
                elif text.lower() == 'autoleave off':
                    settings["autoLeave"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиσиαктιfкαи αυтσ ℓєανє")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαктιfкαи αυтσ яєє∂")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgиσктιfкαи αυтσ яєє∂")
                elif text.lower() == 'checksticker on':
                    settings["checkSticker"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαктιfкαи ¢нє¢к ∂єтαιℓ ѕтι¢кєя")
                elif text.lower() == 'checksticker off':
                    settings["checkSticker"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgиσктιfкαи ¢нє¢к ∂єтαιℓ ѕтι¢кєя")
                elif text.lower() == 'detectmention on':
                    settings["datectMention"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαктιfкαи ∂єтє¢т мєитισи")
                elif text.lower() == 'detectmention off':
                    settings["datectMention"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиσиαктιfкαи ∂єтє¢т мєитισи")
                elif text.lower() == 'detectmention2 on':
                    settings["datectMention2"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαктιfкαи ∂єтє¢т мєитισи")
                elif text.lower() == 'detectmention2 off':
                    settings["datectMention2"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиσиαктιfкαи ∂єтє¢т мєитισи")
                elif text.lower() == 'ghost on':
                    settings["ghost"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαктιfкαи кι¢кєя")
                elif text.lower() == 'ghost off':
                    settings["ghost"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgиσктιfкαи кι¢кєя")
                elif text.lower() == 'cancel on':
                    settings["cancelinvite"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαктιfкαи ¢αи¢єℓ")
                elif text.lower() == 'cancel off':
                    settings["cancelinvite"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgиσктιfкαи ¢αи¢єℓ")
                elif text.lower() == 'protect on':
                    settings["protect"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαктιfкαи ρяσтє¢т")
                elif text.lower() == 'protect off':
                    settings["protect"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgиσктιfкαи ρяσтє¢т")                
                elif text.lower() == 'projoin on':
                    settings["projoin"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαктιfкαи ρяσтє¢тנσιи")
                elif text.lower() == 'projoin off':
                    settings["projoin"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgиσктιfкαи ρяσтє¢тנσιи")
                elif text.lower() == 'link on':
                    settings["linkprotect"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαктιfкαи ℓιикρяσ")
                elif text.lower() == 'link off':
                    settings["linkprotect"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgиσктιfкαи ℓιикρяσ")
                elif text.lower() == 'invite on':
                    settings["inviteprotect"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαктιfкαи ρяσιиνιтє")
                elif text.lower() == 'invite off':
                    settings["inviteprotect"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgиσктιfкαи ρяσιиνιтє")
                elif text.lower() == 'tlak on':
                    settings["talkban"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαктιfкαи тαℓквαи")
                elif text.lower() == 'tlak off':
                    settings["talkban"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgиσктιfкαи тαℓквαи")
                elif text.lower() == 'unsendchat on':
                    settings["unsendMessage"] = True
                    sendMessageWithFooter(to, "Berhasil mengaktifkan unsend message")
                elif text.lower() == 'unsendchat off':
                    settings["unsendMessage"] = False
                    sendMessageWithFooter(to, "Berhasil menonaktifkan unsend message")
                elif text.lower() == 'contact on':
                    settings["checkContact"] = True
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиgαктιfкαи ¢σитα¢т")
                elif text.lower() == 'contact off':
                    settings["checkContact"] = False
                    sendMessageWithFooter(to, "вєянαѕιℓ мєиσиαктιfкαи ¢σитα¢т")
      
                elif text.lower() == 'welcome on':
                   if settings["Sambutan"] == True:
                       if settings["lang"] == "JP":
                           sendMessageWithFooter(msg.to,"ѕυ∂αн σи")
                   else:
                       settings["Sambutan"] = True
                       if settings["lang"] == "JP":
                           sendMessageWithFooter(msg.to,"Sαмвυтαи ∂ι αктιfкαи")

                elif text.lower() == 'welcome off':
                   if settings["Sambutan"] == False:
                       if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ѕυ∂αн σff")
                   else: 
                       settings["Sambutan"] = False
                       if settings["lang"] == "JP":
                           sendMessageWithFooter(msg.to,"Sαмвυтαи ∂ι иσиαктιfкαи")

                elif text.lower() == 'minggat on':
                   if settings["Jembutan"] == True:
                       if settings["lang"] == "JP":
                           sendMessageWithFooter(msg.to,"ѕυ∂αн σи")
                   else:
                       settings["Jembutan"] = True
                       if settings["lang"] == "JP":
                           sendMessageWithFooter(msg.to,"Sαмвυтαи ∂ι αктιfкαи")

                elif text.lower() == 'minggat off':
                   if settings["Jembutan"] == False:
                       if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ѕυ∂αн σff")
                   else: 
                       settings["Jembutan"] = False
                       if settings["lang"] == "JP":
                           sendMessageWithFooter(msg.to,"Sαмвυтαи ∂ι иσиαктιfкαи")
#======================Allrotect==============================#
                elif text.lower() == 'allpro on': 
                  if settings["inviteprotect"] == True:
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(to, "ρяσιиνιтє αℓяєα∂у σи")
                  else:
                      settings["inviteprotect"] = True
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσιиνιтє яєα∂у")
                  if settings["cancelinvite"] == True:
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσ¢αи¢єℓ αℓяєα∂у σи")
                  else:
                      settings["cancelinvite"] = True
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσ¢αи¢єℓ яєα∂у")
                  if settings["protect"] == True:
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσкι¢к αℓяєα∂у σи")
                  else:
                      settings["protect"] = True
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσкι¢к яєα∂у")
                  if settings["linkprotect"] == True:
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσυяℓ αℓяєα∂у σи")
                  else:
                      settings["linkprotect"] = True
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσυяℓ яєα∂у ")
                  if settings["projoin"] == True:
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяנσιи αℓяєα∂у σи")
                  else:
                      settings["projoin"] = True
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяנσιи яєα∂у")

                elif text.lower() == 'allpro off':
                  if settings["inviteprotect"] == False:
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσιиνιтє αℓяєα∂у σff")
                  else:
                      settings["inviteprotect"] = False
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσιиνιтє ∂ιѕαвℓє")
                  if settings["cancelinvite"] == False:
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσ¢αи¢єℓ αℓяєα∂у σff")
                  else:
                      settings["cancelinvite"] = False
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσ¢αи¢єℓ ∂ιѕαвℓє")
                  if settings["protect"] == False:
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσкι¢к αℓяєα∂у σff")
                  else:
                      settings["protect"] = False
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσкι¢к ∂ιѕαвℓє")
                  if settings["linkprotect"] == False:
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσυяℓ αℓяєα∂у σff")
                  else:
                      settings["linkprotect"] = False
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσυяℓ ∂ιѕαвℓє")
                  if settings["projoin"] == False:
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσנσιи αℓяєα∂у σff")
                  else:
                      settings["projoin"] = False
                      if settings["lang"] == "JP":
                          sendMessageWithFooter(msg.to,"ρяσנσιи ∂ιѕαвℓє")
#==============================================================================#
                elif text.lower() == 'mygirl':
                    line.sendContact(to, lineMID)
                    line.sendContact(to, kiker1MID)
                    line.sendContact(to, kiker2MID)
                    line.sendContact(to, kiker3MID)
                    line.sendContact(to, kiker4MID)
                elif text.lower() == 'refresh':
                   line.removeAllMessages(op.param2)
                   sendMessageWithFooter(msg.to,"∂σиє")
                   kiker1.removeAllMessages(op.param2)
                   sendMessageWithFooter1(msg.to,"∂σиє")
                   kiker2.removeAllMessages(op.param2)
                   sendMessageWithFooter2(msg.to,"∂σиє")
                   kiker3.removeAllMessages(op.param2)
                   sendMessageWithFooter3(msg.to,"∂σиє")
                   kiker4.removeAllMessages(op.param2)
                   sendMessageWithFooter4(msg.to,"∂σиє")
#===================CONTACTBOT==================================================#
                elif text.lower() == 'me':
                    sendMentionFooter(to, "@!", [sender])
                    line.sendMessage(to, line.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+line.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~bheghenkz2', 'type': 'mt', 'subText': "  🔒ᶠᵁᶜᴷ ᶠᴬᴷᴱ ᶠᴿᴵᴱᴺᴰ🔒 🔒 ˢᴵᶠᴬᵀ ᴳᵁᴱ ᵀᴱᴿᴳᴬᴺᵀᵁᴺᴳ ˢᴵᶠᴬᵀ ᴸᵁ ᴷᴱ ᴳᵁᴱ 🔒 ", 'a-installUrl': 'https://line.me/ti/p/~bheghenkz2', 'a-installUrl': ' https://line.me/ti/p/~bheghenkz2', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~bheghenkz2', 'i-linkUri': 'https://line.me/ti/p/~bheghenkz2', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~bheghenkz2'}, contentType=19)
                elif text.lower() == '.me':
                    sendMentionFooter(to, " @!", [sender])
                    line.sendContact(to, lineMID)
                elif text.lower() == 'mymid':
                    sendMessageWithFooter(msg.to, lineMID)
                elif text.lower() == 'allmid':
                    sendMessageWithFooter(msg.to, lineMID)
                    sendMessageWithFooter1(msg.to, kiker1MID)
                    sendMessageWithFooter2(msg.to, kiker2MID)
                    sendMessageWithFooter3(msg.to, kiker3MID)
                    sendMessageWithFooter4(msg.to, kiker4MID)
#===========================>========================================#
                elif text.lower() == '!fen':
                       random.choice(assist).sendMessage(to, "Hadir...........-,-")

                elif text.lower() == '!respon':
                       sendMessageWithFooter1(to, "Hadir......")
                       sendMessageWithFooter2(to, "Hadir......")
                       sendMessageWithFooter3(to, "Hadir......")
                       sendMessageWithFooter4(to, "Hadir......") 

                elif text.lower() == 'myname':
                    me = line.getContact(lineMID)
                    sendMessageWithFooter(msg.to,"[∂ιѕρℓαуиαмє]\n"+ me.displayName)

                elif text.lower() == "respon":
                    me = kiker1.getContact(kiker1MID)
                    sendMessageWithFooter1(msg.to, me.displayName)
                    me = kiker2.getContact(kiker2MID)
                    sendMessageWithFooter2(msg.to, me.displayName)
                    me = kiker3.getContact(kiker3MID)
                    sendMessageWithFooter3(msg.to, me.displayName)
                    me = kiker4.getContact(kiker4MID)
                    sendMessageWithFooter4(msg.to, me.displayName)

                elif text.lower() == 'mybio':
                    me = line.getContact(lineMID)
                    sendMessageWithFooter(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)

                elif text.lower() == 'botpict':
                     me = kiker1.getContact(kiker1MID)
                     kiker1.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                     me = kiker2.getContact(kiker2MID)
                     kiker2.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                     me = kiker3.getContact(kiker3MID)
                     kiker3.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                     me = kiker4.getContact(kiker4MID)
                     kiker4.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)

                elif text.lower() == 'myvideoprofile':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("stealcontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("stealmid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        sendMessageWithFooter(msg.to, str(ret_))
                elif msg.text.lower().startswith("stealname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            sendMessageWithFooter(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("stealbio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            sendMessageWithFooter(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("stealpicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealvideoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("stealcover "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cloneprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            line.cloneContactProfile(contact)
                            sendMessageWithFooter(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                        except:
                            sendMessageWithFooter(msg.to, "Gagal clone member")
                elif text.lower() == 'restoreprofile':
                    try:
                        lineProfile.displayName = str(myProfile["displayName"])
                        lineProfile.statusMessage = str(myProfile["statusMessage"])
                        lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                        line.updateProfileAttribute(8, lineProfile.pictureStatus)
                        line.updateProfile(lineProfile)
                        sendMessageWithFooter(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                    except:
                        sendMessageWithFooter(msg.to, "Gagal restore profile")
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            sendMessageWithFooter(msg.to,"Target ditambahkan!")
                            break
                        except:
                            sendMessageWithFooter(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            sendMessageWithFooter(msg.to,"Target dihapuskan!")
                            break
                        except:
                            sendMessageWithFooter(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        sendMessageWithFooter(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        sendMessageWithFooter(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            sendMessageWithFooter(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            sendMessageWithFooter(msg.to,"Reply Message off")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = line.getGroup(to)
                    sendMessageWithFooter(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = line.getGroup(to)
                    sendMessageWithFooter(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'groupticket':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            sendMessageWithFooter(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            sendMessageWithFooter(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'gurl':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            sendMessageWithFooter(to, "Grup qr sudah terbuka")
                        else:
                            group.preventJoinByTicket = False
                            line.updateGroup(group)
                            ticket = line.reissueGroupTicket(to)
                            sendMessageWithFooter(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))

                elif text.lower() == 'curl':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            sendMessageWithFooter(to, "Grup qr sudah tertutup")
                        else:
                            group.preventJoinByTicket = True
                            line.updateGroup(group)
                            sendMessageWithFooter(to, "Berhasil menutup grup qr")
                elif text.lower() == 'groupinfo':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    sendMessageWithFooter(to, str(ret_))
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'memberlist':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        sendMessageWithFooter(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        sendMessageWithFooter(to, str(ret_))
#==============================================================================#          
                elif text.lower() == '@jof':
                            if msg.toType == 0:
                                sendMention(to, to, "", "")
                            elif msg.toType == 2:
                                group = line.getGroup(to)
                                contact = [mem.mid for mem in group.members]
                                ct1, ct2, ct3, ct4, ct5, jml = [], [], [], [], [], len(contact)
                                if jml <= 100:
                                    mentionMembers(to, contact)
                                elif jml > 100 and jml <= 200: 
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, jml):
                                        ct2 += [contact[b]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                elif jml > 200 and jml <= 300:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, jml):
                                        ct3 += [contact[c]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                elif jml > 300 and jml <= 400:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, 299):
                                        ct3 += [contact[c]]
                                    for d in range(300, jml):
                                        ct4 += [contact[d]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                    mentionMembers(to, ct4)
                                elif jml > 400 and jml <= 500:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, 299):
                                        ct3 += [contact[c]]
                                    for d in range(300, 399):
                                        ct4 += [contact[d]]
                                    for e in range(400, jml):
                                        ct4 += [contact[e]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                    mentionMembers(to, ct4)
                                    mentionMembers(to, ct5)
#===================================================================#
                elif 'urlvideo ' in msg.text:
                              spl = msg.text.replace('urlvideo ','')
                              if spl in [""," ","\n",None]:
                                  line.sendMessage(msg.to, "Gagal mengganti url")
                              else:
                                  settings["vezacvp"] = spl
                                  line.sendMessage(msg.to, "✔Succes Silahkan ketik: cvp1 \nUntuk menganti Profile PhotoVideo".format(str(spl)))
                elif text.lower().startswith("cvp "):
                        contact = line.getProfile()
                        data = 'http://dl.profile.line-cdn.net/{}'.format(str(contact.pictureStatus))
                        pict = line.downloadFileURL(data)
                        vids = line.downloadFileURL(settings["vezacvp"], saveAs="video.mp4")
                        changeVideoAndPictureProfile(pict, vids)
                        line.sendMessage(to, "Berhasil mengganti Foto Profile With Video")
                        os.remove("video.mp4")
                elif text.lower() == 'cvpp':
                            nub = line.downloadFileURL('https://file.eater.pw/jpg-A9vg52.jpg')
                            nub1 = line.downloadFileURL('https://file.eater.pw/mp4-uDxMum.mp4')
                            changeVideoAndPictureProfile(nub, nub1)
                            line.sendMessage(msg.to, "Sukses")
                elif msg.text.lower().startswith("cvp: "):
                                sep = text.split(" ")
                                Veza = text.replace(sep[0] + " ","")
                                VezaGans = line.getContact(lineMID)
                                line.sendMessage(to, "Waiting.. ")
                                pic = "http://dl.profile.line-cdn.net/{}".format(VezaGans.pictureStatus)
                                subprocess.getoutput('youtube-dl --format mp4 --output vp.mp4 {}'.format(Veza))
                                pict = line.downloadFileURL(pic)
                                vids = "vp.mp4"
                                time.sleep(2)
                                changeVideoAndPictureProfile(pict, vids)
                                line.sendMessage(to, "Berhasil mengganti Foto Profile With Video")
                                os.remove("vp.mp4")
                elif text.lower() == 'changepictureprofile':
                            settings["changePicture"] = True
                            sendMessageWithFooter(to, "ѕιℓαнкαи кιяιм gαмвαяиуα")
                elif text.lower() == 'bot1changepp':
                            settings1["changePictureProfile"]["kiker1"] =True
                            sendMessageWithFooter1(to, "ѕιℓαнкαи кιяιм gαмвαяиуα") 
                elif text.lower() == 'bot2changepp':
                            settings1["changePictureProfile"]["kiker2"] = True
                            sendMessageWithFooter2(to, "ѕιℓαнкαи кιяιм gαмвαяиуα") 
                elif text.lower() == 'bot3changepp':
                            settings1["changePictureProfile"]["kiker3"] = True
                            sendMessageWithFooter3(to, "ѕιℓαнкαи кιяιм gαмвαяиуα")
                elif text.lower() == 'bot4changepp':
                            settings1["changePictureProfile"]["kiker4"] = True
                            sendMessageWithFooter4(to, "ѕιℓαнкαи кιяιм gαмвαяиуα")
                elif text.lower() == 'changevideopp': 
                            settings["ChangeVideoProfilePicture"] = True
                            sendMessageWithFooter(to, "Send Videonnya")
                elif text.lower() == 'changegrouppicture':
                            if msg.toType == 2:
                                if to not in settings["changeGroupPicture"]:
                                    settings["changeGroupPicture"].append(to)
                                sendMessageWithFooter(to, "ѕιℓαнкαи кιяιм gαмвαяиуα")

                elif text.lower() == "stc tag":
                            settings["AddstickerTag"]["status"] = True
                            sendMessageWithFooter(to, "kirim stickernya ")  

                elif text.lower() == '!gift': 
                    giftnya={'MSGTPL': '5',
                            'PRDTYPE': 'THEME',
                            'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58'}
                    line.sendMessage(msg.to,None, contentMetadata=giftnya, contentType=9) 

                elif text.lower() == '!reject': 
                    if msg.toType == 2:
                      gid = line.getGroupIdsInvited()
                      for i in gid:
                          line.rejectGroupInvitation(i)
                      sendMessageWithFooter(msg.to,"∂σиє яєנє¢т")

                elif text.lower().startswith("gname: "):
                    if msg.toType == 2:
                        X = line.getGroup(msg.to)
                        X.name = msg.text.replace("gname: ","")
                        line.updateGroup(X)
                        sendMessageWithFooter(msg.to,"ѕυкѕєѕ υρ∂αтє:\n\n"+X.name) 

                elif text.lower().startswith("setautolike: "):
                     sep = text.split(" ")
                     txt = text.replace(sep[0] + " ","")
                     try:
                         settings["Comment"] = txt
                         sendMessageWithFooter(to, "Berhasil mengubah pesan autolike menjadi : 「{}」".format(txt))
                     except:
                         sendMessageWithFooter(to, "Gagal mengubah pesan autolike")
                elif text.lower().startswith("setautores: "):
                     sep = text.split(" ")
                     txt = text.replace(sep[0] + " ","")
                     try:
                         settings["autoResponMessage"] = txt
                         sendMessageWithFooter(to, "Berhasil mengubah pesan auto respon menjadi : 「{}」".format(txt))
                     except:
                         sendMessageWithFooter(to, "Gagal mengubah pesan auto respon")

                elif text.lower().startswith("!spam "):
                     txt = msg.text.split(" ")
                     jmlh = int(txt[1])
                     teks = msg.text.replace("!spam "+str(jmlh),"")
                     for i in range(jmlh):
                         if str(txt[2])==None:
                             sendMessageWithFooter(msg.to, "ѕαℓαн ιтυ נσfєи..")
                         else:
                             try:
                                 line.sendMessage(msg.to, teks)
                             except:
                                 sendMessageWithFooter(msg.to, "ѕαℓαн ιтυ נσfєи..")

                elif text.lower().startswith("spamtag: "):
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                settings["JOFEN"] = num
                                line.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                elif text.lower().startswith("spam:tag "):
                       jum = text.split()
                       jumlah = int(jum[1])
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       targets = []
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           if jumlah <= 100:
                              for var in range(0,jumlah):
                               line.sendMessageWithMention(msg.to,jum[2],[target])
                       else:
                           sendMessageWithFooter(msg.to, "Out of range! ")

                elif text.lower() == '@fen':
                     group = line.getGroup(to)
                     midMembers = [contact.mid for contact in group.members]
                     midSelect = len(midMembers)//20
                     for mentionMembers in range(midSelect+1):
                             no = 0
                             ret_ = "╔══[ Mention Members ]"
                             dataMid = []
                             for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                     dataMid.append(dataMention.mid)
                                     no += 1
                                     ret_ += "\n╠ {}. @!".format(str(no))
                             ret_ += "\n╚══[ Total {} Members]".format(str(len(dataMid)))
                             sendMentionFooter(to, ret_, dataMid)
                elif msg.text.lower().startswith("!tag @"):
                   if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            coii = line.getContact(mention['M'])
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                            sendMessageWithMention(msg.to,coii.mid)
                        except:
                            pass

                elif "contact!" in msg.text.lower():
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID) 
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       line.sendContact(to, lineMID)
                       sendMessageWithFooter(msg.to,"∂σиє ѕραм тαяgєт")

                elif 'gift: ' in msg.text.lower():
                              korban = msg.text.replace('gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      line.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)  

                elif "woy! @" in msg.text.lower():
                   _name = msg.text.replace("woy! @","")
                   _nametarget = _name.rstrip(' ')
                   gs = line.getGroup(msg.to)
                   for g in gs.members:
                     if _nametarget == g.displayName:
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"??💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       line.sendMessage(g.mid,"💋💋👀💋💋")
                       sendMessageWithFooter(msg.to,"∂σиє ѕραм тαяgєт")
#==============================================

                elif text.lower() == 'lurking on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                sendMessageWithFooter(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            sendMessageWithFooter(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'lurking off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        sendMessageWithFooter(msg.to,"Lurking already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        sendMessageWithFooter(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        sendMessageWithFooter(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        sendMessageWithFooter(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'lurking':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            sendMessageWithFooter(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        sendMessageWithFooter(receiver,"Lurking has not been set.")

                elif text.lower() == 'bintit on':
                    try:
                        del cctv['point'][msg.to]
                        del cctv['sidermem'][msg.to]
                        del cctv['cyduk'][msg.to]
                    except:
                        pass
                    cctv['point'][msg.to] = msg.id
                    cctv['sidermem'][msg.to] = ""
                    cctv['cyduk'][msg.to]=True 
                    settings["Sider"] = True
                    sendMessageWithFooter(msg.to,"ᴿᵉᵃᵈʸ ᶜᵉᵏ ᴼⁿ ˢᶦᵈᵉʳ...")

                elif text.lower() == 'bintit off':
                    if msg.to in cctv['point']:
                       cctv['cyduk'][msg.to]=False
                       settings["Sider"] = False
                       sendMessageWithFooter(msg.to, "ᶜᵉᵏ ˢᶦᵈᵉʳ ᴰᶦˢᵃᵇˡᵉ")
                    else:
                        sendMessageWithFooter(msg.to, "ᴮᵉˡᵘᵐ ᴰᶦˢᵉᵗ ᴰᵘᵈᵘˡ")
#==============================================================================#
                elif msg.text.lower().startswith("say-af "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'af'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
        
                elif msg.text.lower().startswith("say-sq "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sq'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ar "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ar'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-bn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'bn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ca "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ca'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-cn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-cn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-tw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-yue "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-yue'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cs "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cs'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-da "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'da'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-nl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'nl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-au "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-au'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-eo "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'eo'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-de "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'de'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-el "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'el'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hu "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hu'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-is "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'is'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-id "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-it "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'it'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ja "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-km "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'km'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ko "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ko'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-la "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'la'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-lv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'lv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-mk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'mk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-no "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'no'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pt "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pt'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-do "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ro'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ru "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ru'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-si "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'si'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ta "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ta'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-th "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-tr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'tr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-vi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'vi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
#==============================================================================# 
                elif msg.text.lower().startswith("tr-af "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='af')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sq "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sq')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-am "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='am')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ar "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-az "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='az')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-eu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='eu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-be "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='be')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ca "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ca')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ceb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ceb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ny "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ny')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-cn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-cn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-tw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-co "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='co')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-da "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='da')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-nl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='nl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-en "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-et "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='et')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ka "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ka')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-de "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-el "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='el')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ht "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ht')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ha "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ha')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-haw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='haw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-iw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='iw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hmn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hmn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-is "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='is')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ig "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ig')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-id "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ga "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ga')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-it "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='it')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ja "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-jw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='jw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-km "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='km')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ko "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ko')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ku "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ku')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ky "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ky')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-la "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='la')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ms "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ms')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ml "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ml')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-my "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='my')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ne "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ne')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-no "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='no')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ps "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ps')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ro "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ro')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ru "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ru')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sm "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sm')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-st "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='st')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-si "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='si')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-so "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='so')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-es "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='es')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-su "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='su')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ta "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ta')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-te "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='te')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ur "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ur')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uz "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uz')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-vi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='vi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-xh "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='xh')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fil "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fil')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-he "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='he')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
#==============================================================================#   
                elif text.lower().startswith("pcid"):
                	dan = text.split("|")
                	x = line.findContactsByUserid(dan[1])
                	a = line.getContact(sender)
                	sendMessageWithFooter(x.mid,"Anda mendapatkan pesan dari "+a.displayName+"\n\n"+dan[2])
                	sendMessageWithFooter(to,"Sukses mengirim pesan ke "+x.displayName+"\nDari: "+a.displayName+"\nPesan: "+dan[2])    

                elif text.lower().startswith("spaminvid"):
                	#Script Spam Invite Group via ID LINE for Python3 by Wildan (danrfq)
                	dan = text.split(" ")
                	userid = dan[1]
                	namagrup = dan[2]
                	jumlah = int(dan[3])
                	grups = line.groups
                	tgb = line.findContactsByUserid(userid)
                	line.findAndAddContactsByUserid(userid)
                	if jumlah <= 10:
                		for var in range(0,jumlah):
                			try:
                				line.createGroup(str(namagrup), [tgb.mid])
                				for i in grups:
                					grup = line.getGroup(i)
                					if grup.name == namagrup:
                						line.inviteIntoGroup(grup.id, [tgb.mid])
                						line.leaveGroup(group.id)
                				sendMentionV2(to, "@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                			except Exception as Nigga:
                				line.sendMessage(to, str(Nigga))
                	else:
                		sendMentionV2(to, "@! kebanyakan njer!!", [sender]) 

                elif text.lower().startswith("spaminvtag|"):
                	#Script Spam Invite Group via TAG for Python3 by Wildan (danrfq)
                	tgb = text.replace("spaminvtag|","")
                	key = eval(msg.contentMetadata["MENTION"])
                	mi = key["MENTIONEES"][0]["M"]
                	dan = tgb.split("|")
                	namagrup = dan[1]
                	jumlah = int(dan[2])
                	grups = line.groups
                	line.findAndAddContactsByMid(mi)
                	if jumlah <= 10:
                		for var in range(0,jumlah):
                			try:
                				line.createGroup(namagrup, [mi])
                				for i in grups:
                					grup = line.getGroup(i)
                					if grup.name == namagrup:
                						line.inviteIntoGroup(grup.id, [mi])
                						line.leaveGroup(grup.id)
                				sendMentionV2(to, "@! ѕυкѕєѕ ѕραм gяσυρ!\n\nкσявαи: @!\nנυмℓαн: {}\nиαмα gяσυρ: {}".format(jumlah, str(namagrup)), [sender, mi])
                			except Exception as Nigga:
                				line.sendMessage(to, str(Nigga))
                	else:
                		sendMentionV2(to, "@! kebanyakan njer!!", [sender])


                elif "suwidax1" in msg.text.lower():
                  if msg.toType == 2:
#                    print  ("ok")
                    _name = msg.text.replace("suwidax1","")
                    gs = line.getGroup(msg.to)
                    gs = kiker1.getGroup(msg.to)
                    gs = kiker2.getGroup(msg.to)
                    gs = kiker3.getGroup(msg.to)
                    gs = kiker4.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        line.sendMessage(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            pass
                          if not target in admin:
                            try:
                                KAC = [line,kiker1,kiker2,kiker3,kiker4]
                                kicker = random.choice(KAC)
                                kicker.kickoutFromGroup(msg.to,[target])
                                #print (msg.to,[g.mid])
                            except:
                                pass

                elif "adminadd @" in msg.text.lower():
#                  if msg._from in admin:
                   _name = msg.text.replace("adminadd @","")
                   _nametarget = _name.rstrip('  ')
                   gs = line.getGroup(msg.to)
                   gs = kiker1.getGroup(msg.to)
                   gs = kiker2.getGroup(msg.to)
                   gs = kiker3.getGroup(msg.to)
                   gs = kiker4.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                      sendMessageWithFooter(msg.to,"¢σитα¢т иσт fσυи∂")
                   else:
                      for target in targets:
                           try:
                               admin.append(target)
                               sendMessageWithFooter(msg.to,"α∂мιи ∂ιтαмвαнкαи")
                           except:
                               pass

                elif "admindel @" in msg.text.lower():
                   _name = msg.text.replace("admindel @","")
                   _nametarget = _name.rstrip('  ')
                   gs = line.getGroup(msg.to)
                   gs = kiker1.getGroup(msg.to)
                   gs = kiker2.getGroup(msg.to)
                   gs = kiker3.getGroup(msg.to)
                   gs = kiker4.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                      sendMessageWithFooter(msg.to,"¢σитα¢т иσт fσυи∂")
                   else:
                      for target in targets:
                           try:
                               admin.remove(target)
                               sendMessageWithFooter(msg.to,"α∂мιи ∂ι нαρυѕкαи")
                           except:
                               pass

                elif "adminlist" in msg.text.lower():
                 if admin == []:
                     sendMessageWithFooter(msg.to,"The stafflist is empty")
                 else:
                     sendMessageWithFooter(msg.to,"ρℓєα¢є ωαιт........")
                     mc = "||ℓιѕт α∂мιи נσfєи||\n=====================\n"
                     for mi_d in admin:
                         mc += "ѕтαff>" +line.getContact(mi_d).displayName + "\n"
                     sendMessageWithFooter(msg.to,mc)

                elif "kick" in msg.text.lower():
                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["blacklist"][target] = True 
                            line.kickoutFromGroup(msg.to,[target])
                        except:
                           kiker1.kickoutFromGroup(msg.to,[target])
                    else:
                        pass

                elif "iclik" in msg.text.lower():
                  if 'MENTION' in msg.contentMetadata.keys()!= None:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            random.choice(assist).kickoutFromGroup(msg.to,[target])
                        except:
                            pass

                elif "cikol" in msg.text.lower(): 
                       ulti0 = msg.text.replace("cikol","")
                       ulti1 = ulti0.lstrip()
                       ulti2 = ulti1.replace("@","")
                       ulti3 = ulti2.rstrip()
                       _name = ulti3
                       gs = line.getGroup(msg.to)
                       ginfo = line.getGroup(msg.to)
                       gs.preventedJoinByTicket = False
                       line.updateGroup(gs)
                       invsend = 0
                       Ticket = line.reissueGroupTicket(msg.to)
                       kiker4.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       gs.preventedJoinByTicket = True
                       line.updateGroup(gs)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessageWithFooter(msg.to,"υѕєя ∂σєѕ иσт єχιтѕ")
                           pass 
                       else:
                           for target in targets: 
                                try:
                                    kiker4.kickoutFromGroup(msg.to,[target])
                                    kiker4.leaveGroup(msg.to)
                                    #print (msg.to,[g.mid])
                                except:
                                    pass
#===============================================================
                elif text.lower() == 'oneng on': 
                       try:
                           ginfo = line.getGroup(msg.to)
                           line.inviteIntoGroup(msg.to, [Dmid])
                           sendMessageWithFooter(msg.to," done stay")
                       except:
                           pass
                elif text.lower() == 'jofstandby': 
                       try:
                           ginfo = line.getGroup(msg.to)
                           line.inviteIntoGroup(msg.to, [Amid,Bmid,Cmid,Dmid])
                           #line.inviteIntoGroup(msg.to, [Bmid])
                           #line.inviteIntoGroup(msg.to, [Cmid])
                           #line.inviteIntoGroup(msg.to, [Dmid])
                       #sendMessageWithFooter(msg.to," done stay")
                       except:
                           pass

                elif text.lower() == 'oneng in':
                    X = line.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    line.updateGroup(X)
                    invsend = 0
                    Ti = line.reissueGroupTicket(msg.to)
                    kiker4.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = line.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    kiker4.updateGroup(G)
                    Ticket = kiker3.reissueGroupTicket(msg.to)

                elif "hacked" in msg.text.lower():
                    X = line.getGroup(msg.to)
                    X.preventedJoinByTicket = False
                    line.updateGroup(X)
                    invsend = 0
                    Ti = line.reissueGroupTicket(msg.to)
                    kiker1.acceptGroupInvitationByTicket(msg.to,Ti)
                    kiker2.acceptGroupInvitationByTicket(msg.to,Ti)
                    kiker3.acceptGroupInvitationByTicket(msg.to,Ti)
                    kiker4.acceptGroupInvitationByTicket(msg.to,Ti)             
                    G = line.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    Ticket = line.reissueGroupTicket(msg.to)
#=======================================
                elif "papay" in msg.text.lower():
                    if msg.toType == 2:
                       X = line.getGroup(msg.to)
                    try:
                        kiker1.leaveGroup(msg.to)
                        kiker2.leaveGroup(msg.to)
                        kiker3.leaveGroup(msg.to)
                        kiker4.leaveGroup(msg.to)
                    except:
                         pass  

                elif "oneng out" in msg.text.lower():
                    if msg.toType == 2:
                       X = line.getGroup(msg.to)
                    try:
                        kiker4.leaveGroup(msg.to)
                    except:
                         pass

                elif text.lower().startswith("rw "):
                                try:
                                    txt = text.replace('rw ','').split('|')
                                    btype,ttype = random.choice([1,2,3,4,5]),random.choice([1,2,3,4])
                                    path = 'http://corrykalam.gq/retrowave.php?'
                                    if len(txt) == 1:
                                        params = {'text1': txt[0],'text2': '','text3': '','btype': str(btype),'ttype': str(ttype)}
                                    elif len(txt) == 2:
                                        params = {'text1': txt[0],'text2': txt[1],'text3': '','btype': str(btype),'ttype': str(ttype)}
                                    elif len(txt) == 3:
                                        params = {'text1': txt[0],'text2': txt[1],'text3': txt[2],'btype': str(btype),'ttype': str(ttype)}
                                    data = requests.get(path, params=params).json()
                                    line.sendImageWithURL(receiver, data['image'])
                                except Exception as e:
                                    line.sendMessage(receiver, str(e))  
                elif "invitegroupcall" in msg.text.lower():
                            if msg.toType == 2:
                                sep = text.split(" ")
                                strnum = text.replace(sep[0] + " ","")
                                num = int(strnum)
                                line.sendMessage(to, "вєянαѕιℓ мєиggυи∂αиg кє∂αℓαм ραиggιℓαи gяσυρ")
                                for var in range(0,num):
                                    group = line.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    line.acquireGroupCallRoute(to)
                                    line.inviteIntoGroupCall(to, contactIds=members)

                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    sendMessageWithFooter(msg.to, readTime)                 

                elif msg.text.lower().startswith("checkdate "):
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = "╔══[ D A T E ]"
                    ret_ += "\n╠ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\n╠ Age : {}".format(str(data["data"]["usia"]))
                    ret_ += "\n╠ Birthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += "\n╚══[ Success ]"
                    sendMessageWithFooter(to, str(ret_))
                elif msg.text.lower().startswith("ytmp4: "):
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                   shi = bestaudio.url
                                   me = best.url
                                   hasil = ""
                                   title = "Judul [ " + vid.title + " ]"
                                   author = '\n\n🎸 Author : ' + str(vid.author)
                                   durasi = '\n🎸Duration : ' + str(vid.duration)
                                   rating = '\n🎸Rating : ' + str(vid.rating)
                                   deskripsi = '\n🎸Deskripsi : ' + str(vid.description)
                                line.sendVideoWithURL(msg.to, me)
                                line.sendAudioWithURL(msg.to, shi)
                                line.sendMessage(msg.to,title+ author+durasi + rating+ deskripsi)
                            except Exception as e:
                                line.sendMessage(msg.to,str(e))
                elif msg.text.lower().startswith("smule: "):
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                line.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                line.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                line.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass
                elif "searchyoutube" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html5lib")
                        ret_ = "╔══[ Youtube Result ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ Total {} ]".format(len(datas))
                        sendMessageWithFooter(to, str(ret_))

                elif text.lower().startswith("joox "):
                    a = text.split(" ")
                    song = text.replace(a[0] + " ", "")
                    c = 'https://api.eater.icu/joox/' + song
                    urllib.request.urlretrieve(c,'tmp/{}.json'.format(to))
                    jooxop= codecs.open('tmp/{}.json'.format(to),"r","utf-8")
                    joox = json.load(jooxop)
                    f = '[Select Your Song] \n'
                    jum = joox["result"]
                    for num in range(len(jum)):
                        d = joox['result'][num]['artis']
                        e= joox['result'][num]['judul']
                        f += '{}. {} | By: {} \n'.format(num, e, d)
                    line.sendMessage(to, f)
                    line.sendMessage(to, "[Notice] \nType: Song [Number]")
                elif text.lower().startswith("song "):
                    a = text.split(" ")
                    num = a[1]
                    num = int(num)
                    jooxop= codecs.open('tmp/{}.json'.format(to),"r","utf-8")
                    joox = json.load(jooxop)
                    spec = joox['result'][num]['link']
                    req= requests.get(spec)
                    specs = req.text
                    spek = json.loads(specs)
                    dsa= spek['result'][0]['url']
                    pict= spek['result'][0]['img']
                    lyric = spek['result'][0]['lyric']
                    line.sendAudioWithURL(to,dsa)


            elif msg.contentType == 7:
                if settings["AddstickerTag"]["status"] == True:
                        settings["AddstickerTag"]["sid"] = msg.contentMetadata['STKID']
                        settings["AddstickerTag"]["spkg"] = msg.contentMetadata['STKPKGID']
                        sendMessageWithFooter(to, "sukses tambah sticker")
                        settings["AddstickerTag"]["status"] = False 
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    sendMessageWithFooter(to, str(ret_))

            elif msg.contentType == 1 and sender == lineMID:
                    if bc["img"] == True:
                    	path = line.downloadObjectMsg(msg_id)
                    	for gc in line.groups:
                    		sendMessageWithFooter(gc, bc["txt"])
                    		line.sendContact(gc, bc["mid"])
                    		line.sendImage(gc, path)
                    	bc["img"] = False
                    	sendMessageWithFooter(to, "Sukses broadcast ke {} grup.".format(str(len(line.groups)))) 
                    if settings["changePicture"] == True:
                        path = line.downloadObjectMsg(msg_id)
                        settings["changePicture"] = False
                        line.updateProfilePicture(path)
                        sendMessageWithFooter(to, "вєянαѕιℓ мєиgυвαн fσтσ ρяσfιℓє")
                    if settings1["changePictureProfile"]["kiker1"] == True:
                        path = line.downloadObjectMsg(msg_id)
                        settings1["changePictureProfile"]["kiker1"] = False
                        kiker1.updateProfilePicture(path)
                        sendMessageWithFooter1(to, "вєянαѕιℓ мєиgυвαн fσтσ ρяσfιℓє")
                    if settings1["changePictureProfile"]["kiker2"] == True:
                        path = kiker2.downloadObjectMsg(msg_id)
                        settings1["changePictureProfile"]["kiker2"] = False
                        kiker2.updateProfilePicture(path)
                        sendMessageWithFooter2(to, "вєянαѕιℓ мєиgυвαн fσтσ ρяσfιℓє")
                    if settings1["changePictureProfile"]["kiker3"] == True:
                        path = kiker3.downloadObjectMsg(msg_id)
                        settings1["changePictureProfile"]["kiker3"] = False
                        kiker3.updateProfilePicture(path)
                        sendMessageWithFooter3(to, "вєянαѕιℓ мєиgυвαн fσтσ ρяσfιℓє")
                    if settings1["changePictureProfile"]["kiker4"] == True:
                        path = kiker4.downloadObjectMsg(msg_id)
                        settings1["changePictureProfile"]["kiker4"] = False
                        kiker4.updateProfilePicture(path)
                        sendMessageWithFooter4(to, "вєянαѕιℓ мєиgυвαн fσтσ ρяσfιℓє")
                    if msg.toType == 2:
                        if to in settings["changeGroupPicture"]:
                            path = line.downloadObjectMsg(msg_id)
                            settings["changeGroupPicture"].remove(to)
                            line.updateGroupPicture(to, path)
                            sendMessageWithFooter(to, "вєянαѕιℓ мєиgυвαн fσтσ gяσυρ")
#==============================================================================#
        if op.type == 19:
            if mid in op.param3:
                print (" [ 19 ] KICKOUT_FROM_GROUP")
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kiker1.kickoutFromGroup(op.param1,[op.param2])
                        kiker1.inviteIntoGroup(op.param1,[op.param3])
                        line.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kiker2.kickoutFromGroup(op.param1,[op.param2])
                            kiker2.inviteIntoGroup(op.param1,[op.param3])
                            line.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kiker3.kickoutFromGroup(op.param1,[op.param2])
                                kiker3.inviteIntoGroup(op.param1,[op.param3])
                                line.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kiker4.kickoutFromGroup(op.param1,[op.param2])
                                    kiker4.inviteIntoGroup(op.param1,[op.param3])
                                    line.acceptGroupInvitation(op.param1)
                                except:
                                    pass
            if Amid in op.param3:
                print (" [ 19 ] KICKOUT_FROM_GROUP")
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kiker2.kickoutFromGroup(op.param1,[op.param2])
                        kiker2.inviteIntoGroup(op.param1,[op.param3])
                        kiker1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kiker3.kickoutFromGroup(op.param1,[op.param2])
                            kiker3.inviteIntoGroup(op.param1,[op.param3])
                            kiker1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kiker4.kickoutFromGroup(op.param1,[op.param2])
                                kiker4.inviteIntoGroup(op.param1,[op.param3])
                                kiker1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    line.kickoutFromGroup(op.param1,[op.param2])
                                    line.inviteIntoGroup(op.param1,[op.param3])
                                    kiker1.acceptGroupInvitation(op.param1)
                                except:
                                    pass
            if Bmid in op.param3:
                print (" [ 19 ] KICKOUT_FROM_GROUP")
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kiker3.kickoutFromGroup(op.param1,[op.param2])
                        kiker3.inviteIntoGroup(op.param1,[op.param3])
                        kiker2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kiker4.kickoutFromGroup(op.param1,[op.param2])
                            kiker4.inviteIntoGroup(op.param1,[op.param3])
                            kiker2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                line.kickoutFromGroup(op.param1,[op.param2])
                                line.inviteIntoGroup(op.param1,[op.param3])
                                kiker2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kiker1.kickoutFromGroup(op.param1,[op.param2])
                                    kiker1.inviteIntoGroup(op.param1,[op.param3])
                                    kiker2.acceptGroupInvitation(op.param1)
                                except:
                                    pass
            if Cmid in op.param3:
                print (" [ 19 ] KICKOUT_FROM_GROUP")
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kiker4.kickoutFromGroup(op.param1,[op.param2])
                        kiker4.inviteIntoGroup(op.param1,[op.param3])
                        kiker3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            line.inviteIntoGroup(op.param1,[op.param3])
                            kiker3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kiker1.kickoutFromGroup(op.param1,[op.param2])
                                kiker1.inviteIntoGroup(op.param1,[op.param3])
                                kiker3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kiker2.kickoutFromGroup(op.param1,[op.param2])
                                    kiker2.inviteIntoGroup(op.param1,[op.param3])
                                    kiker3.acceptGroupInvitation(op.param1)
                                except:
                                    pass
            if Dmid in op.param3:
                print (" [ 19 ] KICKOUT_FROM_GROUP")
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        line.inviteIntoGroup(op.param1,[op.param3])
                        kiker4.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kiker1.kickoutFromGroup(op.param1,[op.param2])
                            kiker1.nviteIntoGroup(op.param1,[op.param3])
                            kiker4.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kiker2.kickoutFromGroup(op.param1,[op.param2])
                                kiker2.inviteIntoGroup(op.param1,[op.param3])
                                kiker4.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kiker3.kickoutFromGroup(op.param1,[op.param2])
                                    kiker3.inviteIntoGroup(op.param1,[op.param3])
                                    kiker4.acceptGroupInvitation(op.param1)
                                except:
                                    pass
#===========[ PRO JS ]===========#
        if op.type == 19:
            print (" [ 19 ] PRO JS ")
            if mid in op.param3:
              if op.param2 not in Bots:
                  pass
              if op.param2 not in admin:
                if settings["projs"] ==  True:
                   settings["blacklist"][op.param2] = True
                   try:
                       kiker1.acceptGroupInvitation(op.param1)
                       kiker1.kickoutFromGroup(op.param1,[op.param2])
                       kiker1.findAndAddContactsByMid(op.param3)
                       kiker1.inviteIntoGroup(op.param1,[op.param3])
                       line.acceptGroupInvitation(op.param1)
                   except:
                       pass

            if mid in op.param3:
              if op.param2 not in Bots:
                  pass
              if op.param2 not in admin:
                if settings["projs"] ==  True:
                   settings["blacklist"][op.param2] = True
                   try:
                       kiker2.acceptGroupInvitation(op.param1)
                       kiker2.kickoutFromGroup(op.param1,[op.param2])
                       kiker2.findAndAddContactsByMid(op.param3)
                       kiker2.inviteIntoGroup(op.param1,[op.param3])
                       line.acceptGroupInvitation(op.param1)
                   except:
                       pass

            if mid in op.param3:
              if op.param2 not in Bots:
                  pass
              if op.param2 not in admin:
                if settings["projs"] ==  True:
                   settings["blacklist"][op.param2] = True
                   try:
                       kiker3.acceptGroupInvitation(op.param1)
                       kiker3.kickoutFromGroup(op.param1,[op.param2])
                       kiker3.findAndAddContactsByMid(op.param3)
                       kiker3.inviteIntoGroup(op.param1,[op.param3])
                       line.acceptGroupInvitation(op.param1)
                   except:
                       pass

            if mid in op.param3:
              if op.param2 not in Bots:
                  pass
              if op.param2 not in admin:
                if settings["projs"] ==  True:
                   settings["blacklist"][op.param2] = True
                   try:
                       kiker4.acceptGroupInvitation(op.param1)
                       kiker4.kickoutFromGroup(op.param1,[op.param2])
                       kiker4.findAndAddContactsByMid(op.param3)
                       kiker4.inviteIntoGroup(op.param1,[op.param3])
                       kiker4.leaveGroup(op.param1)
                       line.acceptGroupInvitation(op.param1)
                       line.inviteIntoGroup(op.param1,[Dmid])
                   except:
                       pass 

        if op.type == 32:
            print (" [ 32 ] ANTI JS")
            if Amid in op.param3:
                if op.param2 not in Bots:
                    pass
                if op.param2 not in admin:
                  if settings["projs"] == True:
                     settings["blacklist"][op.param2] = True
                     backupData()
                     try:
                         if op.param3 not in settings["blacklist"]:
                             line.kickoutFromGroup(op.param1,[op.param2])
                             line.inviteIntoGroup(op.param1,[op.param3])
                     except:
                         pass  

            if Bmid in op.param3:
                if op.param2 not in Bots:
                    pass
                if op.param2 not in admin:
                  if settings["projs"] == True:
                     settings["blacklist"][op.param2] = True
                     backupData()
                     try:
                         if op.param3 not in settings["blacklist"]:
                             line.kickoutFromGroup(op.param1,[op.param2])
                             line.inviteIntoGroup(op.param1,[op.param3])
                     except:
                         pass

            if Cmid in op.param3:
                if op.param2 not in Bots:
                    pass
                if op.param2 not in admin:
                  if settings["projs"] == True:
                     settings["blacklist"][op.param2] = True
                     backupData()
                     try:
                         if op.param3 not in settings["blacklist"]:
                             line.kickoutFromGroup(op.param1,[op.param2])
                             line.inviteIntoGroup(op.param1,[op.param3])
                     except:
                         pass

            if Dmid in op.param3:
                if op.param2 not in Bots:
                    pass
                if op.param2 not in admin:
                  if settings["projs"] == True:
                     settings["blacklist"][op.param2] = True
                     backupData()
                     try:
                         if op.param3 not in settings["blacklist"]:
                             line.kickoutFromGroup(op.param1,[op.param2])
                             line.inviteIntoGroup(op.param1,[op.param3])
                     except:
                         pass

#===================[ OP 17 ]================================================#
        if op.type == 17:
            print ("[ 17  ] JOIN KICK BL")
            if op.param2 in settings["blacklist"]:
                random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
        if op.type == 17:
            print (" [ 17 ] PRO JOIN")
            if op.param2 not in Bots:
              pass
            if op.param2 not in admin:
             if settings["projoin"] == True:
                settings["blacklist"][op.param2] = True
                try:
                    random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
                except:
                    pass
#===================[ OP 13 ]=================#
        if op.type == 13:
            print ("[ 13  ] INVIT BL")
            if op.param2 in settings["blacklist"]:
                try:
                    random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
                except:
                    pass
        if op.type == 13:
            print ("[ 13  ] CANCEL BL")
            if op.param3 in settings["blacklist"]:
                try:
                    random.choice(assist).cancelGroupInvitation(op.param1,[op.param3])
                except:
                    pass
        if op.type == 13:
            print (" [ 13 ] CANCEL INVITE")
            if op.param2 not in Bots:
              pass
            if op.param2 not in admin:
              if settings["cancelinvite"] == True:
                 settings["blacklist"][op.param2] = True
                 try:
                     random.choice(assist).cancelGroupInvitation(op.param1,[op.param3])
                 except:
                     pass
              if settings["inviteprotect"] == True:
                 settings["blacklist"][op.param2] = True
                 try:
                     random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
                     random.choice(assist).cancelGroupInvitation(op.param1,[op.param3])
                 except:
                     pass
              if settings["ghost"] == True:
               G = line.getGroup(op.param1)
               G.preventedJoinByTicket = False
               line.updateGroup(G)
               Ticket = line.reissueGroupTicket(op.param1)
               kiker4.acceptGroupInvitationByTicket(op.param1,Ticket)
               time.sleep(0.01)
               kiker4.kickoutFromGroup(op.param1,[op.param2])
               kiker4.cancelGroupInvitation(op.param1,[op.param3])
#              c = Message(to=op.param1, _from=None, text=None, contentType=13)
#              c.contentMetadata={'mid':op.param2}
#              kiker6.sendMessage(c)
               kiker4.leaveGroup(op.param1)
               G.preventedJoinByTicket = True
               line.updateGroup(G)
               settings["blacklist"][op.param2] = True
#==================[ OP 11 ]=================#
        if op.type == 11:
            print ("[ 17  ] LINk KICK BL")
            if op.param2 in settings["blacklist"]:
                G = random.choice(assist).getGroup(op.param1)
                G.preventedJoinByTicket = True
                random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
                random.choice(assist).updateGroup(G)
            else:
                pass

        if op.type == 11:
            print ("[ 11 ] LINK PROTECT")
            if op.param2 not in Bots:
              pass
            if op.param2 not in admin:
              if settings["linkprotect"] == True:
                 settings["blacklist"][op.param2] = True
                 try:
                     G = random.choice(assist).getGroup(op.param1)
                     G.preventedJoinByTicket = True
                     random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
                     random.choice(assist).updateGroup(G)
                 except:
                     pass
            if settings["ghost"] == True:
              G = line.getGroup(op.param1)
              G.preventedJoinByTicket = False
              line.updateGroup(G)
              Ticket = line.reissueGroupTicket(op.param1)
              kiker4.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kiker4.kickoutFromGroup(op.param1,[op.param2])
#              c = Message(to=op.param1, _from=None, text=None, contentType=13)
#              c.contentMetadata={'mid':op.param2}
#              kiker6.sendMessage(c)
              kiker4.leaveGroup(op.param1)
              G.preventedJoinByTicket = True
              line.updateGroup(G)
              settings["blacklist"][op.param2] = True

        if op.type == 19:
            print (" [ 19 ] PRO GROUP")
            if op.param2 not in Bots:
              pass
            if op.param2 not in admin:
             if settings["protect"] == True:
                 settings["blacklist"][op.param2] = True
                 try:
                     random.choice(assist).kickoutFromGroup(op.param1,[op.param2])
                 except:
                     pass
             if settings["ghost"] == True:
              G = line.getGroup(op.param1)
              G.preventedJoinByTicket = False
              line.updateGroup(G)
              Ticket = line.reissueGroupTicket(op.param1)
              kiker4.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              kiker4.kickoutFromGroup(op.param1,[op.param2])
#              c = Message(to=op.param1, _from=None, text=None, contentType=13)
#              c.contentMetadata={'mid':op.param2}
#              kiker6.sendMessage(c)
              kiker4.leaveGroup(op.param1)
              G.preventedJoinByTicket = True
              line.updateGroup(G)
              settings["blacklist"][op.param2] = True


        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    line.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        sendMessageWithFooter(msg.to,text)
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if lineMID in mention["M"]:
                              if settings["datectMention"] == True:
                                 sendMentionFooter(sender, settings["autoResponMessage"], [sender])
                                 break

                    if 'MENTION' in msg.contentMetadata.keys() != None:
                      if settings["datectMention2"] == True:
                          cName = line.getContact(msg._from).displayName
                          name = re.findall(r'@(\w+)', msg.text)
                          mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                          mentionees = mention['MENTIONEES']
                          for mention in mentionees:
                               if lineMID in mention["M"]:
                                  sendMessageWithFooter(msg.to, "☞ "+cName+"☜\n"+settings["autoResponMessage"])
                                  sid = str(settings["AddstickerTag"]["sid"])
                                  spkg = str(settings["AddstickerTag"]["spkg"])
                                  line.sendSticker(msg.to, spkg, sid)
                                  break                                

                elif msg.contentType == 13:
                    if settings["checkContact"] == True:
                        try:
                            contact = line.getContact(msg.contentMetadata["mid"])
                            if line != None:
                             path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                             try:
                                 line.sendImageWithURL(to, str(path))
                             except:
                                pass
                             ret_ = "╔══[ Details Contact ]"
                             ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
                             ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
                             ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
                             ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                            #ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
                             ret_ += "\n╚══[ Finish ]"
                             sendMessageWithFooter(to, str(ret_))
                        except:
                             sendMessageWithFooter(to, "Kontak tidak valid")

#==============================================================================#
        if op.type == 17:
           print ("MEMBER JOIN TO GROUP")
           if settings["Sambutan"] == True:
             if op.param2 in mid:
                 return
             ginfo = line.getGroup(op.param1)
             contact = line.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             sendMessageWithFooter(op.param1,"нι " + line.getContact(op.param2).displayName + "\nWєℓ¢σмє тσ ☞ " + str(ginfo.name) + " ☜" + "\nʝαиgαи ℓυρα ѕαℓιиg ѕαρα\n∂αи ѕємσgα вєтαн ∂ιѕιиι уα ^_^")
             line.sendImageWithURL(op.param1,image)

        if op.type == 15:
           print ("MEMBER LEAVE TO GROUP")
           if settings["Jembutan"] == True:
             if op.param2 in mid:
                 return
             ginfo = line.getGroup(op.param1)
             contact = line.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             line.sendImageWithURL(op.param1,image)
             sendMessageWithFooter(op.param1,"Gσσ∂ вує " + line.getContact(op.param2).displayName + "\nѕєє уσυ иєχт тιмє......  (p′︵‵。)")

        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if cctv['cyduk'][op.param1]==True:
                    if op.param1 in cctv['point']:
                        Name = line.getContact(op.param2).displayName
                        contact = line.getContact(op.param2)
                        image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
                        if Name in cctv['sidermem'][op.param1]:
                            pass
                        else:
                            cctv['sidermem'][op.param1] += "\n• " + Name
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    sendMessageWithFooter(op.param1, "Wᴏɪɪɪ!!!!! " + "☞ " + nick[0] + " ☜" + "\nBᴇᴛᴀʜ ᴀᴍᴀᴛ ʟᴏ ᴊᴀᴅɪ sɪᴅᴇʀ  \nᴀᴅᴀ ʏᴀɴɢ ɢᴀᴊɪ ʏ ᴊᴀᴅɪ sɪᴅᴇʀ ")
                                    line.sendImageWithURL(op.param1,image)
                                else:
                                    sendMessageWithFooter(op.param1, "Assᴀʟᴀᴍᴜᴀʟᴀɪᴋᴜᴍ " + "☞ " + nick[1] + " ☜" + "\nNɢɪɴᴛɪᴘ ᴍᴇʟᴜʟᴜ \nnᴍᴇɴᴅɪɴɢ sɪɴɪ \nᴋɪᴛᴀ ɴɢᴇʀᴜᴍᴘɪ ")
                                    line.sendImageWithURL(op.param1,image)
                            else:
                                sendMessageWithFooter(op.param1, "Nᴀʜʜʜ " + "☞ " + Name + " ☜" + "\nKᴇᴛᴀᴜᴡᴀɴ ɴɢɪɴᴛɪᴘ \nHᴀʜᴀʜᴀ ")
                                line.sendImageWithURL(op.param1,image)
                    else:
                        pass
                else:
                    pass
            except:
                pass


        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
            logError(error)

#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)

