import socket
import wx
import PacketManager
import urllib2
import traceback
import threading
import struct

#Eclipse pyDev error fix
wx=wx

EntityID = 0

class ServerConnection(threading.Thread):
    
    def __init__(self, window, username, password, sessionID, server, port):
        threading.Thread.__init__(self)
        self.username = username
        self.password = password
        self.sessionID = sessionID
        self.server = server
        self.port = port
        if(window == None):
            self.NoGUI = True
        self.window = window
        
    def run(self):
        self.socket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
        try:
            self.socket.connect ( ( self.server, self.port ) )
            PacketManager.sendHandshake(self.socket, self.username, self.server, self.port)
            if(self.socket.recv(1) == "\x02"):
                response = PacketManager.handle02(self.socket)
            else:
                print "Server responded with a malformed packet"
                pass
            serverid = response
            if(serverid != '-'):
                url = "http://session.minecraft.net/game/joinserver.jsp?user=" + self.username + "&sessionId=" + self.sessionID + "&serverId=" + serverid
                response = urllib2.urlopen(url).read()
                if(response != "OK"):
                    if(self.NoGUI == False):
                        self.window.connectStatus.SetLabel("Response from sessions.minecraft.net wasn't OK")
                    else:
                        print "Response from sessions.minecraft.net wasn't OK, it was " + response
                    return False
                PacketManager.sendLoginRequest(self.socket, self.username)
                PacketListener(self.window, self.socket).start()
            else:
                print "Server is in offline mode"
                PacketManager.sendLoginRequest(self.socket, self.username)
        except Exception, e:
            if(self.NoGUI == False):
                self.window.connectStatus.SetForegroundColour(wx.RED)
                self.window.connectStatus.SetLabel("Connection to server failed")
            else:
                print "Connection to server failed"
            traceback.print_exc()
            return False
        
class PacketListener(threading.Thread):
    
    def __init__(self, window, socket):
        threading.Thread.__init__(self)
        self.socket = socket
        self.window = window
        
    def run(self):
        self.socket.settimeout(60)
        while True:
            try:
                response = self.socket.recv(1)
            except socket.timeout, e:
                if(self.NoGUI == False):
                    self.window.connectStatus.SetLabel("Ping timeout")
                else:
                    print "Ping timeout"
                break
            print hex(ord(response[0]))
            if(response[0] == "\x00"):
                PacketManager.handle00(self.socket)
            if(response[0] == "\x01"):
                PacketManager.handle01(self.socket)
            if(response[0] == "\x03"):
                PacketManager.handle03(self.socket)
            if(response[0] == "\x04"):
                PacketManager.handle04(self.socket)
            if(response[0] == "\x05"):
                PacketManager.handle05(self.socket)
            if(response[0] == "\x06"):
                PacketManager.handle06(self.socket)
            if(response[0] == "\x07"):
                PacketManager.handle07(self.socket)
            if(response[0] == "\x08"):
                PacketManager.handle08(self.socket)
            if(response[0] == "\x09"):
                PacketManager.handle09(self.socket)
            if(response[0] == "\x0D"):
                PacketManager.handle0D(self.socket)
            if(response[0] == "\x11"):
                PacketManager.handle11(self.socket)
            if(response[0] == "\x12"):
                PacketManager.handle12(self.socket)
            if(response[0] == "\x14"):
                PacketManager.handle14(self.socket)
            if(response[0] == "\x15"):
                PacketManager.handle15(self.socket)
            if(response[0] == "\x16"):
                PacketManager.handle16(self.socket)
            if(response[0] == "\x17"):
                PacketManager.handle17(self.socket)
            if(response[0] == "\x18"):
                print PacketManager.handle18(self.socket)
            if(response[0] == "\x1A"):
                PacketManager.handle1A(self.socket)
            if(response[0] == "\x1C"):
                PacketManager.handle1C(self.socket)
            if(response[0] == "\x1D"):
                PacketManager.handle1D(self.socket)
            if(response[0] == "\x1E"):
                PacketManager.handle1E(self.socket)
            if(response[0] == "\x20"):
                PacketManager.handle20(self.socket)
            if(response[0] == "\x21"):
                PacketManager.handle21(self.socket)
            if(response[0] == "\x22"):
                PacketManager.handle22(self.socket)
            if(response[0] == "\x23"):
                PacketManager.handle23(self.socket)
            if(response[0] == "\x26"):
                PacketManager.handle26(self.socket)
            if(response[0] == "\x27"):
                PacketManager.handle27(self.socket)
            if(response[0] == "\x28"):
                PacketManager.handle28(self.socket)
            if(response[0] == "\x29"):
                PacketManager.handle29(self.socket)
            if(response[0] == "\x2A"):
                PacketManager.handle2A(self.socket)
            if(response[0] == "\x2B"): 
                PacketManager.handle2B(self.socket)
            if(response[0] == "\x32"):
                PacketManager.handle32(self.socket)
            if(response[0] == "\x33"):
                PacketManager.handle33(self.socket)
            if(response[0] == "\x34"):
                PacketManager.handle34(self.socket)
            if(response[0] == "\x35"):
                PacketManager.handle35(self.socket)
            if(response[0] == "\x36"):
                PacketManager.handle36(self.socket)
            if(response[0] == "\x3C"):
                print PacketManager.handle3C(self.socket)
            if(response[0] == "\x3D"):
                PacketManager.handle3D(self.socket)
            if(response[0] == "\x46"):
                PacketManager.handle46(self.socket)
            if(response[0] == "\x47"):
                PacketManager.handle47(self.socket)
            if(response[0] == "\x64"):
                PacketManager.handle64(self.socket)
            if(response[0] == "\x65"):
                PacketManager.handle65(self.socket)
            if(response[0] == "\x67"):
                PacketManager.handle67(self.socket)
            if(response[0] == "\x68"):
                PacketManager.handle68(self.socket)
            if(response[0] == "\x69"):
                PacketManager.handle69(self.socket)
            if(response[0] == "\x6A"):
                PacketManager.handle6A(self.socket)
            if(response[0] == "\x6B"):
                PacketManager.handle6B(self.socket)
            if(response[0] == "\x82"):
                PacketManager.handle82(self.socket)
            if(response[0] == "\x83"):
                PacketManager.handle83(self.socket)
            if(response[0] == "\x84"):
                PacketManager.handle84(self.socket)
            if(response[0] == "\xC8"):
                PacketManager.handleC8(self.socket)
            if(response[0] == "\xC9"):
                print PacketManager.handleC9(self.socket)
            if(response[0] == "\xCA"):
                print PacketManager.handleCA(self.socket)
            if(response[0] == "\xFA"):
                print PacketManager.handleFA(self.socket)
            if(response[0] == "\xFF"):
                DisconMessage = PacketManager.handleFF(self.socket)
                if(self.window == None):
                    print "Disconnected: " + DisconMessage
                else:
                    self.window.connectStatus.SetLabel("Disconnected: " + DisconMessage)
                break
    