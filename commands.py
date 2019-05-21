# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil import parser
from random import randint
from archimed import Archimed
from Naked.toolshed.shell import execute_js
from api.settings import LineHeaders
from api.services.ttypes import TalkException
import time
import random
import sys
import json
import codecs
import threading
import subprocess
import signal
import glob
import re
import string
import os
import requests
import ast
import pytz
import traceback
import importlib
import platform

Build = 1.7
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Days %02d Hours %02d Minutes' % (days, hours, mins)
def waktus(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Days %02d Hours' % (days, hours)
class beta():
    uid = None
    namen = None
    client = None
    sett = None
    awit = None
    mode = None
    app = None
    letak = None
    creator = ["u2286e272840491415e82447163dadf6c"]
    adc = False
    addajs = False
    duedate = None

    def __init__(self,uid=None,namen=None,client=None,sett=None,awit=None,mode=None,app=None,letak=None,cover=None):
        self.uid = uid
        self.namen = namen
        self.client = client
        self.set = sett
        self.awit = awit
        self.mode = mode
        self.app = app
        self.letak = letak
        self.cover = cover
        self.pro = ''
        self.tempban = []
        self.invban = []
        self.point = time.time()
        self.commands = self.set["commands"]
        self.settings = self.set["settings"]
        self.status = self.set["status"]
        self.duedate = parser.parse(self.status["duedate"])
        self.jepitan = []

    def async_notified_kickout_from_group(self,op):
                            kicker = op.param2
                            kicked = op.param3
                            kroom = op.param1
                            if self.uid == kicked:
                                if self.pangkat(kroom,kicker) > 8:
                                   self.addbl(kicker)
                            elif kroom in self.settings["protect"]:
                                if self.settings["protect"][kroom] == 0:
                                    if self.pangkat(kroom,kicker) > 8:
                                        if self.pangkat(kroom,kicked) < 9:
                                            self.addbl(kicker)

                                elif self.settings['war'] and kicked in self.status['squad']:
                                    if self.pangkat(kroom,kicker) > 8:
                                        self.addbl(kicker)
                                        try:
                                            self.client.kick_out_from_group(kroom,[kicker])
                                            self.client.invite_into_group(kroom,self.status['squad'])
                                        except TalkException as talk_error:
                                            if talk_error.code == 10:
                                                self.logError("Bot not in room {}".format(kroom))
                                            elif talk_error.code == 35:
                                                self.logError("limit")
                                                g = self.client.get_compact_group(kroom)
                                                links = g.preventedJoinByTicket
                                                if links == True:
                                                    g.preventedJoinByTicket = False
                                                    self.client.update_group(g)
                                                link = self.client.reissue_group_ticket(kroom)
                                                self.client.send_message(kicked,"%s %s"%(kroom,link))

                                elif self.pangkat(kroom,kicked) < 8 and self.pangkat(kroom,kicker) > 8:
                                        self.addbl(kicker)
                                        try:
                                            self.client.kick_out_from_group(kroom,[kicker])
                                            self.client.invite_into_group(kroom,[kicked])
                                        except TalkException as talk_error:
                                            if talk_error.code == 10:
                                                self.logError("Bot not in room {}".format(kroom))
                                            elif talk_error.code == 35:
                                              self.logError("limit")
                                              if op.param3 in self.status['squad'] or op.param3 in self.status['bot']:
                                                g = self.client.get_compact_group(kroom)
                                                links = g.preventedJoinByTicket
                                                if links == True:
                                                    g.preventedJoinByTicket = False
                                                    self.client.update_group(g)
                                                link = self.client.reissue_group_ticket(kroom)
                                                self.client.send_message(kicked,"%s %s"%(kroom,link))
                                elif self.settings["protect"][kroom] == 2 and self.pangkat(kroom,kicker) > 8:
                                    self.addbl(kicker)
                                    self.client.kick_out_from_group(kroom, [kicker])

    def async_notified_invite_into_group(self,op):
                            grup = op.param1
                            inviter = op.param2
                            invites = op.param3.split('\x1e')
                            if self.uid in op.param3:
                                if self.pangkat(grup,inviter) < 7:
                                    self.client.accept_group_invitation(grup)
                                    if inviter in self.status['anti']:
                                       self.settings['protect'][grup] = 2
                                       self.backupData()

                                    elif self.settings['nuke']:
                                        x = self.client.get_compact_group(grup)
                                        nama = [contact.mid for contact in x.members]
                                        targets = []
                                        for a in nama:
                                            if self.pangkat(grup,a) > 8 and a != self.uid:
                                                targets.append(a)
                                        if targets == []:
                                            pass
                                        else:
                                            cms = '/root/crash/simple.js gid={} token={} app={}'.format(grup,self.client.authToken,self.app)
                                            for y in targets:
                                                cms += ' uid={}'.format(y)
                                            success = execute_js(cms)
                                            if success:
                                                self.client.send_message(inviter,'Execute success')
                                            else:
                                                self.client.send_message(inviter,'error')
                            elif grup in self.settings["protect"]:
                                if self.settings["protect"][grup] > 0:
                                    if not set(self.status['blacklist']).isdisjoint(invites):
                                        band = set(self.status['blacklist']).intersection(invites)
                                        for c in band:
                                            self.client.cancel_group_invitation(grup,[c])
                                        if self.pangkat(grup,inviter) > 8:
                                            self.addbl(inviter)
                                            self.client.kick_out_from_group(grup,[inviter])

                                    elif inviter in self.status['blacklist']:
                                        self.client.kick_out_from_group(grup,[inviter])
                                        self.invban = invites
                                        for target in invites:
                                            self.client.cancel_group_invitation(grup,[target])
                                    elif grup in self.settings['cancel']:
                                        if self.pangkat(grup,inviter) > 8:
                                            self.invban = invites
                                            for target in invites:
                                                self.client.cancel_group_invitation(grup,[target])
                                            if self.settings['cancel'][grup] == 2:
                                                self.addbl(inviter)
                                                self.client.kick_out_from_group(grup,[inviter])

    def async_notified_accept_group_invitation(self,op):
                            if op.param1 in self.settings["protect"]:
                              if self.settings["protect"][op.param1] > 0:
                                if op.param2 in self.status['blacklist']:
                                    if self.settings['lock']:
                                      if self.tempban != []: 
                                        group = self.client.get_group(op.param1)
                                        members = [o.mid for o in group.members]
                                        matched_list = []
                                        matched_list.append(op.param2)
                                        for tag in self.tempban:
                                            matched_list+=filter(lambda str: str == tag, members)
                                        if group.preventedJoinByTicket == False:
                                            group.preventedJoinByTicket = True
                                            self.client.update_group(group)
                                        for c in matched_list:
                                            self.client.kick_out_from_group(op.param1,[c])
                                      else:self.client.kick_out_from_group(op.param1,[op.param2])
                                    else:self.client.kick_out_from_group(op.param1,[op.param2])
                                elif op.param2 in self.invban and self.pangkat(op.param1,op.param2) > 8:
                                       self.client.kick_out_from_group(op.param1,[op.param2])
                                       self.invban.remove(op.param2)
                                elif op.param1 in self.settings['blj'] and self.pangkat(op.param1,op.param2) > 8:
                                       self.client.kick_out_from_group(op.param1,[op.param2])
    def async_notified_cancel_invitation_group(self,op):
                              if op.param3 != self.uid and self.pangkat(op.param1,op.param2) > 8:
                                if op.param1 in self.settings['protect']:
                                    if self.pangkat(op.param1,op.param3) < 8 and self.settings['protect'][op.param1] > 0:
                                        self.addbl(op.param2)
                                        self.client.invite_into_group(op.param1,[op.param3])
                                        self.client.kick_out_from_group(op.param1, [op.param2])
                                    elif self.settings['protect'][op.param1] == 2:
                                        self.addbl(op.param2)
                                        self.client.kick_out_from_group(op.param1, [op.param2])
    def async_notified_update_group(self,op):
                                    if op.param3 == '1':
                                        if op.param1 in self.settings['namelock'] and self.pangkat(op.param1,op.param2) > 8:
                                            cek = self.client.get_compact_group(op.param1)
                                            cek.name = self.settings['namelock'][op.param1]
                                            self.client.update_group(cek)
                                            if op.param1 in self.settings['protect'] and self.settings['protect'][op.param1] > 1:
                                                self.client.kick_out_from_group(op.param1,[op.param2])
                                                self.addbl(op.param2)
                                    else:
                                        if op.param1 in self.settings['linkprotect'] and self.pangkat(op.param1,op.param2) > 8:
                                                cek = self.client.get_compact_group(op.param1)
                                                if cek.preventedJoinByTicket == False:
                                                    cek.preventedJoinByTicket = True
                                                    self.client.update_group(cek)
                                                    if self.settings['linkprotect'][op.param1] == 2:
                                                        self.addbl(op.param2)
                                                        self.client.kick_out_from_group(op.param1,[op.param2])
                                        elif op.param1 in self.settings["protect"]:
                                          if self.settings["protect"][op.param1] > 0:
                                            if op.param2 in self.status['blacklist']:
                                                cek = self.client.get_compact_group(op.param1)
                                                if cek.preventedJoinByTicket == False:
                                                    cek.preventedJoinByTicket = True
                                                    self.client.update_group(cek)
                                                    if op.param1 in self.settings['protect'] and self.settings['protect'][op.param1] > 0:
                                                        self.client.kick_out_from_group(op.param1,[op.param2])

                                            elif self.settings['lock']:
                                                if op.param2 not in self.tempban and self.pangkat(op.param1,op.param2) > 8:
                                                    self.tempban.append(op.param2)
    def async_notified_read_message(self,op):
                            if op.param2 in self.status['blacklist'] and op.param1 in self.settings['protect']:
                                if self.settings['protect'][op.param1] > 0:
                                   self.client.kick_out_from_group(op.param1,[op.param2])
    def async_notified_leave_group(self,op):
                            if op.param2 in self.status['anti'] and op.param1 in self.settings['protect']:
                                if self.settings['protect'][op.param1] > 0:
                                    self.client.invite_into_group(op.param1, [op.param2])
    def async_accept_group_invitation(self,op):
                            if op.param1 not in self.settings['protect']:
                                self.settings['protect'][op.param1] = 0
                            if self.settings["purge"]:
                                group = self.client.get_group(op.param1)
                                members = [o.mid for o in group.members]
                                if not set(members).isdisjoint(self.status["blacklist"]):
                                    band = set(members).intersection(self.status["blacklist"])
                                    for ban in band:
                                        self.client.kick_out_from_group(op.param1,[ban])
    def async_auto(self):
        if self.invban != [] or self.tempban != []:
            if time.time() - self.point >= 60:
                self.invban = []
                self.tempban = []
                self.point = time.time()
    def pangkat(self, room, userr):
        u = self.creator
        if userr in u:
            return 0
        u = self.status['owner']
        if userr in u:
            return 1
        u = self.status['admin']
        if userr in u:
            return 2
        u = self.status['staff']
        if userr in u:
            return 3
        u = self.status['squad']
        if userr in u:
            return 4
        u = self.status['bot']
        if userr in u:
            return 5
        u = self.status['anti']
        if userr in u:
            return 6
        if room in self.status['gaccess']:
            self.access = self.status['gaccess'][room]
            u = self.access['gowner']
            if userr in u:
                return 7
            u = self.access['gadmin']
            if userr in u:
                return 8
        return 1000

    def addbl(self, user):
        if user in self.status['blacklist'] or not self.settings['allowban']:
            pass
        else:
            self.status['blacklist'].append(user)
            self.backupData()
        return 1
    def mention(self,msg,targets):
        if msg.mentionees:
            for mention in msg.mentionees:
                targets.append(mention)
    def backupData(self):
        with open('{}peki/{}.json'.format(self.letak,self.namen), 'w') as fp:
            json.dump(self.set, fp, sort_keys=True, indent=4)
    def sendtag(self, to, text="",eto="", mids=[], isUnicode=False):
        arrData = ""
        arr = []
        mention = "@Alen OupTz "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ""
            unicode = ""
            if isUnicode:
                for mid in mids:
                    unicode += str(texts[mids.index(mid)].encode('unicode-escape'))
                    textx += str(texts[mids.index(mid)])
                    slen = len(textx) if unicode == textx else len(textx) + unicode.count('U0')
                    elen = len(textx) + 15
                    arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
                    arr.append(arrData)
                    textx += mention
            else:
                for mid in mids:
                    textx += str(texts[mids.index(mid)])
                    slen = len(textx)
                    elen = len(textx) + 15
                    arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
                    arr.append(arrData)
                    textx += mention
            textx += str(texts[len(mids)])
        else:
            raise Exception("Invalid mention position")
        self.client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

    def mycmd(self,text,wait,msg):
        cmd = ''
        pesan = text
        if msg.from_id in wait['cname']:
            rname =  wait['cname'][msg.from_id]
        else:rname = wait['rname']
        if msg.from_id in wait['dname']:
            sname =  wait['dname'][msg.from_id]
        else:sname = wait['sname']
        if pesan.lower().startswith(rname):
                if ' & ' in text:
                    cmd = pesan.split(' & ')
                else:
                    cmd = [pesan]
        elif pesan.lower().startswith(sname):
                if ' & ' in text:
                    cmd = pesan.split(' & ')
                else:
                    cmd = [pesan]
        elif pesan.lower().startswith("oup"):
                if ' & ' in text:
                    cmd = pesan.split(' & ')
                else:
                    cmd = [pesan]
        return cmd

    def abort(self,to,silent):
        self.status["repeat"] = False
        if self.status["abl"]:
            self.status["abl"] = False
        if self.status["invite"]:
            self.status["invite"] = False
        if self.status["abot"]:
            self.status["abot"] = False
        if self.status["aadmin"]:
            self.status["aadmin"] = False
        if self.status["expel"]:
            self.status["expel"] = False
        if self.status["astaff"]:
            self.status["astaff"] = False
        if self.status['picture']:
            self.status["picture"] = False
        if self.status['cvp']:
            self.status["cvp"] = False
        self.addajs = False
        self.backupData()
        if not silent:self.client.send_message(to,"Command done")

    def listdata(self,to,status,text='',ps='',data=[]):
        k = len(data)//20
        for aa in range(k+1):
            if aa == 0:dd = '   ✨ {} ✨'.format(text,ps);no=aa
            else:dd = '   ✨ {} ✨'.format(text,ps);no=aa*20
            msgas = dd
            for i in data[aa*20 : (aa+1)*20]:
                no+=1
                if no == len(data):msgas+='\n{}. @!'.format(no)
                else:msgas+='\n{}. @!'.format(no)
            if data == []:pass
            else:self.sendtag(to, msgas,' ✨ {} ✨'.format(ps), data[aa*20: (aa+1)*20])
    def logError(self,text):
      try:
        print('ERROR')
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
        with open("{}log/e{}".format(self.letak,self.namen),"a") as error:
            error.write("\n[ {} ] {}".format(str(time), text))
      except Exception as e:
        traceback.print_exc()
    def ranking(self, room, userr):
        u = self.creator
        if userr in u:
            return 0
        u = self.status['owner']
        if userr in u:
            return 1
        u = self.status['admin']
        if userr in u:
            return 2
        u = self.status['staff']
        if userr in u:
            return 3
        if room in self.status['gaccess']:
            self.access = self.status['gaccess'][room]
            u = self.access['gowner']
            if userr in u:
                return 4
            u = self.access['gadmin']
            if userr in u:
                return 5
        return 1000
    def listcon(self,to,msg,num,status,data=[]):
        if data == []:
            self.client.send_message(to, " ✨ Empty List ✨")
        else:
                    nama = data
                    no = 0
                    targets = []
                    selection = Archimed(num,range(1,len(nama)+1))
                    for i in selection.parse():
                        targets.append(nama[i-1])
                    for target in targets:
                          try:
                              self.client.send_contact(msg.to_id,target)
                          except Exception as e:traceback.print_exc()

    def mentionmention(self,to,status, text, dataMid=[], pl='', ps='',pg='',pt=[],silent=False):
        arr = []
        list_text=ps
        i=0
        no=pl
        if pg == 'MENTIONALLME':
            for l in dataMid:
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text+text
        if pg == 'DELFL':
            for l in dataMid:
                try:
                    self.client.delcon(l)
                    a = 'Del Friend'
                except:
                    a = 'Not Friend User'
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=text+list_text
        if pg == 'ADDFL':
            lss = self.client.refreshContacts()
            for l in dataMid:
                if not l in self.uid and l not in lss:
                   self.client.add_contact_by_mid(l)
                no+=1
                list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'ADDWL':
            for l in dataMid:
              if not l in self.uid:
                if l in status["bot"]:
                    a = 'whitelist'
                else:
                    if l not in status["blacklist"]:
                        a = 'whitelist'
                        status["bot"].append(l)
                        self.client.add_contact_by_mid(l)
                    else:
                        a = 'BL User'
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'ADDST':
            for l in dataMid:
              if not l in self.uid:
                if l in status["staff"]:
                    a = 'Already Staff'
                else:
                    a = 'Add staff'
                    status["staff"].append(l)
                    self.client.add_contact_by_mid(l)
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'DELST':
            for l in dataMid:
                if l not in status["staff"]:
                    a = 'Not staff'
                else:
                    a = 'DEL staff'
                    status["staff"].remove(l)
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'ADDGO':
            for l in dataMid:
              if not l in self.uid:
                if to in status['gaccess']:
                        if l in status['gaccess'][to]["gowner"]:
                            a = 'Already Gowner'
                        else:
                            a = 'Add Gowner'
                            status['gaccess'][to]["gowner"].append(l)
                            self.client.add_contact_by_mid(l)
                else:
                    status['gaccess'][to] = {'gowner':[],'gadmin':[]}
                    a = 'Add Gowner'
                    status['gaccess'][to]["gowner"].append(l)
                    self.client.add_contact_by_mid(l)
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'DELGO':
            for l in dataMid:
                if to in status['gaccess']:
                        if l in status['gaccess'][to]["gowner"]:
                            a = 'Del Gowner'
                            status['gaccess'][to]["gowner"].remove(l)
                else:
                    pass
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'ADDGA':
            for l in dataMid:
              if not l in self.uid:
                if to in status['gaccess']:
                        if l in status['gaccess'][to]["gadmin"]:
                            a = 'Already Gowner'
                        else:
                            a = 'Add Gowner'
                            status['gaccess'][to]["gadmin"].append(l)
                            self.client.add_contact_by_mid(l)
                else:
                    status['gaccess'][to] = {'gowner':[],'gadmin':[]}
                    a = 'Add GAdmin'
                    status['gaccess'][to]["gadmin"].append(l)
                    self.client.add_contact_by_mid(l)
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'DELGA':
            for l in dataMid:
                if to in status['gaccess']:
                        if l in status['gaccess'][to]["gadmin"]:
                            a = 'Del Gowner'
                            status['gaccess'][to]["gadmin"].remove(l)
                else:
                    pass
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'ADDBO':
            for l in dataMid:
              if not l in self.uid:
                if l in status["squad"]:
                    a = 'Already Warlist'
                else:
                    a = 'Warlist added'
                    status["squad"].append(l)
                    status["bot"].append(l)
                    self.client.add_contact_by_mid(l)
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'DELBO':
            for l in dataMid:
                if l not in status["squad"]:
                    a = 'Not Warlist'
                else:
                    a = 'DEL Warlist'
                    status["squad"].remove(l)
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'ADDBK':
            for l in dataMid:
              if not l in self.uid:
                if l in status["anti"]:
                    a = 'Already Bolo'
                else:
                    a = 'Add squad'
                    status["anti"].append(l)
                    self.client.add_contact_by_mid(l)
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'ADDC':
            for l in dataMid:
              if not l in self.uid:
                a = 'Add Con'
                self.client.add_contact_by_mid(l)
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'ADDADM':
            for l in dataMid:
              if not l in self.uid:
                if l in status["admin"]:
                    a = 'Already Admin'
                else:
                    a = 'Add Admin'
                    status["admin"].append(l)
                    self.client.add_contact_by_mid(l)
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'DELADM':
            for l in dataMid:
                if l not in status["admin"]:
                    a = 'Not Admin'
                else:
                    a = 'DEL Admin'
                    status["admin"].remove(l)
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'ADDOWN':

            for l in dataMid:
                if l in status["owner"]:
                    a = 'Sampun Owner'
                else:
                    a = 'Add Owner'
                    status["owner"].append(l)
                    self.client.add_contact_by_mid(l)
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'DELOWN':
            for l in dataMid:
                if l not in status["owner"]:
                    a = 'Not Owner'
                else:
                    a = 'DEL Owner'
                    status["owner"].remove(l)
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=list_text
        if pg == 'ADDBL':
            for l in dataMid:
                if l in status["bot"]:
                    a = 'Bot access'
                else:
                    if l not in status["blacklist"]:
                        a = 'Add BL'
                        status["blacklist"].append(l)
                    else:
                        a = 'BL User'
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=text+list_text
        if pg == 'DELWL':
            for l in dataMid:
                try:
                    status["bot"].remove(l)
                    a = 'Del Bot'
                except:
                    a = 'Not whitelist'
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=text+list_text
        if pg == 'DELBL':
            for l in dataMid:
                try:
                    status["blacklist"].remove(l)
                    a = 'Del BL'
                except:
                    a = 'Not BL User'
                no+=1
                if no == len(pt):list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                else:list_text+='\n'+str(no)+'. @[oup-'+str(i)+'] '
                i=i+1
            text=text+list_text
        i=0
        for l in dataMid:
          if l not in self.uid:
            mid=l
            name='@[oup-'+str(i)+']'
            ln_text=text.replace('\n',' ')
            if ln_text.find(name):
                line_s=int( ln_text.index(name) )
                line_e=(int(line_s)+int( len(name) ))
            arrData={'S': str(line_s), 'E': str(line_e), 'M': mid}
            arr.append(arrData)
            i=i+1
        if not silent:self.client.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    def cleartemp(self,to):
                        gid = self.client.get_joined_group_mids()
                        al = []
                        bl = []
                        cf = []
                        dl = []
                        el = []
                        for a in self.settings["cancel"]:
                            if a not in gid:
                                al.append(a)
                        for b in self.settings["protect"]:
                            if b not in gid:
                                bl.append(b)
                        for c in self.settings["linkprotect"]:
                            if c not in gid:
                                cf.append(c)
                        for d in self.settings["namelock"]:
                            if d not in gid:
                                dl.append(d)
                        for e in self.settings["blj"]:
                            if e not in gid:
                                el.append(e)
                        for z in al:
                            del self.settings["cancel"][z]
                        for z in bl:
                            del self.settings["protect"][z]
                        for z in cf:
                            del self.settings["linkprotect"][z]
                        for z in dl:
                            del self.settings["namelock"][z]
                        for z in el:
                            del self.settings["blj"][z]

    def async_receive_message(self,op):
      try:
        msg = op.message
        to = msg.to_id
        saya = msg.from_id
        text = msg.text
        if self.settings["mute"]:
           silent = self.settings["mute"]
        else:silent = False
        if msg.from_id in self.settings['cname']:
            rname =  self.settings['cname'][msg.from_id].lower() + " "
        else:rname = self.settings['rname'].lower() + " "
        if msg.from_id in self.settings['dname']:
            sname =  self.settings['dname'][msg.from_id].lower() + " "
        else:sname = self.settings['sname'].lower() + " "
        if msg.content_type == 0:
                if None == msg.text:
                   return
                if msg.to_type == 0:
                    to = msg.from_id
                    if self.pangkat(to,saya) < 6:
                        if text.startswith(rname + 'kick '):
                                regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = regex.findall(text)
                                tickets = []
                                gids = self.client.get_joined_group_mids()
                                for link in links:
                                    if link not in tickets:
                                        tickets.append(link)
                                for ticket in tickets:
                                    try:
                                        group = self.client.get_group_by_ticket(ticket)
                                    except:
                                        continue
                                    if group.id in gids:
                                        continue
                                    x = self.client.get_group(group.id)
                                    nama = [contact.mid for contact in x.members]
                                    targets = []
                                    for a in nama:
                                            if self.pangkat(to,a) > 4 and a != self.uid:
                                                targets.append(a)
                                    if targets == []:
                                            self.client.send_message(to,"Target not found.")
                                    else:
                                            cms = '/root/crash/simple.js gid={} token={} app={}'.format(group.id,self.client.authToken,self.app)
                                            for y in targets:
                                                cms += ' uid={}'.format(y)
                                            self.client.accept_group_invitation_by_ticket(group.id, ticket)
                                            print(cms)
                                            success = execute_js(cms)
                                            if success:
                                                self.client.send_message(to,'Execute success')
                                            else:
                                                self.client.send_message(to,'error')

                        elif not rname in text.lower():
                            cond = text.split(" ")
                            if len(cond) == 2:
                               gid = msg.text.split()[0]
                               link = msg.text.split()[1]
                               gids = self.client.get_joined_group_mids()
                               if gid not in gids:
                                  self.client.accept_group_invitation_by_ticket(gid,link)

                txt = msg.text.lower()
                txt = " ".join(txt.split())
                if ".silent" in txt:
                    silent = True
                    txt = txt.replace(".silent","")
                    txt = " ".join(txt.split())
                if txt.startswith(rname) or txt.startswith(sname) or txt.startswith('oup '):
                   cmds = self.mycmd(txt,self.settings,msg)
                else:cmds=[]
                if self.pangkat(to,saya) == 0:
                  for a in cmds:
                    if a.startswith(rname):txt = a.replace(a[:len(rname)],'')
                    elif a.startswith(sname):txt = a.replace(a[:len(sname)],'')
                    elif a.startswith("oup"):txt = a.replace(a[:len("oup")]+' ','')
                    elif cmds.index(a) != 0 and rname not in a and sname not in a:txt = a
                    if txt == 'bot reset':
                        self.settings = {'nuke':False,'atjoin':True,'blj':{},'reb': '','cancel':{},'cname':{},'dname':{},'rname': self.namen,'sname':'default','squad':'B£∆CK_∆NG€£','protect':{},'namelock':{'on':1,'nama':''},'allowban':True,'spam':{},'ant':False,'lock':False,'mute':False,'antimode':False,'purge':False,'war': False,'mode1': False,'linkprotect':{},'kick':{}}
                        self.status = {'start':time.time(), 'ban':False, 'invite':False,'unban':False,'abot':False,'aadmin':False,'aowner':False,'expel':False,\
                                       'repeat':False,'astaff':False,'abl':False,'owner':[],'squad':[],'backup':{'all':[]},'admin':[],'gaccess': {},'wordban':[],'staff':[],'anti':[],\
                                       'bot':[],'squad':[],'blacklist':[],'picture':{},'cvp': False,'gpic':{'pic': '','vid': ''},'duedate':str(datetime.now()+relativedelta(months=1))}
                        self.backupData()
                        if not silent:self.client.send_message(to, "Bot reseted.")
                    if txt.startswith("date "):
                        date = txt.split(' ')[1]
                        self.duedate = parser.parse(date)
                        self.status["duedate"] = str(self.duedate)
                        self.backupData()
                        if not silent:self.client.send_message(to,"Duedate set to %s."%self.duedate)
                    if txt == 'reboot':
                                        self.settings["reb"] = to
                                        self.backupData()
                                        if not silent:self.client.send_message(to,"Restarting bot system...")
                                        python3 = sys.executable
                                        os.execl(python3, python3, *sys.argv)

                    if txt == "addmonth":
                        self.duedate = self.duedate + relativedelta(months=1)
                        self.status["duedate"] = str(self.duedate)
                        self.backupData()
                        if not silent:self.client.send_message(to,"Time has been extended with 1 month")
                    if txt == "decmonth":
                        self.duedate = self.duedate - relativedelta(months=1)
                        self.status["duedate"] = str(self.duedate)
                        self.backupData()
                        if not silent:self.client.send_message(to,"Time has been deducted with 1 month.")
                    if txt == "addweek":
                        self.duedate = self.duedate + relativedelta(weeks=1)
                        self.status["duedate"] = str(self.duedate)
                        self.backupData()
                        if not silent:self.client.send_message(to,"Time has been extended with 1 week.")
                    if txt == "decweek":
                        self.duedate = self.duedate - relativedelta(weeks=1)
                        self.status["duedate"] = str(self.duedate)
                        self.backupData()
                        if not silent:self.client.send_message(to,"Time has been decrased 1 week.")
                    if txt == "addday":
                        self.duedate = self.duedate + relativedelta(days=1)
                        self.status["duedate"] = str(self.duedate)
                        self.backupData()
                        if not silent:self.client.send_message(to,"Time has been extended with with 1 day.")
                    if txt == "decday":
                        self.duedate = self.duedate - relativedelta(days=1)
                        self.status["duedate"] = str(self.duedate)
                        self.backupData()
                        if not silent:self.client.send_message(to,"Time has been deducted with with 1 day.")
                    if txt == "logs":
                                a=subprocess.getoutput('cat {}log/e{}'.format(self.letak,self.namen))
                                k = len(a)//10000
                                for aa in range(k+1):
                                    if not silent:self.client.send_message(to,'{}'.format(a[aa*10000 : (aa+1)*10000]))
                                try:
                                   os.remove('{}log/e{}'.format(self.letak,self.namen))
                                except:pass
                    if txt == "clear logs":
                                try:
                                   os.remove('log/e{}'.format(self.namen))
                                   if not silent:self.client.send_message(to,'Done.')
                                except:
                                   if not silent:self.client.send_message(to,'Logs is empty.') 
                    if txt.startswith("add owner"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        for target in targets:
                            if target in self.status["staff"]:
                               self.status["staff"].remove(target)
                            if target in self.status["bot"]:
                               self.status["bot"].remove(target)
                            if target in self.status["admin"]:
                               self.status["admin"].remove(target)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Owner Add ✨\n',pg='ADDOWN',pt=targets,silent=silent)
                      else:
                        self.status["aowner"] = True
                        if not silent:self.client.send_message(to,"Send contact.")
                      self.backupData()

                    if txt.startswith("del owner"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Del Owner ✨\n',pg='DELOWN',pt=targets,silent=silent)
                      else:
                        data = txt.replace("del owner","")
                        text = data.split(' ')
                        com = str(text[1])
                        selection = Archimed(com,range(1,len(self.status['owner'])+1))
                        k = len(self.status['owner'])//100
                        d = []
                        for c in selection.parse():
                            d.append(self.status['owner'][int(c)-1])
                        for a in range(k+1):
                            if a == 0:self.mentionmention(to=to,status=self.status,text='',dataMid=d[:100],pl=-0,ps='   ✨ Del Owner ✨\n',pg='DELOWN',pt=d,silent=silent)
                            else:self.mentionmention(to=to,status=self.status,text='',dataMid=d[a*100 : (a+1)*100],pl=a*100,ps='   ✨ Del Owner ✨\n',pg='DELOWN',pt=d,silent=silent)
                      self.backupData()

                if self.pangkat(to,saya) < 2:
                  if txt == 'radisti'.lower() or \
                                txt == rname.replace(" ","").lower() or \
                                txt == sname.replace(" ","").lower():
                                if not silent:self.sendtag(to,"Hola @! ",rname, [saya])
                  
                  if msg.text.lower().startswith(rname + "squad: ") or msg.text.lower().startswith(sname + "squad: ") or txt.startswith("default squad: "):
                            sep = msg.text.lower().split(": ")
                            self.settings["sname"] = sep[1]
                            self.backupData()
                            if not silent:self.client.send_message(to,"Squad response changed to " +self.settings["sname"])

                  if msg.text.lower().startswith(rname+"r,"):
                        if not "r, " in msg.text.lower():
                            number = msg.text.lower().split("r,")[1]
                            number = number.split()[0]
                            num = int(number)
                            gid = self.client.get_joined_group_mids()
                            sumi = gid[num-1]
                            group = sumi
                            to = group
                            if not " & " in msg.text.lower():
                               z = msg.text.lower().replace(rname+"r,%s "%number,"").lstrip().rstrip()
                               cmds = [z]
                               if not silent:self.client.send_message(msg.to_id,"Command '%s' sent to group %s."%(z.replace(rname,""),self.client.get_group(group).name))
                            else:
                               z = msg.text.lower().replace(rname+"r,%s "%number,"").lstrip().rstrip()
                               cmds = z.split(" & ")
                               if not silent:self.client.send_message(msg.to_id,"Multi Command '%s' sent to group %s."%(z.replace(rname,""),self.client.get_group(group).name))

                  if msg.text.lower().startswith(sname+"r,"):
                        if not "r, " in msg.text.lower():
                            number = msg.text.lower().split("r,")[1]
                            number = number.split()[0]
                            num = int(number)
                            gid = self.client.get_joined_group_mids()
                            sumi = gid[num-1]
                            group = sumi
                            to = group
                            if not " & " in msg.text.lower():
                               z = msg.text.lower().replace(sname+"r,%s "%number,"").lstrip().rstrip()
                               cmds = [z]
                            else:
                               z = msg.text.lower().replace(sname+"r,%s "%number,"").lstrip().rstrip()
                               cmds = z.split(" & ")
                            if not silent:self.client.send_message(msg.to_id,"Command '%s' sent to group %s."%(msg.text[len(rname)-1:].lstrip(),self.client.get_group(group).name))
                  for a in cmds:
                    if a.startswith(rname):txt = a.replace(a[:len(rname)],'')
                    elif a.startswith(sname):txt = a.replace(a[:len(sname)],'')
                    elif a.startswith("oup"):txt = a.replace(a[:len("oup")]+' ','')
                    elif cmds.index(a) != 0 and rname not in a and sname not in a:txt = a
                    if txt == "shutdown":
                            if not silent:self.client.send_message(msg.to_id,"Bot will shuting down...")
                            self.backupData()
                            time.sleep(3)
                            sys.exit('Sayonara')

                    if txt == '.nuker mode':
                        self.settings['nuke'] = True
                        self.backupData()
                        if not silent:self.client.send_message(msg.to_id,"Nuke mode enabled.")
                    if txt == '.nuker off':
                        self.settings['nuke'] = False
                        self.backupData()
                        if not silent:self.client.send_message(msg.to_id,"Nuke mode disabled.")

                    if txt == 'clear all protect':
                        self.settings["cancel"] = {}
                        self.settings["linkprotect"] = {}
                        self.settings["protect"] = {}
                        self.settings["namelock"] = {}
                        self.settings["blj"] = {}
                        self.settings["purge"] = False
                        self.settings["lock"] = False
                        self.settings["war"] = False
                        self.backupData()
                        if not silent:self.client.send_message(msg.to_id, "All protection cleared.")
                    if txt == 'autopurge on':
                        if self.settings["purge"] :
                            if not silent:self.client.send_message(msg.to_id, "Auto purge already enabled.")
                        else:
                            self.settings["purge"] = True
                            self.backupData()
                            if not silent:self.client.send_message(msg.to_id, "Purge mode enabled.")
                    if txt == 'autopurge off':
                        if self.settings["purge"] :
                            self.settings["purge"] = False
                            self.backupData()
                            if not silent:self.client.send_message(msg.to_id, "Auto purge disabled.")
                        else:
                            if not silent:self.client.send_message(msg.to_id, "Auto purge already disabled.")

                    if txt == 'urljoin off':
                        if self.settings["atjoin"]:
                            self.settings["atjoin"] = False
                            self.backupData()
                            if not silent:self.client.send_message(msg.to_id, "Url join disabled.")
                        else:
                            if not silent:self.client.send_message(msg.to_id, "Urljoin already disabled.")
                    if txt == 'urljoin on':
                        if self.settings["atjoin"]:
                            if not silent:self.client.send_message(msg.to_id, "Url join already enabled.")
                        else:
                            self.settings["atjoin"] = True
                            self.backupData()
                            if not silent:self.client.send_message(msg.to_id, "Url join enabled.")
                    if txt == 'lock on':
                        if self.settings["lock"] :
                            if not silent:self.client.send_message(msg.to_id, "Lock mode already enabled.")
                        else:
                            self.settings["lock"] = True
                            self.backupData()
                            if not silent:self.client.send_message(msg.to_id, "Lock mode enabled.")
                    if txt == 'lock off':
                        if self.settings["lock"] :
                            self.settings["lock"] = False
                            self.backupData()
                            if not silent:self.client.send_message(msg.to_id, "Auto lock disabled.")
                        else:
                            if not silent:self.client.send_message(msg.to_id, "Auto lock already disabled.")
                    if txt == 'war off':
                      if self.mode == 1:
                        if not self.settings["war"]:
                            if not silent:self.client.send_message(msg.to_id, "Already in normal mode.")
                        else:
                            self.settings["war"] = False
                            self.backupData()
                            if not silent:self.client.send_message(msg.to_id, "switched to normal mode.")
                    if txt == 'war on':
                      if self.mode == 1:
                        if self.settings["war"]:
                            if not silent:self.client.send_message(msg.to_id, "Already in war mode.")
                        else:
                            self.settings["war"] = True
                            self.backupData()
                            if not silent:self.client.send_message(msg.to_id, "switched to war mode.")

                    if txt == "duedate":
                        duedate = str(self.duedate).split()[0]
                        if not silent:self.client.send_message(to,duedate)

                    if txt == "timeleft":
                        timeleft = self.duedate - datetime.now()
                        days, seconds = timeleft.days, timeleft.seconds
                        hours = seconds / 3600
                        minutes = (seconds / 60) % 60
                        harto = "Time to due: %s Days, %s Hours, %s Minutes"%(days,round(hours),round(minutes))
                        if not silent:self.client.send_message(to,harto)

                    if txt == 'gettime':
                        t = time.time()*1000-int(op.createdTime)
                        backfire = 0.0
                        if(t < 30):
                            t = t/3
                            backfire = random.randint(1,5)
                        elif( t < 60):
                            t= t/6
                            backfire = random.randint(6,9)
                        else:
                            t = t/8
                            backfire = random.randint(0,9)
                        t = int(t)
                        t = t+(backfire/10.0)
                        if not silent:self.client.send_message(to,"%s"%t)
                    if txt == 'bot:room':
                       Data = self.status["bot"]
                       a = []
                       b = self.client.get_group(to)
                       lss = self.client.refreshContacts()
                       for i in b.members:
                        if i.mid not in Data and i.mid not in self.uid and self.pangkat(to,i.mid) > 6:
                            Data.append(i.mid)
                            a.append(i.mid)
                            if i.mid not in lss:
                               self.client.add_contact_by_mid(i.mid)
                            time.sleep(0.02)
                       if a == []:
                          if not silent:self.client.send_message(to,"Nothing to added.")
                       else:self.listdata(to,self.status,'Add whitelist','bot',a)
                       self.backupData()
                    if txt == "test":
                        try:self.client.invite_into_group(to, ["u05b001551c897ad6a6e2ca6cecccd32e"]);has = "Normal"
                        except:has = "Down"
                        if not silent:self.client.send_message(to, "{}".format(has))

                    if txt == 'global:room':
                       Data = self.status["bot"]
                       a = []
                       b = self.client.get_group(to)
                       for i in b.members:
                        if i.mid not in Data and i.mid not in self.uid and self.pangkat(to,i.mid) > 4:
                            Data.append(i.mid)
                            a.append(i.mid)
                       if a == []:
                          if not silent:self.client.send_message(to,"Nothing to added.")
                       else:self.listdata(to,self.status,'Add whitelist','bot',a)
                       self.backupData()

                    if txt == "invite bot":
                        if self.status["squad"] != []:
                            try:
                               self.client.invite_into_group(to, self.status["squad"])
                            except:
                               if not silent:self.client.send_message(to,"Limit.")
                        else:
                            if not silent:self.client.send_message(to,"Squad list is empty.")
                    if txt == "invite staybot":
                        if self.status["anti"] != []:
                            try:
                               self.client.invite_into_group(to, self.status["anti"])
                            except:
                               if not silent:self.client.send_message(to,"Limit.")
                        else:
                            if not silent:self.client.send_message(to,"Squad list is empty.")
                    if txt == "bot:qr":
                        g = self.client.get_compact_group(to)
                        links = g.preventedJoinByTicket
                        if links == True:
                            g.preventedJoinByTicket = False
                            self.client.update_group(g)
                        link = self.client.reissue_group_ticket(to)
                        for ki in self.status["squad"]:
                            self.client.send_message(ki,"%s %s"%(to,link))
                        time.sleep(0.1)
                        g.preventedJoinByTicket = True
                        self.client.update_group(g)
                    if txt.startswith("set flag: "):
                            sep = msg.text.split(": ")
                            stickername = msg.text.replace(sep[0] + ": ","")
                            self.settings["squad"] = stickername
                            self.backupData()
                            if not silent:self.client.send_message(to,"Squad flag name changed to " + self.settings["squad"])

                    if txt.startswith("uprname "):
                        string = txt.split(" ")[1]
                        self.settings["rname"] = string
                        self.backupData()
                        if not silent:self.client.send_message(to,"Responsename changed to " +self.settings["rname"])

                    if txt == "cname":
                        profile_B = self.client.profile
                        if msg.from_id in self.settings['cname']:
                            rn = self.settings['cname'][msg.from_id]
                        else:rn = self.settings["rname"]
                        profile_B.displayName = rn
                        self.client.update_profile_attribute(2, profile_B.displayName)
                        if not silent:self.client.send_message(to,"Display Name changed to " + self.settings["rname"])
                    if txt == "crname":
                        profile_B = self.client.profile
                        xn = str(profile_B.displayName).replace(' ','')
                        self.settings["rname"] = xn.lower()
                        self.backupData()
                        if not silent:self.client.send_message(to,"Responsename changed to " +xn)

                    if txt == "groups":
                        gid = self.client.get_joined_group_mids()
                        print(len(gid))
                        b = 0
                        h = ""
                        for a in gid:
                            b = b + 1
                            end = '\n'
                            h += str(b) + " - " + self.client.get_group(a).name + "\n"
                        if not silent:self.client.send_message(to,"List groups:" + "\n" + h + "Total [%s] groups" %str(len(gid)))
                    if txt == "gpending" or txt.startswith('gpending '):
                       gid = self.client.get_invited_group_mids()
                       if txt == 'gpending':
                        print(len(gid))
                        b = 0
                        h = ""
                        for a in gid:
                            b = b + 1
                            end = '\n'
                            h += str(b) + " - " + self.client.get_group(a).name + "\n"
                        if not silent:self.client.send_message(to,"List invitatation:" + "\n" + h + "Total [%s] groups" %str(len(gid)))
                       else:
                        txtk = int(txt.replace("gpending ",""))
                        p = self.client.get_group(gid[txtk-1])
                        print(gid[txtk-1])
                        b = 0
                        h = ""
                        gh = [i.mid for i in p.members]
                        for a in gh:
                            b = b + 1
                            end = '\n'
                            h += str(b) + " - " + self.client.get_contact(a).displayName + "\n"
                        if not silent:self.client.send_message(to,"List Members:" + "\n" + h + "Total [%s] groups" %str(len(gh)))

                    if txt == "clear temp":
                        self.cleartemp(to)
                        self.client.removeAllMessages(to)
                        if not silent:self.client.send_message(to,"Tempfile Cleared")
                        self.backupData()

                    if txt.startswith("add admin"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        for target in targets:
                            if target in self.status["staff"]:
                               self.status["staff"].remove(target)
                            if target in self.status["bot"]:
                               self.status["bot"].remove(target)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Admin Add ✨\n',pg='ADDADM',pt=targets,silent=silent)
                      else:
                        self.status["aadmin"] = True
                        if not silent:self.client.send_message(to,"Send contact.")
                      self.backupData()

                    if txt == "admin repeat":
                        self.status["aadmin"] = True
                        self.status["repeat"] = True
                        self.backupData()
                        if not silent:self.client.send_message(to,"Send contact.")

                    if txt == "bot repeat":
                        self.status["abot"] = True
                        self.status["repeat"] = True
                        self.backupData()
                        if not silent:self.client.send_message(to,"Send contact.")
                    if txt == "ajs repeat":
                        self.addajs = True
                        self.status["repeat"] = True
                        self.backupData()
                        if not silent:self.client.send_message(to,"Send contact.")

                    if txt.startswith("del admin"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Del Admin ✨\n',pg='DELADM',pt=targets,silent=silent)
                      else:
                        data = txt.replace("del admin","")
                        text = data.split(' ')
                        com = str(text[1])
                        selection = Archimed(com,range(1,len(self.status['admin'])+1))
                        k = len(self.status['admin'])//100
                        d = []
                        for c in selection.parse():
                            d.append(self.status['admin'][int(c)-1])
                        for a in range(k+1):
                            if a == 0:self.mentionmention(to=to,status=self.status,text='',dataMid=d[:100],pl=-0,ps='   ✨ Del Admin ✨\n',pg='DELADM',pt=d,silent=silent)
                            else:self.mentionmention(to=to,status=self.status,text='',dataMid=d[a*100 : (a+1)*100],pl=a*100,ps='   ✨ Del Admin ✨\n',pg='DELADM',pt=d,silent=silent)
                      self.backupData()

                    if txt.startswith("add bot"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        for target in targets:
                            if target in self.status["staff"]:
                                self.status["staff"].remove(target)
                            if target in self.status["admin"]:
                                self.status["admin"].remove(target)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Bot Add ✨',pg='ADDWL',pt=targets,silent=silent)
                      else:
                        self.status["abot"] = True
                        if not silent:self.client.send_message(to,"Send contact.")
                      self.backupData()

                    if txt.startswith("add squad"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        for target in targets:
                            if target in self.status["staff"]:
                                self.status["staff"].remove(target)
                            if target in self.status["admin"]:
                                self.status["admin"].remove(target)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Squad Add ✨',pg='ADDBO',pt=targets,silent=silent)
                        self.backupData()
                    if txt.startswith("add con"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Contact Add ✨',pg='ADDFL',pt=targets,silent=silent)
                    if txt.startswith("del con"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Del Friend ✨',pg='DELFL',pt=targets,silent=silent)
                      else:
                        split = txt.replace("del con ","")   
                        nama = self.client.refreshContacts()
                        selection = Archimed(split,range(1,len(nama)+1))
                        k = len(nama)//100
                        d = []
                        for c in selection.parse():
                            d.append(nama[int(c)-1])
                        for a in range(k+1):
                            if a == 0:self.mentionmention(to=to,status=self.status,text='',dataMid=d[:100],pl=-0,ps='   ✨ del friends ✨\n',pg='DELFL',pt=d,silent=silent)
                            else:self.mentionmention(to=to,status=self.status,text='',dataMid=d[a*100 : (a+1)*100],pl=a*100,ps='   ✨ del friends ✨\n',pg='DELFL',pt=d,silent=silent)
                    if txt.startswith("friends ") or txt == "friends":
                                if txt.startswith('friends '):
                                     a = self.client.refreshContacts()
                                     data = txt.replace("friends","")
                                     text = data.split(' ')
                                     num = str(text[1])
                                     self.listcon(to,msg,num,self.status,a)
                                else:
                                     a = self.client.refreshContacts()
                                     k = len(a)//20
                                     for aa in range(k+1):
                                       if aa == 0:self.mentionmention(to=to,status=self.status,text='',dataMid=a[:20],pl=0,ps='   ✨ Friends ✨',pg='MENTIONALLME',pt=a,silent=silent)
                                       else:self.mentionmention(to=to,status=self.status,text='',dataMid=a[aa*20 : (aa+1)*20],pl=aa*20,ps='   ✨ Friends ✨',pg='MENTIONALLME',pt=a,silent=silent)
                    if txt.startswith("del squad"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ del squad ✨\n',pg='DELBO',pt=targets,silent=silent)
                      else:
                        data = txt.replace("del squad","")
                        text = data.split(' ')
                        com = str(text[1])
                        selection = Archimed(com,range(1,len(self.status['squad'])+1))
                        k = len(self.status['squad'])//100
                        d = []
                        for c in selection.parse():
                            d.append(self.status['squad'][int(c)-1])
                            self.status["bot"].append(c)
                        for a in range(k+1):
                            if a == 0:self.mentionmention(to=to,status=self.status,text='',dataMid=d[:100],pl=-0,ps='   ✨ del squad ✨\n',pg='DELBO',pt=d,silent=silent)
                            else:self.mentionmention(to=to,status=self.status,text='',dataMid=d[a*100 : (a+1)*100],pl=a*100,ps='   ✨ del squad ✨\n',pg='DELBO',pt=d,silent=silent)
                      self.backupData()
                    if txt.startswith("add ajs") and self.mode == 1:
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Backup Add ✨\n',pg='ADDBK',pt=targets,silent=silent)
                      else:self.addajs = True;self.client.send_message(msg.to_id, "Send contact.")
                      self.backupData()
                    if txt.startswith("del ajs") and self.mode == 1:
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Del ajs ✨\n',pg='DELBK',pt=targets,silent=silent)
                      else:
                        data = txt.replace("del ajs","")
                        text = data.split(' ')
                        com = str(text[1])
                        selection = Archimed(com,range(1,len(self.status['anti'])+1))
                        k = len(self.status['anti'])//100
                        d = []
                        for c in selection.parse():
                            d.append(self.status['anti'][int(c)-1])
                        for a in range(k+1):
                            if a == 0:self.mentionmention(to=to,status=self.status,text='',dataMid=d[:100],pl=-0,ps='   ✨ Del ajs ✨\n',pg='DELBK',pt=d,silent=silent)
                            else:self.mentionmention(to=to,status=self.status,text='',dataMid=d[a*100 : (a+1)*100],pl=a*100,ps='   ✨ Del ajs ✨\n',pg='DELBK',pt=d,silent=silent)
                      self.backupData()

                    if txt == 'mute':
                        if self.settings["mute"]:
                            self.client.send_message(msg.to_id, "Already silent.")
                        else:
                            self.settings["mute"] = True
                            self.backupData()
                            self.client.send_message(msg.to_id, "I will silent.")

                    if txt == 'unmute':
                        if self.settings["mute"]:
                            self.settings["mute"] = False
                            self.backupData()
                            self.client.send_message(msg.to_id, "Yups Stay")
                        else:
                            self.client.send_message(msg.to_id, "Ready to Stay")
                    if txt.startswith("del bot"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Del Bot ✨\n',pg='DELWL',pt=targets,silent=silent)
                      else:
                        data = txt.replace("del bot","")
                        text = data.split(' ')
                        com = str(text[1])
                        selection = Archimed(com,range(1,len(self.status['bot'])+1))
                        k = len(self.status['bot'])//100
                        d = []
                        for c in selection.parse():
                            d.append(self.status['bot'][int(c)-1])
                        for a in range(k+1):
                            if a == 0:self.mentionmention(to=to,status=self.status,text='',dataMid=d[:100],pl=-0,ps='   ✨ Del Bot ✨\n',pg='DELWL',pt=d,silent=silent)
                            else:self.mentionmention(to=to,status=self.status,text='',dataMid=d[a*100 : (a+1)*100],pl=a*100,ps='   ✨ Del Bot ✨\n',pg='DELWL',pt=d,silent=silent)
                      self.backupData()

                    if txt == 'add all bot':
                        a = self.client.refreshContacts()
                        for target in self.status["bot"]:
                            if target not in self.client.profile.mid and target not in a:
                                try:
                                    self.client.add_contact_by_mid(target)
                                    time.sleep(0.33)
                                except Exception as e:
                                    pass
                    if txt == 'clear friends':
                        a = self.client.refreshContacts()
                        ko = []
                        for l in a:
                            if self.pangkat(to,l) > 8:
                                try:
                                    self.client.delcon(l)
                                    ko.append(l)
                                except Exception as e:
                                    traceback.print_exc()
                        if not silent:self.client.send_message(to, "{} friends deleted.".format(len(ko)))
                    if txt == '.add me':
                                a = self.client.refreshContacts()
                                if msg.from_id not in a:
                                    self.client.add_contact_by_mid(msg.from_id)
                                    if not silent:self.client.send_message(to, "Okay...")
                                else:
                                    if not silent:self.client.send_message(to, "Already in friendlist...")
                    if txt == "max":
                        if to not in self.settings["cancel"]:
                            self.settings["cancel"][to] = 2
                        if to not in self.settings["linkprotect"]:
                            self.settings["linkprotect"][to] = 2
                        if to not in self.settings["protect"]:
                            self.settings["protect"][to] = 2
                        if to not in self.settings["blj"]:
                            self.settings["blj"][to] = True
                        self.pro = to
                        self.backupData()
                        if not silent:self.client.send_message(msg.to_id, "Maximal !!!")
                    if txt == "none":
                        if self.pro == to:
                                        if to in self.settings["cancel"]:
                                            del self.settings["cancel"][to]
                                        if to in self.settings["linkprotect"]:
                                            del self.settings["linkprotect"][to]
                                        if to in self.settings["protect"]:
                                            self.settings["protect"][to] = 1
                                        if to in self.settings["namelock"]:
                                            del self.settings["namelock"][to]
                                        if to in self.settings["blj"]:
                                            del self.settings["blj"][to]
                                        self.pro = ''
                                        self.backupData()
                                        if not silent:self.client.send_message(msg.to_id, "Sayonara !!!")
                    if txt == 'clear ban':
                                    if self.status["blacklist"] != []:
                                        jum = len(self.status["blacklist"])
                                        self.status["blacklist"] = []
                                        if not silent:self.client.send_message(to, "{} blacklist cleared.".format(jum))
                                        self.backupData()
                                    else:
                                        if not silent:self.client.send_message(to, "Blacklist is empty.")
                                    
                    if txt == 'clear backup' and self.mode == 0:
                                    self.status["backup"]["all"] = []
                                    if not silent:self.client.send_message(to, "Back cleared.")
                                    self.backupData()
                    if txt == 'clear bot':
                                    self.status["bot"] = []
                                    self.backupData()
                                    if not silent:self.client.send_message(to, "Bot cleared.")
                    if txt == 'clear squad':
                                    self.status["squad"] = []
                                    self.backupData()
                                    if not silent:self.client.send_message(to, "Squad cleared.")
                    if txt == 'clear admin':
                                    self.status["admin"] = []
                                    self.backupData()
                                    if not silent:self.client.send_message(to, "Admin cleared.")
                    if txt == 'clear staff':
                                    self.status["staff"] = []
                                    self.backupData()
                                    if not silent:self.client.send_message(to, "Staff cleared.")
                    if txt == 'clear ajs':
                                    self.status["anti"] = []
                                    self.backupData()
                                    if not silent:self.client.send_message(to, "Stanby bot cleared.")
                    if txt == 'clear gaccess':
                                    self.status["gaccess"] = {}
                                    self.backupData()
                                    if not silent:self.client.send_message(to, "All gaccess cleared.")

                    if txt.startswith("del gaccess "):
                          nump = txt.split()[2]
                          lik = []
                          if nump.isdigit:
                            for a in self.status['gaccess']:
                                lik.append(a)
                            hi = lik[int(nump)-1]
                            del self.status['gaccess'][hi]
                            self.backupData()
                            if not silent:self.client.send_message(to, "Gaccess on '{}' cleared.".format(self.client.get_group(hi).name))
                    if txt.startswith('del group'):
                        gid = self.client.get_joined_group_mids()
                        selection = Archimed(txt.split(' ')[2],range(1,len(gid)+1))
                        k = len(gid)//100
                        for a in range(k+1):
                            if a == 0:eto='  ✨ Leave Group ✨'
                            else:eto='  ✨ Leave Group ✨'
                            text = ''
                            no = 0
                            for i in selection.parse()[a*100 : (a+1)*100]:
                                self.client.leave_group(gid[i - 1])
                                no+=1
                                if no == len(selection.parse()):text+= "\n{}. {}".format(i,self.client.get_group(gid[i - 1]).name)
                                else:text+= "\n{}. {}".format(i,self.client.get_group(gid[i - 1]).name)
                            if not silent:self.client.send_message(to,eto+text)

                    if txt.startswith('talk'):
                      try:
                        txtk = msg.text.split("|")
                        ng = str(txtk[1])
                        foo = str(txtk[2])
                        gid = self.client.get_joined_group_mids()
                        for i in gid:
                            h = self.client.get_group(i).name
                            if h == ng:
                                self.client.send_message(i,foo)
                      except Exception as e:traceback.print_exc()

                    if txt.startswith('invme '):
                        cond = txt.replace("invme ","")
                        num = int(cond)
                        gid = self.client.get_joined_group_mids()
                        group = self.client.get_group(gid[num-1])
                        self.client.add_contact_by_mid(saya)
                        try:
                           self.client.invite_into_group(gid[num-1],[saya])
                           if not silent:self.client.send_message(to,"You has been invited to {}".format(group.name))
                        except:
                           if not silent:self.client.send_message(to,"Sorry i can't invite you to {}\nBecause limit.".format(group.name))
                    if txt.startswith('bc '):
                        text = txt.replace("bc ","")
                        gid = self.client.get_joined_group_mids()
                        if text == "":
                            if not silent:self.client.send_message(to,"Message is Empty")
                        else:
                            for i in gid:
                                self.client.send_message(i, text)
                    if txt == "leave all":
                        gid = self.client.get_joined_group_mids()
                        for g in gid:
                            if g in to:
                                pass
                            else:
                                self.client.leave_group(g)
                        if not silent:self.client.send_message(to, "successfully left from all groups.")
                    if txt == "reject all":
                        gid = self.client.get_invited_group_mids()
                        for g in gid:
                            self.client.reject_group_invitation(g)
                        if not silent:self.client.send_message(to, "successfully reject all invitation.")
                    if txt == "accept all":
                        gid = self.client.get_invited_group_mids()
                        for g in gid:
                            self.client.accept_group_invitation(g)
                        if not silent:self.client.send_message(to, "successfully accept all invitation.")
                    if txt == "remove chat":
                            self.client.removeAllMessages(to)
                            if not silent:self.client.send_message(to,"chat cleared")

                    if txt.startswith('left '):
                        ng = msg.text.replace('left ','')
                        gid = self.client.get_joined_group_mids()
                        for i in gid:
                            h = self.client.get_group(i).name
                            if h == ng:
                                self.client.leave_group(i)
                                if not silent:self.client.send_message(to,"success left from {}".format(ng))

                    if txt.startswith("owncon"):
                      data = txt.replace("owncon","")
                      text = data.split(' ')
                      num = str(text[1])
                      self.listcon(to,msg,num,self.status,self.status["owner"])

                    if txt.startswith("admcon"):
                      data = txt.replace("admcon","")
                      text = data.split(' ')
                      num = str(text[1])
                      self.listcon(to,msg,num,self.status,self.status["admin"])

                    if txt == "owner list":
                        if self.status["owner"] != []:
                           self.listdata(to,self.status,'Bot Owner','own',self.status['owner'])
                        else:
                            if not silent:self.client.send_message(to,"List is empty.")
                    if txt == "admin list":
                        if self.status["admin"] != []:
                           self.listdata(to,self.status,'Bot Admin','adm',self.status['admin'])
                        else:
                            if not silent:self.client.send_message(to,"List is empty.")
                    if txt == "upimage":
                        self.status['picture'] = True
                        self.backupData()
                        if not silent:self.client.send_message(to,"Send the picture.")
                    if txt.startswith("upstatus "):
                            status = msg.text.split("upstatus ")[1]
                            self.client.set_profile_status(status)
                            if not silent:self.client.send_message(to,"Status updated to: %s."%status)
                    if txt == "upcover":
                        self.adc = True
                        if not silent:self.client.send_message(to,"Send the picture.")
                    if txt == "upvideo":
                        self.status['cvp'] = True
                        self.backupData()
                        if not silent:self.client.send_message(to,"Send the video.")
                    if txt.startswith("upname "):
                        string = msg.text.split("upname ")[1].replace(' .silent','')
                        profile_B = self.client.profile
                        profile_B.displayName = string
                        self.client.update_profile_attribute(2, profile_B.displayName)
                        if not silent:self.client.send_message(to,"Display Name changed to " + string)
                    if txt.startswith("copyname"):
                        targets = []
                        if msg.mentionees:
                            self.mention(msg,targets)
                            for target in targets:
                                try:
                                    self.client.copyName(target)
                                    if not silent:self.client.send_message(to, "Succes copy Name")
                                except:
                                    if not silent:self.client.send_message(to,"Failled")
                    if txt.startswith("copystatus"):
                        targets = []
                        if msg.mentionees:
                            self.mention(msg,targets)
                            for target in targets:
                                try:
                                    self.client.copyStatus(target)
                                    if not silent:self.client.send_message(to, "Succes copy Status")
                                except:
                                    if not silent:self.client.send_message(to,"Failled")
                    if txt.startswith("copypic"):
                        targets = []
                        if msg.mentionees:
                            self.mention(msg,targets)
                            for target in targets:
                                try:
                                    A = self.client.get_contact(target)
                                    url = "http://dl.profile.line.naver.jp"+A.picturePath
                                    xpath = self.client.download_regular(url)
                                    self.client.updateProfilePicture(xpath)
                                    os.remove(xpath)
                                    if not silent:self.client.send_message(to, "Succes copy Picture")
                                except:
                                    if not silent:self.client.send_message(to,"Failled")

                if self.pangkat(to,saya) < 3:
                  if "pancal" in txt:
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        for target in targets:
                            if self.pangkat(to,target) < 9:
                                pass
                            else:
                                try:
                                    self.addbl(target)
                                except:
                                    traceback.print_exc()
                  if '/ti/g/' in msg.text and self.settings["atjoin"] and not 'kick' in txt:
                                regex = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = regex.findall(text)
                                tickets = []
                                gids = self.client.get_joined_group_mids()
                                for link in links:
                                    if link not in tickets:
                                        tickets.append(link)
                                for ticket in tickets:
                                    try:
                                        group = self.client.get_group_by_ticket(ticket)
                                    except:
                                        continue
                                    if group.id in gids:
                                        continue
                                    self.client.accept_group_invitation_by_ticket(group.id, ticket)
                  if msg.text.startswith(rname+"nk "):
                                        nk0 = msg.text.replace(rname+"nk ","")
                                        nk1 = nk0.lstrip()
                                        nk2 = nk1.replace("@","")
                                        nk3 = nk2.rstrip()
                                        _name = nk3
                                        gs = self.client.get_group(to)
                                        targets = []
                                        for s in gs.members:
                                            if _name in s.displayName:
                                                targets.append(s.mid)
                                        if targets == []:
                                            self.client.send_message(msg.to_id,"Target not match.")
                                        else:
                                            cms = '/root/crash/simple.js gid={} token={} app={}'.format(to,self.client.authToken,self.app)
                                            for y in targets:
                                                cms += ' uid={}'.format(y)
                                            success = execute_js(cms)
                                            if success:
                                                self.client.send_message(to,'Execute success')
                                            else:
                                                 self.client.send_message(to,'error')
                  for a in cmds:
                    if a.startswith(rname):txt = a.replace(a[:len(rname)],'')
                    elif a.startswith(sname):txt = a.replace(a[:len(sname)],'')
                    elif a.startswith("oup"):txt = a.replace(a[:len("oup")]+' ','')
                    elif cmds.index(a) != 0 and rname not in a and sname not in a:txt = a
                    if txt == 'allowban on':
                        if self.settings["allowban"]:
                            if not silent:self.client.send_message(msg.to_id, "Allowban already enabled.")
                        else:
                            self.settings["allowban"] = True
                            self.backupData()
                            if not silent:self.client.send_message(msg.to_id, "Allowban enabled.")
                    if txt == 'allowban off':
                        if self.settings["allowban"] :
                            self.settings["allowban"] = False
                            self.backupData()
                            if not silent:self.client.send_message(msg.to_id, "Allowban disabled.")
                        else:
                            if not silent:self.client.send_message(msg.to_id, "Allowban already disabled.")

                    if txt.startswith("#nuke"):
                        data = txt.replace("#nuke","")
                        text = data.split(' ')
                        com = str(text[1])
                        gs = self.client.get_group(to)
                        nama = [contact.mid for contact in gs.members]
                        no = 0
                        targets = []
                        selection = Archimed(com,range(1,len(nama)+1))
                        for i in selection.parse():
                            targets.append(nama[i-1])
                        mc = ""
                        b = 0
                        for mi_d in targets:
                            b = b + 1
                            end = '\n'
                            mc += str(b) + " - " +self.client.get_contact(mi_d).displayName + "\n"
                        for target in targets:
                              try:
                                            cms = '/root/crash/simple.js gid={} token={} app={}'.format(to,self.client.authToken,self.app)
                                            for y in targets:
                                                cms += ' uid={}'.format(y)
                                            print(cms)
                                            success = execute_js(cms)
                                            if success:
                                                self.client.send_message(to,'Execute success')
                                            else:
                                                self.client.send_message(to,'error')
                              except Exception as e:print(e)
                        if not silent:self.client.send_message(msg.to_id,"Trying to kick user :\n"+"\n"+mc+"\nFrom Group"+ gs.name)

                    if txt == 'info group':
                        group = self.client.get_group(to)
                        zxc = " ✨ Group members ✨\nName: "+group.name+"\nMember:"
                        total = "\nGroup ID:\n"+to
                        no = 0
                        if len(group.members) > 0:
                            for a in group.members:
                                no += 1
                                zxc += "\n   " + str(no) + ". " + a.displayName
                            if not silent:self.client.send_message(msg.to_id,zxc + total)

                    if txt.startswith('chat, '):
                        txti = txt.split("chat, ")
                        foo = str(txti[1])
                        if not silent:self.client.send_message(to, foo)
                    if txt == "squad list":
                        if self.status['squad']:
                            self.listdata(to,self.status,'squad','bol',self.status['squad'])
                        else:
                            if not silent:self.client.send_message(to,"List is empty.")
                    if txt == 'leave' or txt == 'out' or txt == 'bye' or txt == '@bye' or txt == 'retreat':
                        self.client.leave_group(to)

                    if txt == 'whitelist':
                        mc = ""
                        a = 0
                        for m_id in self.status["bot"]:
                            a = a + 1
                            end = '\n'
                            try:
                               mc += str(a) + " • " +self.client.get_contact(m_id).displayName + "\n"
                            except Exception as e:self.status["bot"].remove(m_id);print("del {}".format(m_id))
                        self.backupData()
                        if not silent:self.client.send_message(to," ∆✨ "+self.settings["squad"]+" ✨∆\n✨   Whitelist   ✨\n\n"+mc)

                    if txt == "run" or txt == "runtime":
                       eltime = time.time() - self.awit
                       cin = "Uptime "+waktu(eltime)
                       if not silent:self.client.send_message(to,cin)

                    if txt == "uinvite":
                        self.status["invite"] = True
                        self.backupData()
                        if not silent:self.client.send_message(to,"Send contact.")

                    if txt.startswith("unsend "):
                        args = txt.replace("unsend ","").lstrip().rstrip()
                        mes = 0
                        try:
                            mes = int(args)
                        except:
                            mes = 1
                        M = self.client.getRecentMessages(to, 101)
                        MId = []
                        for ind,i in enumerate(M):
                            if ind == 0:
                                pass
                            else:
                                if i._from == self.client.profile.mid:
                                    MId.append(i.id)
                                    if len(MId) == mes:
                                        break
                        def unsMes(id):
                            self.client.unsend_message(id)
                        for i in MId:
                            thread1 = threading.Thread(target=unsMes, args=(i,))
                            thread1.start()
                            thread1.join()
                    if txt == "staffs" or txt == 'access':
                       rname = self.settings["rname"]
                       tst = "      ✨ ∆ "+self.settings["squad"]+" ∆ ✨ "+ "\n\n  🔯✨ Bot Access ✨🔯"
                       num=0
                       num1=0
                       num2=0
                       num3=0
                       num4=0
                       num5=0
                       uh = self.status
                       mstr1 = self.creator
                       mstr2 = uh["owner"]
                       mstr3 = uh["admin"]
                       mstr4 = uh["staff"]
                       num=(num+1)
                       num1=(num1+1)
                       num2=(num2+1)
                       num3=(num3+1)
                       num4=(num4+1)
                       num5=(num5+1)
                       tst += "\n\n       ✨ Creator ✨ "
                       for c in mstr1:
                        try:
                           c = self.client.get_contact(c).displayName
                           if num1 < 10:
                            tst += "\n %i.   %s "%(num1,c)
                           else:
                            tst += "\n %i. %s "%(num1,c)
                           num1=(num1+1)
                        except Exception as e:mstr1.remove(c)
                       if mstr2 != []:
                        tst += "\n\n       ✨ Owner ✨ "
                        for c in mstr2:
                          try:
                           c = self.client.get_contact(c).displayName
                           if num < 10:
                            tst += "\n %i.   %s "%(num,c)
                           else:
                            tst += "\n %i. %s "%(num,c)
                           num=(num+1)
                          except:mstr2.remove(c)
                       if mstr3 != []:
                        tst += "\n\n       ✨ Admin ✨ "
                        for c in mstr3:
                          try:
                           c = self.client.get_contact(c).displayName
                           if num2 < 10:
                            tst += "\n %i.   %s "%(num2,c)
                           else:
                            tst += "\n %i. %s "%(num2,c)
                           num2=(num2+1)
                          except:mstr3.remove(c)
                       if mstr4 != []:
                        tst += "\n\n       ✨ Staff ✨ "
                        for c in mstr4:
                          try:
                           c = self.client.get_contact(c).displayName
                           if num3 < 10:
                            tst += "\n %i.   %s "%(num3,c)
                           else:
                            tst += "\n %i. %s "%(num3,c)
                           num3=(num3+1)
                          except:mstr4.remove(c)
                       if to in uh['gaccess']:
                        akses = uh['gaccess'][to]
                        if akses['gowner'] != []:
                         tst += "\n\n       ✨ GOwner ✨ "
                         for c in akses['gowner']:
                          try:
                           c = self.client.get_contact(c).displayName
                           if num4 < 10:
                            tst += "\n %i.   %s "%(num4,c)
                           else:
                            tst += "\n %i. %s "%(num4,c)
                           num4=(num4+1)
                          except:akses['gowner'].remove(c)
                        if akses['gadmin'] != []:
                         tst += "\n\n       ✨ GAdmin ✨ "
                         for c in akses['gadmin']:
                          try:
                           c = self.client.get_contact(c).displayName
                           if num5 < 10:
                            tst += "\n %i.   %s "%(num5,c)
                           else:
                            tst += "\n %i. %s "%(num5,c)
                           num5=(num5+1)
                          except:akses['gadmin'].remove(c)
                       tst += "\n\n✨ B£∆CK_∆NG€£ ✨"
                       if not silent:self.client.send_message(to,tst)
                    if txt == "all gaccess":
                       rname = self.settings["rname"]
                       tst = "      ✨ ∆ "+self.settings["squad"]+" ∆ ✨ "+ "\n\n  ✡✨ Group Access ✨✡"
                       deli = []
                       if self.status['gaccess'] != {}:
                        for hi in self.status['gaccess']:
                          if self.status['gaccess'][hi]['gowner'] == [] and self.status['gaccess'][hi]['gadmin'] == []:
                            deli.append(hi)
                          else:
                            num=0
                            num1=0
                            num=(num+1)
                            num1=(num1+1)
                            tst += "\n\n • {} \n".format(self.client.get_group(hi).name)
                            if self.status['gaccess'][hi]['gowner'] != []:
                                tst += "\n          ✨ Group Owner ✨ "
                                for c in  self.status['gaccess'][hi]['gowner']:
                                 try:
                                    z = self.client.get_contact(c).displayName
                                    if num < 10:
                                     tst += "\n %i.   %s "%(num,z)
                                    else:
                                     tst += "\n %i. %s "%(num,z)
                                    num=(num+1)
                                 except:
                                    self.status['gaccess'][hi]['gowner'].remove(c)
                            if self.status['gaccess'][hi]['gadmin'] != []:
                                tst += "\n\n          ✨ Group Admin ✨ "
                                for c in  self.status['gaccess'][hi]['gadmin']:
                                 try:
                                    z = self.client.get_contact(c).displayName
                                    if num1 < 10:
                                     tst += "\n %i.   %s "%(num1,z)
                                    else:
                                     tst += "\n %i. %s "%(num1,z)
                                    num1=(num1+1)
                                 except:self.status['gaccess'][hi]['gadmin'].remove(c)
                       tst += "\n\n✨ B£∆CK_∆NG€£ ✨"
                       if not silent:self.client.send_message(to,tst)
                       for a in deli:
                            del self.status['gaccess'][a]
                       self.backupData()
                    if txt == "gaccess" or txt.startswith("gaccess "):
                        if txt == "gaccess":
                            rname = self.settings["rname"]
                            tst = "      ✨ ∆ "+self.settings["squad"]+" ∆ ✨ "+ "\n\n  ⚛✨ Group Access ✨⚛\n"
                            deli = []
                            num=0
                            num=(num+1)
                            if self.status['gaccess'] != {}:
                             for hi in self.status['gaccess']:
                               if self.status['gaccess'][hi]['gowner'] == [] and self.status['gaccess'][hi]['gadmin'] == []:
                                 deli.append(hi)
                               else:
                                 tst += "\n{} •  {} ".format(num,self.client.get_group(hi).name)
                               num = (num+1)

                            tst += "\n\n✨ B£∆CK_∆NG€£ ✨"
                            if not silent:self.client.send_message(to,tst)
                            for a in deli:
                                 del self.status['gaccess'][a]
                            self.backupData()
                        else:
                          nump = txt.split()[1]
                          lik = []
                          if nump.isdigit:
                            for a in self.status['gaccess']:
                                lik.append(a)
                            hi = lik[int(nump)-1]
                            tst = "      ✨ ∆ "+self.settings["squad"]+" ∆ ✨ "+ "\n\n  ⚛✨ Group Access ✨⚛"
                            num=0
                            num1=0
                            num=(num+1)
                            num1=(num1+1)
                            tst += "\n\n ⚙️ {} ⚙️".format(self.client.get_group(hi).name)
                            if self.status['gaccess'][hi]['gowner'] != []:
                                tst += "\n          ✨ Group Owner ✨ "
                                for c in  self.status['gaccess'][hi]['gowner']:
                                 try:
                                    z = self.client.get_contact(c).displayName
                                    if num < 10:
                                     tst += "\n %i.   %s "%(num,z)
                                    else:
                                     tst += "\n %i. %s "%(num,z)
                                    num=(num+1)
                                 except:
                                    self.status['gaccess'][hi]['gowner'].remove(c)
                            if self.status['gaccess'][hi]['gadmin'] != []:
                                tst += "\n\n          ✨ Group Admin ✨ "
                                for c in  self.status['gaccess'][hi]['gadmin']:
                                 try:
                                    z = self.client.get_contact(c).displayName
                                    if num1 < 10:
                                     tst += "\n %i.   %s "%(num1,z)
                                    else:
                                     tst += "\n %i. %s "%(num1,z)
                                    num1=(num1+1)
                                 except:self.status['gaccess'][hi]['gadmin'].remove(c)
                            tst += "\n\n✨ B£∆CK_∆NG€£ ✨"
                            if not silent:self.client.send_message(to,tst)
                    if txt == 'prot status':
                                a = "    ✨ ᴅᴇɴʏɪɴᴠɪᴛᴇ ✨"
                                b = "    ✨ ʟɪɴᴋᴘʀᴏᴛᴇᴄᴛ ✨"
                                c = "    ✨ ᴍᴀɪɴ ᴘʀᴏᴛᴇᴄᴛ ✨"
                                e = "    ✨ ᴘᴊᴏɪɴ ✨"
                                f = "    ✨ ɴᴀᴍᴇʟᴏᴄᴋ ✨"
                                g = "    ✨ ᴋɪᴄᴋ ✨"
                                aa = 0
                                bb = 0
                                cc = 0
                                ee = 0
                                ff = 0
                                gg = 0
                                gid = self.settings["cancel"]
                                for group in gid:
                                  if self.settings["cancel"] == {}:
                                    a += "Empty"
                                  else:
                                    G = self.client.get_group(group)
                                    aa += 1
                                    a += "\n" + str(aa) + ". " + str(G.name)
                                gid = self.settings["linkprotect"]
                                for group in gid:
                                  if self.settings["linkprotect"] == {}:
                                     b += "Empty"
                                  else:
                                    G = self.client.get_group(group)
                                    bb += 1
                                    b += "\n" + str(bb) + ". " + str(G.name)
                                gid = self.settings["protect"]
                                for group in gid:
                                  if self.settings["protect"] == {}:
                                     c += "Empty"
                                  else:
                                    G = self.client.get_group(group)
                                    cc += 1
                                    c += "\n" + str(cc) + ". " + str(G.name)
                                gid = self.settings["blj"]
                                for group in gid:
                                  if self.settings["blj"] == {}:
                                     e += "Empty"
                                  else:
                                    G = self.client.get_group(group)
                                    ee += 1
                                    e += "\n" + str(ee) + ". " + str(G.name)
                                gid = self.settings["namelock"]
                                for group in gid:
                                  if self.settings["namelock"] == {}:
                                     f = "Empty"
                                  else:
                                    G = self.client.get_group(group)
                                    ff += 1
                                    f += "\n" + str(ff) + ". " + str(G.name)
                                gid = self.settings["kick"]
                                for group in gid:
                                  if self.settings["kick"] == {}:
                                     g = "Empty"
                                  else:
                                    G = self.client.get_group(group)
                                    gg += 1
                                    g += "\n" + str(gg) + ". " + str(G.name)
                                if not silent:self.client.send_message(to,"  ∆✨ "+self.settings["squad"]+" ✨ \n  ∆Set Status\n\n"+a+"\n\n"+b+"\n\n"+c+"\n\n"+e+"\n\n"+f+"\n\n"+g+"\n\n   ✨ Encore ✨")

                    if txt.startswith("staffcon"):
                      data = txt.replace("staffcon","")
                      text = data.split(' ')
                      num = str(text[1])
                      self.listcon(to,msg,num,self.status,self.status["staff"])

                    if txt.startswith("botcon"):
                      data = txt.replace("botcon","")
                      text = data.split(' ')
                      num = str(text[1])
                      self.listcon(to,msg,num,self.status,self.status["bot"])

                    if txt.startswith("bancon"):
                      data = txt.replace("bancon","")
                      text = data.split(' ')
                      num = str(text[1])
                      self.listcon(to,msg,num,self.status,self.status["blacklist"])

                    if txt.startswith("expel"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        eto = "Expelled"
                        for target in targets:
                          if self.pangkat(to,saya) < 1:
                            if target in self.status["owner"]:
                                self.status["owner"].remove(target)
                                if not silent:self.sendtag(to,"access user @! expeled from owner",eto,[target])
                            if target in self.status["admin"]:
                                self.status["admin"].remove(target)
                                if not silent:self.sendtag(to,"access user @! expeled from admin",eto,[target])
                            if target in self.status["bot"]:
                                self.status["bot"].remove(target)
                                if not silent:self.sendtag(to,"access user @! expeled from bot",eto,[target])
                            if target in self.status["squad"]:
                                self.status["squad"].remove(target)
                                if not silent:self.sendtag(to,"access user @! expeled from bolo",eto,[target])
                            if target in self.status["staff"]:
                                self.status["staff"].remove(target)
                                if not silent:self.sendtag(to,"access user @! expeled from staff",eto,[target])
                            if to in self.status['gaccess']:
                                if target in self.status['gaccess'][to]['gowner']:
                                   self.status['gaccess'][to]['gowner'].remove(target)
                                   if not silent:self.sendtag(to,"access user @! expeled from gowner",eto,[target])
                                if target in self.status['gaccess'][to]['gadmin']:
                                   self.status['gaccess'][to]['gadmin'].remove(target)
                                   if not silent:self.sendtag(to,"access user @! expeled from gadmin",eto,[target])
                          if self.pangkat(to,saya) == 1:
                            if target in self.creator:
                                if not silent:self.sendtag(to,"Who are you @! ?\nThat's my creator",eto,[saya])
                            if target in self.status["owner"]:
                                if not silent:self.sendtag(to,"Stop @! ?\nYour access is to low",eto,[saya])
                            if target in self.status["admin"]:
                                self.status["admin"].remove(target)
                                if not silent:self.sendtag(to,"access user @! expeled from admin",eto,[target])
                            if target in self.status["bot"]:
                                self.status["bot"].remove(target)
                                if not silent:self.sendtag(to,"access user @! expeled from bot",eto,[target])
                            if target in self.status["squad"]:
                                self.status["squad"].remove(target)
                                if not silent:self.sendtag(to,"access user @! expeled from bolo",eto,[target])
                            if target in self.status["staff"]:
                                self.status["staff"].remove(target)
                                if not silent:self.sendtag(to,"access user @! expeled from staff",eto,[target])
                          if self.pangkat(to,saya) == 2:
                            if target in self.creator:
                                if not silent:self.sendtag(to,"Who are you @! ?\nThat's my creator",eto,[saya])
                            if target in self.status["owner"]:
                                if not silent:self.sendtag(to,"Who are you @! ?\nThat's my owner",eto,[saya])
                            if target in self.status["admin"]:
                                self.status["admin"].remove(target)
                                if not silent:self.sendtag(to,"Stop @! ?\nYour access is to low",eto,[saya])
                            if target in self.status["bot"]:
                                self.status["bot"].remove(target)
                                if not silent:self.sendtag(to,"access user @! expeled from bot",eto,[target])
                            if target in self.status["staff"]:
                                self.status["staff"].remove(target)
                                if not silent:self.sendtag(to,"access user @! expeled from staff",eto,[target])
                      else:
                        self.status["expel"] = True
                        if not silent:self.client.send_message(to,"Send contact.")
                      self.backupData()

                    if txt == "rep expel":
                        self.status["expel"] = True
                        self.status["repeat"] = True
                        self.backupData()
                        if not silent:self.client.send_message(to,"Send contact.")

                    if txt.startswith("*"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        for target in targets:
                            if self.pangkat(to,target) < 4:
                                pass
                            else:
                                try:
                                    self.client.kick_out_from_group(to,[target])
                                except:
                                    if not silent:self.client.send_message(msg.to_id, "Limit cok")
                    if txt.startswith("kick"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        for target in targets:
                            if self.pangkat(to,target) < 4:
                                pass
                            else:
                                try:
                                    self.client.kick_out_from_group(to,[target])
                                except:
                                    if not silent:self.client.send_message(msg.to_id, "Limit cok")
                    if txt.startswith("skick"):
                            targets = []
                            if msg.mentionees:
                                self.mention(msg,targets)
                                try:
                                            cms = '/root/crash/simple.js gid={} token={} app={}'.format(to,self.client.authToken,self.app)
                                            for y in targets:
                                                cms += ' uid={}'.format(y)
                                            print(cms)
                                            success = execute_js(cms)
                                            if not success:
                                                self.client.send_message(to,'Failed.')
                                except Exception as e:
                                    if not silent:self.client.send_message(msg.to_id, "{}".format(e))

                    if txt == "cleanse":
                                        x = self.client.get_group(to)
                                        nama = [contact.mid for contact in x.members]
                                        targets = []
                                        for a in nama:
                                            if self.pangkat(to,a) > 4 and a != self.uid:
                                                targets.append(a)
                                        if targets == []:
                                            self.client.send_message(msg.to_id,"Target not found.")
                                        else:
                                            cms = '/root/crash/simple.js gid={} token={} app={}'.format(to,self.client.authToken,self.app)
                                            for y in targets:
                                                cms += ' uid={}'.format(y)
                                            success = execute_js(cms)
                                            if success:
                                                self.client.send_message(to,'Execute success')
                                            else:
                                                self.client.send_message(to,'error')

                    if txt == "cans":
                                        x = self.client.get_group(to)
                                        nama = [contact.mid for contact in x.invitee]
                                        targets = []
                                        for a in nama:
                                            if self.pangkat(to,a) > 4:
                                                targets.append(a)
                                        if targets == []:
                                            self.client.send_message(msg.to_id,"Target not found.")
                                        else:
                                            cms = '/root/crash/cancel.js gid={} token={} app={}'.format(to,self.client.authToken,self.app)
                                            for y in targets:
                                                cms += ' uid={}'.format(y)
                                            success = execute_js(cms)
                                            if success:
                                                self.client.send_message(to,'Execute success')
                                            else:
                                                self.client.send_message(to,'error')
                    if txt == 'pending list':
                                        x = self.client.get_group(to)
                                        nama = [contact.mid for contact in x.invitee]
                                        h = ''
                                        for a in nama:
                                           h += '{}'.format(self.client.get_contact(a).displayName)
                                        print(h)
                    if txt.startswith('@cleanse'):
                                        x = self.client.get_group(to)
                                        if x.invitee == None:
                                            nami = []
                                        else:nami = [contact.mid for contact in x.invitee]
                                        targeti = []
                                        for a in nami:
                                            if self.pangkat(to,a) > 6:
                                                targeti.append(a)
                                        if targeti == []:
                                            cmo = []
                                        else:
                                            cmo = '/root/crash/cancel.js gid={} token={}'.format(to,self.client.authToken)
                                            for y in targeti:
                                                cmo += ' uid={}'.format(y)
                                        nama = [contact.mid for contact in x.members]
                                        targets = []
                                        for a in nama:
                                            if self.pangkat(to,a) > 4 and a != self.uid:
                                                targets.append(a)
                                        if targets == []:
                                            cms = []
                                        else:
                                            cms = '/root/crash/simple.js gid={} token={}'.format(to,self.client.authToken)
                                            for y in targets:
                                                cms += ' uid={}'.format(y)
                                        tasks = [asyncio.ensure_future(self.nuker(cms)),asyncio.ensure_future(self.nuker(cmo))]
                                        asyncio.gather(*tasks)
                    if txt.startswith('@break'):
                                        x = self.client.get_group(to)
                                        if x.invitee == None:nama = []
                                        else:nama = [contact.mid for contact in x.invitee]
                                        targets = []
                                        for a in nama:
                                            if self.pangkat(to,a) > 4:
                                                targets.append(a)
                                        nami = [contact.mid for contact in x.members]
                                        targetk = []
                                        cms = '/root/crash/dual.js gid={} token={} app={}'.format(to,self.client.authToken,self.app)
                                        for a in nami:
                                            if self.pangkat(to,a) > 4 and a != self.uid:
                                                targetk.append(a)
                                        for y in targets:
                                            cms += ' uid={}'.format(y)
                                        for y in targetk:
                                            cms += ' uik={}'.format(y)
                                        self.client.sendMessage(msg.to_id,'Please wait...')
                                        print(cms)
                                        success = execute_js(cms)
                                        if success:
                                                self.client.sendMessage(to,'Execute success')
                                        else:
                                                self.client.sendMessage(to,'error')
                    if txt == "kill ban":
                        if msg.to_type == 2:
                            group = self.client.get_group(to)
                            gMembMids = [contact.mid for contact in group.members]
                            matched_list = []
                            for tag in self.status["blacklist"]:
                                matched_list+=filter(lambda str: str == tag, gMembMids)
                            if matched_list == []:
                                pass
                            else:
                                            cms = '/root/crash/simple.js gid={} token={} app={}'.format(to,self.client.authToken,self.app)
                                            for y in targets:
                                                cms += ' uid={}'.format(y)
                                            print(cms)
                                            success = execute_js(cms)
                                            if success:
                                                self.client.send_message(to,'Execute success')
                                            else:
                                                self.client.send_message(to,'error')

                    if txt.startswith("add staff"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        for target in targets:
                            if target in self.status["bot"]:
                                self.status["bot"].remove(target)
                            if target in self.status["admin"]:
                                self.status["admin"].remove(target)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Add staff ✨\n',pg='ADDST',pt=targets,silent=silent)
                      else:
                        self.status["astaff"] = True
                        if not silent:self.client.send_message(to,"Send contact.")
                      self.backupData()
                   
                    if txt == "staff rep":
                        self.status["astaff"] = True
                        self.status["repeat"] = True
                        self.backupData()
                        if not silent:self.client.send_message(to,"Send contact.")

                    if txt.startswith("del staff"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Del staff ✨\n',pg='DELST',pt=targets,silent=silent)
                      else:
                        data = txt.replace("del staff","")
                        text = data.split(' ')
                        com = str(text[1])
                        selection = Archimed(com,range(1,len(self.status['staff'])+1))
                        k = len(self.status['staff'])//100
                        d = []
                        for c in selection.parse():
                            d.append(self.status['staff'][int(c)-1])
                        for a in range(k+1):
                            if a == 0:self.mentionmention(to=to,status=self.status,text='',dataMid=d[:100],pl=-0,ps='   ✨ Del staff ✨\n',pg='DELST',pt=d,silent=silent)
                            else:self.mentionmention(to=to,status=self.status,text='',dataMid=d[a*100 : (a+1)*100],pl=a*100,ps='   ✨ Del staff ✨\n',pg='DELST',pt=d,silent=silent)
                      self.backupData()

                    if txt.startswith("bann"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Blacklist ✨\n',pg='ADDBL',pt=targets,silent=silent)
                      else:
                        self.status["abl"] = True
                        if not silent:self.client.send_message(to,"Send contact.")
                      self.backupData()

                    if txt == "ban rep":
                        self.status["abl"] = True
                        self.status["repeat"] = True
                        self.backupData()
                        if not silent:self.client.send_message(to,"Send contact.")

                    if txt.startswith("unbann"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Del staff ✨\n',pg='DELST',pt=targets,silent=silent)
                      else:
                        data = txt.replace("unbann","")
                        text = data.split(' ')
                        com = str(text[1])
                        selection = Archimed(com,range(1,len(self.status['blacklist'])+1))
                        k = len(self.status['blacklist'])//100
                        d = []
                        for c in selection.parse():
                            d.append(self.status['blacklist'][int(c)-1])
                        for a in range(k+1):
                            if a == 0:self.mentionmention(to=to,status=self.status,text='',dataMid=d[:100],pl=-0,ps='   ✨ Unbanned ✨\n',pg='DELBL',pt=d,silent=silent)
                            else:self.mentionmention(to=to,status=self.status,text='',dataMid=d[a*100 : (a+1)*100],pl=a*100,ps='   ✨ Unbanned ✨\n',pg='DELBL',pt=d,silent=silent)
                      self.backupData()

                    if txt == 'staff list':
                        if self.status['staff'] != []:
                           self.listdata(to,self.status,'Staff List','staff',self.status['staff'])
                        else:
                            if not silent:self.client.send_message(to,"List is empty.")
                    if txt == 'ajs list' and self.mode == 1:
                        if self.status["anti"] != []:
                           self.listdata(to,self.status,'AJS List','own',self.status['anti'])
                        else:
                            if not silent:self.client.send_message(to,"List is empty.")
                    if txt == 'bot list':
                        if self.status["bot"] != []:
                           self.listdata(to,self.status,'Bot List','own',self.status['bot'])
                        else:
                            if not silent:self.client.send_message(to,"List is empty.")

                    if txt == 'flist':
                        if self.status["squad"] == []:
                            if not silent:self.client.send_message(to,"Empty list")
                        else:
                            mc = ""
                            b = 0
                            for mi_d in self.status["squad"]:
                                b = b + 1
                                end = '\n'
                                try:
                                   mc += str(b) + " • " +self.client.get_contact(mi_d).displayName + "\n"
                                except Exception as e:self.status["squad"].remove(mi_d);print("del {}".format(mi_d))
                            self.backupData()
                            if not silent:self.client.send_message(to,"  Squad list:\n"+"\n"+mc)

                    if txt == 'blist':
                        if self.status['blacklist'] != []:
                           self.listdata(to,self.status,'Blacklist','own',self.status['blacklist'])
                        else:
                            if not silent:self.client.send_message(to,"List is empty.")

                if self.ranking(to,saya) < 5:
                  if txt == "angela" or txt == "rname" or txt == "respon" or txt == sname + "rname":
                    if not silent:self.client.send_message(to,rname.rstrip())
                    print(rname)

                  if txt == "sname" or txt == "squad" or txt == "squadname":
                        if not silent:self.client.send_message(to,sname.rstrip())
                  for a in cmds:
                    if a.startswith(rname):txt = a.replace(a[:len(rname)],'')
                    elif a.startswith(sname):txt = a.replace(a[:len(sname)],'')
                    elif a.startswith("oup"):txt = a.replace(a[:len("oup")]+' ','')
                    elif cmds.index(a) != 0 and rname not in a and sname not in a:txt = a
                    if txt.startswith("rname "):
                        string = txt.split(" ")[1]
                        self.settings["cname"][msg.from_id] = string
                        self.backupData()
                        if not silent:self.client.send_message(to,"Responsename changed to " +self.settings["cname"][msg.from_id])
                    if txt.startswith("sname "):
                        string = txt.split(" ")[1]
                        self.settings["dname"][msg.from_id] = string
                        self.backupData()
                        if not silent:self.client.send_message(to,"Squad response changed to " +self.settings["dname"][msg.from_id])
                    if txt == 'reset rname':
                        if msg.from_id in self.settings['cname']:
                           del self.settings['cname'][msg.from_id]
                           self.backupData()
                        if not silent:self.client.send_message(to,"Responsename reseted to " +self.settings["rname"])
                    if txt == 'reset sname':
                        if msg.from_id in self.settings['dname']:
                           del self.settings['dname'][msg.from_id]
                           self.backupData()
                        if not silent:self.client.send_message(to,"Squad Response reseted to " +self.settings["sname"])
                    if txt == "hi" or txt == 'fetch':
                        a = self.client.sendMessage(to,"Hi !").createdTime
                        if not silent:self.client.sendMessage(to,"Fetchops: {}".format(a - op.createdTime))
                    if txt.startswith("add gowner"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Add Gowner ✨\n',pg='ADDGO',pt=targets,silent=silent)
                      self.backupData()
                    if txt.startswith("del gowner"):
                      if to in self.status['gaccess']:
                            targets = []
                            if msg.mentionees:
                              self.mention(msg,targets)
                              self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Del Gowner ✨\n',pg='DELGO',pt=targets,silent=silent)
                            else:
                              data = txt.replace("del gowner","")
                              text = data.split(' ')
                              com = str(text[1])
                              selection = Archimed(com,range(1,len(self.status['gaccess'][to]['gowner'])+1))
                              k = len(self.status['gaccess'][to]['gowner'])//100
                              d = []
                              for c in selection.parse():
                                  d.append(self.status['gaccess'][to]['gowner'][int(c)-1])
                              for a in range(k+1):
                                  if a == 0:self.mentionmention(to=to,status=self.status,text='',dataMid=d[:100],pl=-0,ps='   ✨ Del Gowner ✨\n',pg='DELGO',pt=d,silent=silent)
                                  else:self.mentionmention(to=to,status=self.status,text='',dataMid=d[a*100 : (a+1)*100],pl=a*100,ps='   ✨ Del Gowner ✨\n',pg='DELGO',pt=d,silent=silent)
                            self.backupData()
                    if txt.startswith("gcon"):
                      data = txt.replace("gcon","")
                      text = data.split(' ')
                      num = str(text[1])
                      gs = self.client.get_group(to) 
                      nama = [contact.mid for contact in gs.members]
                      num = str(text[1])
                      self.listcon(to,msg,num,self.status,nama)
                    if txt.startswith("add gadmin"):
                      targets = []
                      if msg.mentionees:
                        self.mention(msg,targets)
                        self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Add GAdmin ✨\n',pg='ADDGA',pt=targets,silent=silent)
                      self.backupData()
                    if txt.startswith("del gadmin"):
                      if to in self.status['gaccess']:
                            targets = []
                            if msg.mentionees:
                              self.mention(msg,targets)
                              self.mentionmention(to=to,status=self.status,text='',dataMid=targets,pl=0,ps='   ✨ Del GAdmin ✨\n',pg='DELGA',pt=targets,silent=silent)
                            else:
                              data = txt.replace("del gadmin","")
                              text = data.split(' ')
                              com = str(text[1])
                              selection = Archimed(com,range(1,len(self.status['gaccess'][to]['gadmin'])+1))
                              k = len(self.status['gaccess'][to]['gadmin'])//100
                              d = []
                              for c in selection.parse():
                                  d.append(self.status['gaccess'][to]['gadmin'][int(c)-1])
                              for a in range(k+1):
                                  if a == 0:self.mentionmention(to=to,status=self.status,text='',dataMid=d[:100],pl=-0,ps='   ✨ Del GAdmin ✨\n',pg='DELGA',pt=d,silent=silent)
                                  else:self.mentionmention(to=to,status=self.status,text='',dataMid=d[a*100 : (a+1)*100],pl=a*100,ps='   ✨ Del GAdmin ✨\n',pg='DELGA',pt=d,silent=silent)
                            self.backupData()         
                    if txt.startswith('tag'):
                      tt = txt.split(' ')
                      com = str(tt[1])
                      gs = self.client.get_group(to)
                      nama = [contact.mid for contact in gs.members]
                      no = 0
                      mids = []
                      selection = Archimed(com,range(1,len(nama)+1))
                      k = len(nama)//20
                      for a in range(k+1):
                        if a == 0:eto='    ✨ Tag Member ✨\n'
                        else:eto='    ✨ Tag Member ✨\n'
                        b=[]
                        text = ''
                        mids = []
                        no = 0
                        for i in selection.parse()[a*500 : (a+1)*500]:
                            mids.append(nama[i-1])
                        self.listdata(to,self.status,'Tag Member','tag',mids)
                    if txt == 'tempban':
                        if self.tempban == []:
                            if not silent:self.client.send_message(to,"Empty list")
                        else:
                            mc = ""
                            b = 0
                            for mi_d in self.tempban:
                                b = b + 1
                                end = '\n'
                                try:
                                   mc += str(b) + " • " +self.client.get_contact(mi_d).displayName + "\n"
                                except Exception as e:self.tempban.remove(mi_d);print("del {}".format(mi_d))
                            if not silent:self.client.send_message(to," Temporary Blacklist User:\n"+"\n"+mc)
                    if txt == 'banlist' or txt == 'blacklist':
                        if self.status["blacklist"] == []:
                            if not silent:self.client.send_message(to,"Empty list")
                        else:
                            mc = ""
                            b = 0
                            for mi_d in self.status["blacklist"]:
                                b = b + 1
                                end = '\n'
                                try:
                                   mc += str(b) + " • " +self.client.get_contact(mi_d).displayName + "\n"
                                except Exception as e:self.status["blacklist"].remove(mi_d);print("del {}".format(mi_d))
                            self.backupData()
                            if not silent:self.client.send_message(to,"  Blacklist user:\n"+"\n"+mc)
                    if txt == "contact":
                        self.client.send_contact(msg.to_id, self.uid)

                    if txt == 'name':
                            s = self.client.profile
                            if not silent:self.client.send_message(to,s.displayName)
                    if txt == "bots":
                            x = self.client.get_group(to)
                            nama = [contact.mid for contact in x.members]
                            targets = []
                            tot = []
                            for z in self.status['bot']:
                                if z not in tot:
                                    tot.append(z)
                            for s in self.status['squad']:
                                if s not in tot:
                                    tot.append(s)
                            for a in nama:
                                if a in self.status['bot'] or a in self.status['squad']:
                                    targets.append(a)
                            if not silent:self.client.send_message(to,"Bots in group: {}/{}.".format(len(targets),len(tot)))
                    if txt == "here":
                            x = self.client.get_group(to)
                            nama = [contact.mid for contact in x.members]
                            targets = []
                            with open('/root/register.json', 'r') as fp:
                              uka = json.load(fp)
                            for a in nama:
                                if a in uka:
                                    targets.append(a)
                            if not silent:self.client.send_message(to,"Bots in group: {}/{}.".format(len(targets),len(uka)))
                    if txt == 'find staff':
                            stf = []
                            gs = self.client.get_group(to) 
                            nama = [contact.mid for contact in gs.members]
                            for tag in self.status["owner"]:
                                stf+=filter(lambda str: str == tag, nama)
                            for tag in self.status["admin"]:
                                stf+=filter(lambda str: str == tag, nama)
                            for tag in self.status["staff"]:
                                stf+=filter(lambda str: str == tag, nama)
                            for tag in self.creator:
                                stf+=filter(lambda str: str == tag, nama)
                            if to in self.status['gaccess']:
                                rooma = self.status['gaccess'][to]
                                for tag in rooma['gowner']:
                                    stf+=filter(lambda str: str == tag, nama) 
                                for tag in rooma['gadmin']:
                                    stf+=filter(lambda str: str == tag, nama) 
                            self.listdata(to,self.status,'Bot Staff','bot',stf)
                    if txt == 'find gstaff':
                            stf = []
                            gs = self.client.get_group(to) 
                            nama = [contact.mid for contact in gs.members]
                            if to in self.status['gaccess']:
                                rooma = self.status['gaccess'][to]
                                for tag in rooma['gowner']:
                                    stf+=filter(lambda str: str == tag, nama) 
                                for tag in rooma['gadmin']:
                                    stf+=filter(lambda str: str == tag, nama) 
                                self.listdata(to,self.status,'Bot Staff','bot',stf)
                            else:self.client.send_message(to,"Group staff is empty.")
                    if txt == 'my grade':
                        if self.pangkat(to,saya) == 0:
                            if not silent:self.sendtag(to, " Hai @! My Creator","Encore-Bot Protect", [saya])
                        elif self.pangkat(to,saya) == 1:
                            if not silent:self.sendtag(to, " Hai @! My Owner","Encore-Bot Protect", [saya])
                        elif self.pangkat(to,saya) == 2:
                            if not silent:self.sendtag(to, " Hai @! My Admin","Encore-Bot Protect", [saya])
                        elif self.pangkat(to,saya) == 4:
                            if not silent:self.sendtag(to, " Hai @! My Staff","Encore-Bot Protect", [saya])
                        else:
                            pass
                    if txt == 'speed':
                        start = time.time()
                        self.client.send_message("u018d9e9ea188bc5f7f30b246eecd73d7", '.')
                        hasil = time.time()-start
                        if not silent:self.client.send_message(to, '✨ %.5f' % round(hasil,4)+ " ✨")
                        print(hasil)

                    if txt == "abort":
                            self.abort(to,silent)
                            self.backupData()
                            if not silent:self.client.send_message(to,"Command aborted.")
                    if txt == "commands":
                       rname = self.settings["rname"]
                       tst = "      ✨ ∆ "+self.settings["squad"]+" ∆ ✨ "+ "\n\n      ---✨ Commands ✨---"
                       num=0
                       num1=0
                       num2=0
                       num3=0
                       num4=0
                       with open('{}helpi.json'.format(self.letak),'r') as ini:
                            uh = json.load(ini)
                       mstr1 = uh["protect"]
                       mstr2 = uh["creator"]
                       mstr3 = uh["owner"]
                       mstr4 = uh["admin"]
                       mstr5 = uh["staff"]
                       num=(num+1)
                       num1=(num1+1)
                       num2=(num2+1)
                       num3=(num3+1)
                       num4=(num4+1)
                       if self.pangkat(to,msg.from_id) < 1:
                         tst += "\n\n       ♻ Creator ♻ "
                         for c in mstr2:
                           if num1 < 10:
                            tst += "\n %i.   %s %s "%(num1,rname,c)
                           else:
                            tst += "\n %i. %s %s "%(num1,rname,c)
                           num1=(num1+1)
                       tst += "\n\n        ♻ Protect Set ♻ "
                       for c in mstr1:
                           if num < 10:
                            tst += "\n %i.   %s %s "%(num,rname,c)
                           else:
                            tst += "\n %i. %s %s "%(num,rname,c)
                           num=(num+1)
                       if self.pangkat(to,msg.from_id) < 2:
                         tst += "\n\n        ♻ Owner ♻ "
                         for c in mstr3:
                           if num2 < 10:
                            tst += "\n %i.   %s %s "%(num2,rname,c)
                           else:
                            tst += "\n %i. %s %s "%(num2,rname,c)
                           num2=(num2+1)
                       if self.pangkat(to,msg.from_id) < 3:
                         tst += "\n\n        ♻ Admin ♻ "
                         for c in mstr4:
                           if num3 < 10:
                            tst += "\n %i.   %s %s "%(num3,rname,c)
                           else:
                            tst += "\n %i. %s %s "%(num3,rname,c)
                           num3=(num3+1)
                       if self.pangkat(to,msg.from_id) < 5:
                         tst += "\n\n        ♻ Staff ♻ "
                         for c in mstr5:
                           if num4 < 10:
                            tst += "\n %i.   %s %s "%(num4,rname,c)
                           else:
                            tst += "\n %i. %s %s "%(num4,rname,c)
                           num4=(num4+1)
                       tst += "\n\n✨ B£∆CK_∆NG€£ ✨"
                       if not silent:self.client.send_message(to,tst)
                    if txt == "help":
                        if rname in txt:ihik = rname
                        else:ihik = sname
                        md =  "   ∆✨"+self.settings["squad"]+"✨∆ "+ "\n\n  ---✨ List Help ✨---\n\n"
                        md += "• ✨" + ihik + "commands ✨" + "\n"
                        md += "• ✨" + ihik + "detail ✨" + "\n"
                        md += "\n\n✨ B£∆CK_∆NG€£ ✨"
                        if not silent:self.client.send_message(to,md)

                    if txt == "detail":
                        md =  "   ∆✨"+self.settings["squad"]+"✨∆ "+ "\n\n  ---✨ Detail ✨---\n\n"
                        md += "1. ✨ C = send contact ✨\n"
                        md += "2. ✨ R = <,>- ✨" + "\n"
                        md += "3. ✨ @ = need tag ✨" + "\n"
                        md += "4. ✨ all use rname or sname ✨" + "\n"
                        md += "\n\n✨ B£∆CK_∆NG€£ ✨"
                        if not silent:self.client.send_message(to,md)

                    if txt == 'set' or txt == "settings":
                        try: a = self.client.get_group(to).name
                        except: a = ''
                        md = "∆✨ "+self.settings["squad"]+" ✨∆\n ✨sᴇᴛ ᴘʟᴀɴ✨ \n\n• ✨ {} ✨ \n• ✨ sɴᴀᴍᴇ:   ".format(a) + sname+ " ✨\n• ✨ ʀɴᴀᴍᴇ:   "+ rname+ " ✨\n"
                        if to in self.settings["protect"]:
                            if self.settings["protect"][to] == 1:md+="⭕ ᴍᴀɪɴ ᴘʀᴏᴛᴇᴄᴛ      \n"
                            elif self.settings["protect"][to] == 2:md+="🚫 ᴍᴀɪɴ ᴘʀᴏᴛᴇᴄᴛ      \n"
                            else: md+= "❌ ᴍᴀɪɴ ᴘʀᴏᴛᴇᴄᴛ      \n"
                        if to in self.settings["cancel"]:
                            if self.settings["cancel"][to] == 1:md+="⭕ ᴅᴇɴʏɪɴᴠɪᴛᴇ      \n"
                            elif self.settings["cancel"][to] == 2:md+="🚫 ᴅᴇɴʏɪɴᴠɪᴛᴇ      \n"
                        else: md+= "❌ ᴅᴇɴʏɪɴᴠɪᴛᴇ       \n"
                        if self.settings["allowban"]: md+="⭕ ᴀʟʟᴏᴡʙᴀɴ     \n"
                        else: md+= "❌ ᴀʟʟᴏᴡʙᴀɴ      \n"
                        if to in self.settings["linkprotect"]:
                            if self.settings["linkprotect"][to] == 1:md+="⭕ ʟɪɴᴋᴘʀᴏᴛᴇᴄᴛ      \n"
                            elif self.settings["linkprotect"][to] == 2:md+="🚫 ʟɪɴᴋᴘʀᴏᴛᴇᴄᴛ     \n"
                        else: md+= "❌ ʟɪɴᴋᴘʀᴏᴛᴇᴄᴛ      \n"
                        if to in self.settings["blj"]: md+="⭕ ᴘᴊᴏɪɴ      \n"
                        else: md+= "❌ ᴘᴊᴏɪɴ       \n"
                        if to in self.settings["namelock"]: md+="⭕ ɴᴀᴍᴇʟᴏᴄᴋ          \n"
                        else: md+= "❌ ɴᴀᴍᴇʟᴏᴄᴋ          \n"
                        if self.settings["purge"]: md+="⭕ ᴀᴜᴛᴏᴘᴜʀɢᴇ      \n"
                        else: md+= "❌ ᴀᴜᴛᴏᴘᴜʀɢᴇ       \n"
                        if self.mode == 1:
                           if self.settings["war"]: md+="⭕ ᴡᴀʀ ᴍᴏᴅᴇ       \n"
                           else: md+= "❌ ᴡᴀʀ ᴍᴏᴅᴇ       \n"
                        if self.mode == 0:
                          if self.settings["antimode"]: md+="⭕ sᴛᴀɴᴅʙʏ ᴍᴏᴅᴇ      \n"
                          else: md+= "❌ sᴛᴀɴᴅʙʏ ᴍᴏᴅᴇ       \n"
                        if self.settings["lock"]: md+="⭕ ʟᴏᴄᴋ ᴍᴏᴅᴇ      \n"
                        else: md+= "❌ ʟᴏᴄᴋ ᴍᴏᴅᴇ       \n"
                        if self.settings["atjoin"]: md+="⭕ ᴀᴜᴛᴏᴊᴏɪɴ ᴜʀʟ     \n"
                        else: md+= "❌ ᴀᴜᴛᴏᴊᴏɪɴ ᴜʀʟ      \n"
                        if self.status["aadmin"]: md+="⭕ ᴀᴅᴅ ᴀᴅᴍɪɴ      \n"
                        else: md+= "❌ ᴀᴅᴅ ᴀᴅᴍɪɴ       \n"
                        if self.status["expel"]: md+="⭕ ᴇxᴘᴇʟ     \n"
                        else: md+= "❌ ᴇxᴘᴇʟ      \n"
                        if self.status["astaff"]: md+="⭕ ᴀᴅᴅ sᴛᴀғғ      \n"
                        else: md+= "❌ ᴀᴅᴅ sᴛᴀғғ       \n"
                        if self.status["abl"]: md+="⭕ ᴀᴅᴅ ʙʟ      \n"
                        else: md+= "❌ ᴀᴅᴅ ʙʟ       \n"
                        if self.status["abot"]: md+="⭕ ᴀᴅᴅ ʙᴏᴛ      \n"
                        else: md+= "❌ ᴀᴅᴅ ʙᴏᴛ       \n"
                        if self.status["repeat"]: md+="⭕ ʀᴇᴘᴇᴀᴛ      \n"
                        else: md+= "❌ ʀᴇᴘᴇᴀᴛ       \n"
                        if self.settings['nuke']: md+="⭕ ɴᴜᴋᴇ ʙᴏᴛ     \n"
                        else: md+= "❌ ɴᴜᴋᴇ ʙᴏᴛ       \n"
                        if not silent:self.client.send_message(msg.to_id,md + "\n   ●∆✨ B£∆CK_∆NG€£ ✨∆●   ")

                    if txt == "system" or txt == "about":
                        ac = subprocess.getoutput('lsb_release -a')
                        am = subprocess.getoutput('cat /proc/meminfo')
                        ax = subprocess.getoutput('lscpu')
                        core = subprocess.getoutput('grep -c ^processor /proc/cpuinfo ')
                        fri = len(self.client.refreshContacts())
                        bt = len(self.status['bot'])
                        eltime = time.time() - self.awit
                        cin = waktus(eltime)
                        duedate = str(self.duedate).split()[0]
                        python_imp = platform.python_implementation()
                        python_ver = platform.python_version()
                        if self.uid in self.client.authToken:aps = 'Primary'
                        else:aps = 'Secondary'
                        for line in ac.splitlines():
                            if 'Description:' in line:
                                osi = line.split('Description:')[1].replace('  ','')
                        for line in ax.splitlines():
                            if 'Architecture:' in line:
                                architecture =  line.split('Architecture:')[1].replace(' ','')
                        for line in am.splitlines():
                            if 'MemTotal:' in line:
                                mem = line.split('MemTotal:')[1].replace(' ','')
                            if 'MemFree:' in line:
                                fr = line.split('MemFree:')[1].replace(' ','')
                        md = "∆✨ "+self.settings["squad"]+" ✨∆\n    ✨ Information ✨ \n\n"
                        md +="• Squad:   {}\n".format(sname)
                        md +="• Rname:   {}\n".format(rname)
                        md +="• Friend's:   {}\n".format(fri)
                        md +="• Bot's:   {}\n".format(bt)
                        md +="• Bot Ver:   {}\n".format(Build)
                        md +="• Alive:   {}\n".format(cin)
                        md +="• Due:   {}\n".format(duedate)
                        md +="• Auth:   {}\n".format(aps)
                        md +="• Host:   www.hostinger.co.id\n"
                        md +="• OS:   {}\n".format(osi)
                        md +="• Lang:   {}\n".format(python_imp)
                        md +="• Ver:   {}\n".format(python_ver)
                        md +="• Architecture:   {}\n".format(architecture)
                        md +="• CPU Core:   {}\n".format(core)
                        md +="• Memory:   {}\n".format(mem)
                        md +="• Free:   {}\n\n".format(fr)
                        md += "\n✨ B£∆CK_∆NG€£ ✨"
                        if not silent:self.client.sendMessage(to,md)

                    if txt.startswith('denyinvite ') or txt == 'denyinvite':
                        if txt.startswith('denyinvite '):
                            jenis = txt.replace('denyinvite ','')
                            if jenis == 'on' or jenis == '1':
                                self.settings["cancel"][to] = 1
                                if not silent:self.client.send_message(msg.to_id, "Deny invite enabled.")
                            elif jenis == 'max' or jenis == '2':
                                self.settings["cancel"][to] = 2
                                if not silent:self.client.send_message(msg.to_id, "Deny Invite Protection max enabled.")
                            elif jenis == 'off' or jenis == '0':
                                del self.settings["cancel"][to]
                                if not silent:self.client.send_message(msg.to_id, "Deny invite disabled.")
                            self.backupData()
                        else:
                            md = '    ✨ sᴛᴀᴛᴜs ✨\n'
                            if to in self.settings["cancel"]:
                                if self.settings["cancel"][to] == 1:md+="• ʙʟᴏᴄᴋ ᴏɴʟʏ      → ⭕\n"
                                elif self.settings["cancel"][to] == 2:md+="• ᴍᴀx ᴘʀᴏᴛᴇᴄᴛ      → 🚫\n"
                                else: md+= "• ᴏғғ      → ❌\n"
                            else:md+= "• ᴏғғ      → ❌\n"
                            if not silent:self.client.send_message(msg.to_id, "{}\n ғᴏʀ sᴇᴛ:\n ✨ᴏғғ/0✨✨ᴏɴ/1✨✨ᴍᴀx/2✨".format(md))

                    if txt.startswith('namelock ') or txt == 'namelock':
                        if txt.startswith('namelock '):
                            jenis = txt.replace('namelock ','')
                            if jenis == 'on' or jenis == '1':
                                self.settings["namelock"][to] = {'on':1,'nama':self.client.get_group(to).name}
                                if not silent:self.client.send_message(msg.to_id, "Namelock enabled.")
                            elif jenis == 'off' or jenis == '0':
                                del self.settings["namelock"][to]
                                if not silent:self.client.send_message(msg.to_id, "Namelock disabled.")
                            self.backupData()
                        else:
                            md = '    ✨ sᴛᴀᴛᴜs ✨\n'
                            if to in self.settings["namelock"]:
                               md+="• ᴏɴ      → ⭕\n"
                            else:md+= "• ᴏғғ      → ❌\n"
                            if not silent:self.client.send_message(msg.to_id, "{}\n ғᴏʀ sᴇᴛ:\n ✨ᴏғғ/0✨✨ᴏɴ/1✨".format(md))

                    if txt.startswith('protect ') or txt == 'ready' or txt == 'close' or txt == 'protect' or txt == 'off' or txt == 'on':
                        if  txt.startswith('protect '):    
                            jenis = txt.replace('protect ','')
                            if jenis == 'on' or jenis == '1':
                                self.settings["protect"][to] = 1
                                if not silent:self.client.send_message(msg.to_id, "Protection enabled.")
                            elif jenis == 'max' or jenis == '2':
                                self.settings["protect"][to] = 2
                                if not silent:self.client.send_message(msg.to_id, "Protection max enabled.")
                            elif jenis == 'off' or jenis == '0' or jenis == 'none':
                                self.settings["protect"][to] = 0
                                if not silent:self.client.send_message(msg.to_id, "Protection disabled.")
                        elif txt == 'ready' or txt == 'on':
                                self.settings["protect"][to] = 1
                                if not silent:self.client.send_message(msg.to_id, "Bots Ready to Wars.")
                        elif txt == 'close' or txt == 'off':
                                self.settings["protect"][to] = 0
                                if not silent:self.client.send_message(msg.to_id, "Ok bye bye.")
                        elif txt == 'protect':
                            md = '    ✨ sᴛᴀᴛᴜs ✨\n'
                            if to in self.settings["protect"]:
                                if self.settings["protect"][to] == 1:md+="• sᴛᴀғғ ᴏɴʟʏ      → ⭕\n"
                                elif self.settings["protect"][to] == 2:md+="• ᴍᴀx ᴘʀᴏᴛᴇᴄᴛ      → 🚫\n"
                                else: md+= "• ᴏғғ      → ❌\n"
                            else:md+= "• ᴏғғ      → ❌\n"
                            if not silent:self.client.send_message(msg.to_id, "{}\n ғᴏʀ sᴇᴛ:\n ✨ᴏғғ/0✨✨ᴏɴ/1✨✨ᴍᴀx/2✨".format(md))
                        self.backupData()

                    if txt.startswith('linkprotect ') or txt == 'linkprotect':
                        if txt.startswith('linkprotect '):    
                            jenis = txt.replace('linkprotect ','')
                            if jenis == 'on' or jenis == '1':
                                self.settings["linkprotect"][to] = 1
                                if not silent:self.client.send_message(msg.to_id, "Protection url protection enabled.")
                            elif jenis == 'max' or jenis == '2':
                                self.settings["linkprotect"][to] = 2
                                if not silent:self.client.send_message(msg.to_id, "Url Max Protection enabled.")
                            elif jenis == 'off' or jenis == '0':
                                del self.settings["linkprotect"][to]
                                if not silent:self.client.send_message(msg.to_id, "Protection disabled.")
                            self.backupData()
                        else:
                            md = '    ✨ sᴛᴀᴛᴜs ✨\n'
                            if to in self.settings["linkprotect"]:
                                if self.settings["linkprotect"][to] == 1:md+="• ʙʟᴏᴄᴋ ᴏɴʟʏ      → ⭕\n"
                                elif self.settings["linkprotect"][to] == 2:md+="• ᴍᴀx ᴘʀᴏᴛᴇᴄᴛ      → 🚫\n"
                                else: md+= "• ᴏғғ      → ❌\n"
                            else:md+= "• ᴏғғ      → ❌\n"
                            if not silent:self.client.send_message(msg.to_id, "{}\n ғᴏʀ sᴇᴛ:\n ✨ᴏғғ/0✨✨ᴏɴ/1✨✨ᴍᴀx/2✨".format(md))

                    if txt == 'pjoin on' or txt == 'blj on':
                        if to in self.settings["blj"] :
                            if not silent:self.client.send_message(msg.to_id, "Block join already enabled.")
                        else:
                            self.settings["blj"][to] = True
                            self.backupData()
                            if not silent:self.client.send_message(msg.to_id, "Block join enabled.")

                    if txt == 'pjoin off' or txt == 'blj off':
                        if to in self.settings["blj"]:
                            del self.settings["blj"][to]
                            self.backupData()
                            if not silent:self.client.send_message(msg.to_id, "Allowing all joined members.")
                        else:
                            if not silent:self.client.send_message(msg.to_id, "Block join already disabled.")

                    if txt.startswith('protection ') or txt == 'protection':
                        if txt.startswith('protection '):
                            jenis = txt.replace('protection ','')
                            if jenis == 'on' or jenis == '1':
                                self.settings["cancel"][to] = 1
                                self.settings["linkprotect"][to] = 1
                                self.settings["protect"][to] = 1
                                self.settings["namelock"][to] = {'on':1,'nama':self.client.get_group(to).name}
                                if not silent:self.client.send_message(msg.to_id, "All protection enabled.")
                            elif jenis == 'max' or jenis == '2':
                                self.settings["cancel"][to] = 2
                                self.settings["linkprotect"][to] = 2
                                self.settings["protect"][to] = 2
                                self.settings["namelock"][to] = {'on':1,'nama':self.client.get_group(to).name}
                                if not silent:self.client.send_message(msg.to_id, "Maximal protection enabled.")
                            elif jenis == 'off' or jenis == '0':
                                if to in self.settings["cancel"]:
                                   del self.settings["cancel"][to]
                                if to in self.settings["linkprotect"]:
                                   del self.settings["linkprotect"][to]
                                self.settings["protect"][to] = 0
                                if to in self.settings["namelock"]:
                                   del self.settings["namelock"][to]
                                if to in self.settings["blj"]:
                                    del self.settings["blj"][to]
                                if not silent:self.client.send_message(msg.to_id, "All protection disabled.")
                            self.backupData()
                        else:
                            md = '    ✨ sᴛᴀᴛᴜs ✨\n'
                            if to in self.settings["cancel"]:
                                if self.settings["cancel"][to] == 1:md+="• ᴅᴇɴʏɪɴᴠɪᴛᴇ      → ⭕\n"
                                elif self.settings["cancel"][to] == 2:md+="• ᴅᴇɴʏɪɴᴠɪᴛᴇ      → 🚫\n"
                            else: md+= "• ᴅᴇɴʏɪɴᴠɪᴛᴇ       → ❌\n"
                            if to in self.settings["protect"]:
                                if self.settings["protect"][to] == 1:md+="• ᴍᴀɪɴ ᴘʀᴏᴛᴇᴄᴛ      → ⭕\n"
                                elif self.settings["protect"][to] == 2:md+="• ᴍᴀɪɴ ᴘʀᴏᴛᴇᴄᴛ      → 🚫\n"
                                else: md+= "• ᴍᴀɪɴ ᴘʀᴏᴛᴇᴄᴛ      → ❌\n"
                            if to in self.settings["linkprotect"]:
                                if self.settings["linkprotect"][to] == 1:md+="• ʟɪɴᴋᴘʀᴏᴛᴇᴄᴛ      → ⭕\n"
                                elif self.settings["linkprotect"][to] == 2:md+="• ʟɪɴᴋᴘʀᴏᴛᴇᴄᴛ      → 🚫\n"
                            else: md+= "• ʟɪɴᴋᴘʀᴏᴛᴇᴄᴛ      → ❌\n"
                            if to in self.settings["blj"]: md+="• ᴘᴊᴏɪɴ      → ⭕\n"
                            else: md+= "• ᴘᴊᴏɪɴ       → ❌\n"
                            if to in self.settings["namelock"]: md+="• ɴᴀᴍᴇʟᴏᴄᴋ          → ⭕\n"
                            else: md+= "• ɴᴀᴍᴇʟᴏᴄᴋ          → ❌\n"
                            if not silent:self.client.send_message(msg.to_id, "{}\n ғᴏʀ sᴇᴛ:\n ✨ᴏғғ/0✨✨ᴏɴ/1✨✨ᴍᴀx/2✨".format(md))

                    if txt == 'open link':
                            X = self.client.get_group(to)
                            X.preventedJoinByTicket = False
                            self.client.update_group(X)

                    if txt == 'close link':
                            X = self.client.get_group(to)
                            X.preventedJoinByTicket = True
                            self.client.update_group(X)

                    if txt == 'group link':
                            x = self.client.get_group(to)
                            if x.preventedJoinByTicket:
                                x.preventedJoinByTicket = False
                                self.client.update_group(x)
                            gurl = self.client.reissue_group_ticket(to)
                            if not silent:self.client.send_message(msg.to_id,"line://ti/g/" + gurl)

                    if txt == 'cancelall':
                            X = self.client.get_group(to)
                            if X.invitee is not None:
                                gInviMids = [contact.mid for contact in X.invitee]
                                for a in gInviMids:
                                   self.client.cancel_group_invitation(to, [a])
                                   time.sleep(1)

        if msg.content_type == 13:
                uid = msg.content_metadata["mid"]
                if self.pangkat(to,saya) < 1:
                    if self.status["aowner"]:
                      if uid in self.creator:
                            if not silent:self.sendtag(to,"User @! adalah creator.","Owner ADD",[uid])
                      else:
                        if uid not in self.status["owner"]:
                            self.status["owner"].append(uid)
                            try:
                                self.client.add_contact_by_mid(uid)
                            except:pass
                            if not silent:self.sendtag(to,"User @! added to owner.","Owner ADD",[uid])
                        else:
                            if not silent:self.sendtag(to,"User @! already on owner.","Owner ADD",[uid])
                        if uid in self.status["staff"]:
                                self.status["staff"].remove(uid)
                        if uid in self.status["bot"]:
                                self.status["bot"].remove(uid)
                        if uid in self.status["admin"]:
                                self.status["admin"].remove(uid)
                      if not self.status["repeat"]:
                          self.status["aowner"] = False
                    self.backupData()
                if self.pangkat(to,saya) < 2:
                    if self.addajs:
                        if uid not in self.status["anti"]:
                            self.status["anti"].append(uid)
                            self.client.add_contact_by_mid(uid)
                            self.backupData()
                            if not silent:self.client.send_message(to,"User %s added to all stay bot"%(self.client.get_contact(uid).displayName))
                        else:
                            if not silent:self.client.send_message(to,"%s already on stay bot"%(self.client.get_contact(uid).displayName))
                        if not self.status["repeat"]:
                            self.addajs = False
                    elif self.status["aadmin"]:
                      if uid in self.creator or uid in self.status["owner"]:
                            if not silent:self.sendtag(to,"User @! have higher grade.","Admin ADD",[uid])
                      else:
                        if uid not in self.status["admin"]:
                            self.status["admin"].append(uid)
                            try:
                                self.client.add_contact_by_mid(uid)
                            except:pass
                            if not silent:self.sendtag(to,"User @! added to admin list.","Admin ADD",[uid])
                        else:
                            if not silent:self.sendtag(to,"User @! already on admin list.","Admin ADD",[uid])
                        if uid in self.status["staff"]:
                                self.status["staff"].remove(uid)
                        if uid in self.status["bot"]:
                                self.status["bot"].remove(uid)
                      if not self.status["repeat"]:
                          self.status["aadmin"] = False
                    self.backupData()

                if self.pangkat(to,saya) < 3:
                    if self.status["astaff"]:
                      if uid in self.creator or uid in self.status["owner"]:
                            if not silent:self.sendtag(to,"User @! have higher grade.","Staff ADD",[uid])
                      else:
                        if uid not in self.status["staff"]:
                            self.status["staff"].append(uid)
                            try:
                                self.client.add_contact_by_mid(uid)
                            except:pass
                            if not silent:self.sendtag(to,"User @! added to staff.","Staff ADD",[uid])
                        else:
                            if not silent:self.sendtag(to,"User @! already on staff.","Staff ADD",[uid])
                        if uid in self.status["admin"]:
                                self.status["admin"].remove(uid)
                        if uid in self.status["bot"]:
                                self.status["bot"].remove(uid)
                      if not self.status["repeat"]:
                          self.status["astaff"] = False

                    if self.status["invite"]:
                            if uid in self.status["blacklist"]:
                                if not silent:self.sendtag(to,"Sorry, User @! in blacklist",[uid])
                            else:
                                target = uid
                                try:
                                    self.client.add_contact_by_mid(target)
                                    self.client.invite_into_group(to,[target])
                                    self.status["invite"] = False
                                except:
                                    if not silent:self.client.send_message(to,"Limit !")
                                    self.status["invite"] = False

                    if self.status["expel"]:
                        if self.pangkat(to,saya) < 3:
                            if uid in self.status["owner"]:
                              if self.pangkat(to,saya) < 1:
                                self.status["owner"].remove(uid)
                                if not silent:self.sendtag(to,"User @! expeled from owner.","Expel",[uid])
                            if uid in self.status["bot"]:
                                self.status["bot"].remove(uid)
                                if not silent:self.sendtag(to,"User @! expeled from bot.","Expel",[uid])
                            if uid in self.status["admin"]:
                              if self.pangkat(to,saya) < 2:
                                self.status["admin"].remove(uid)
                                if not silent:self.sendtag(to,"User @! expeled from admin.","Expel",[uid])
                            if uid in self.status["staff"]:
                                self.status["staff"].remove(uid)
                                if not silent:self.sendtag(to,"User @! expeled from staff.","Expel",[uid])
                            if uid in self.status["squad"]:
                              if self.pangkat(to,saya) < 2:
                                self.status["squad"].remove(uid)
                                if not silent:self.sendtag(to,"User @! expeled from bot.","Expel",[uid])
                        if not self.status["repeat"]:
                            self.status["expel"] = False

                    if self.status["abl"]:
                        if self.pangkat(to,saya) < 5:
                            if self.pangkat(to,uid) < 5:
                              if not silent:self.sendtag(to,"User @! already on user access.",[uid])
                            else:
                                if uid not in self.status["blacklist"]:
                                   self.status["blacklist"].append(uid)
                                   if not silent:self.sendtag(to,"User @! added to blacklist.",[uid])
                                else:self.sendtag(to,"User @! already on blacklist.",[uid])
                        if not self.status["repeat"]:
                            self.status["abl"] = False

                    if self.status["abot"]:
                        if self.pangkat(to,saya) < 3:
                            if uid in self.status["admin"]:
                                self.status["admin"].remove(uid)
                            if uid in self.status["staff"]:
                                self.status["staff"].remove(uid)
                            if self.pangkat(to,uid) == 1:
                                if not silent:self.sendtag(to,"User @! already in owner.",[uid])
                            if uid not in self.status["bot"]:
                                   self.status["bot"].append(uid)
                                   if not silent:self.sendtag(to,"User @! added to bot list.",[uid])
                        if not self.status["repeat"]:
                            self.status["abl"] = False
                    self.backupData()
        if msg.content_type == 1:
            if self.pangkat(to,saya) < 2:
                    if self.status['picture']:
                        xpath = self.client.downloadObjectMsg(msg.id)
                        self.client.updateProfilePicture(xpath)
                        if not silent:self.client.send_message(to, "Profile picture successfully updated.")
                        self.client.deleteFile(xpath)
                        self.status['picture'] = False
                        self.backupData()
                    elif self.status['cvp']:
                        try:
                            path = self.client.downloadObjectMsg(msg.id)
                            self.status['gpic']['pic'] = path
                            self.backupData()
                            self.client.changecpvv(to,self.status)
                            if not silent:self.client.send_message(to, " ✨ Video profile successfully updated. ✨")
                        except Exception as e:                   
                            if not silent:self.client.send_message(msg.to_id,"✨ {} ✨".format(e))
                    elif self.adc:
                           self.cover(msg)
                           self.adc = False
        if msg.content_type == 2:
                       if self.status['cvp']:
                        try:
                            path = self.client.downloadObjectMsg(msg.id)
                            self.status['gpic']['pic'] = ''
                            self.status['gpic']['vid'] = path
                            self.backupData()
                            self.client.changecpvv(to,self.status)
                        except Exception as e:
                            if not silent:self.client.send_message(to,str(e))

      except TalkException as talk_error:
          e = traceback.format_exc()
          if "EOFError" in e:
              pass
          elif 'code=20' in e:
              self.backupData()
              time.sleep(5)
              python3 = sys.executable
              os.execl(python3, python3, *sys.argv)
          elif 'code=7' in e:
              self.backupData()
              sys.exit('AUTH FAILED')
          elif 'code=8' in e:
              self.backupData()
              time.sleep(5)
              python3 = sys.executable
              os.execl(python3, python3, *sys.argv)
          else:
            self.logError(e)
            print('error')
