from asyncore import dispatcher
from asynchat import async_chat
import socket,asyncore

PORT = 5005
NAME = 'TestChat'

class EndSeesion(Exception):
	pass

class CommandHandler:
	'''
	类似于标准库中的cmd.Cmd的简单命令处理程序
	'''
	def unknown(self,session,cmd):
		'响应未知命令'
		msg = 'Unknown command:{}\r\n'.format(cmd)
		session.push(msg.encode())

	def handle(self,session,line):
		'处理从指定会话收到的行'
		#如果line为空,忽略
		if not line.strip():
			pass
		#提取命令
		parts = line.split(' ',1)
		cmd = parts[0]
		try:
			line = parts[1].strip()
		except IndexError:
			line = ''
		#尝试查询处理程序
		method = getattr(self,'do_'+cmd,None)
		try:
			#假设它是可调用的
			method(session,line)
		except TypeError:
			#不可调用，响应位置命令
			self.unknown(session,cmd)

class Room(CommandHandler):
	'''
	可能包含一个或多个用户（会话）的通用环境
	负责基本的命令处理和广播
	'''	

	def __init__(self,server):
		self.server = server
		self.sessions = []

	def add(self,session):
		'有会话（用户）进入聊天室'
		self.sessions.append(session)

	def remove(self,session):
		'有会话（用户）离开聊天室'
		self,sessions.remove(session)

	def broadcast(self,line):
		'将一行内容发送给聊天室内所有会话'
		for session in self.sessions:
			session.push(line.encode())

	def do_logout(self,session,line):
		'响应命令logout'
		raise EndSeesion

class LoginRoom(Room):
	'''
	为刚连接的用户准备的聊天室
	'''
	def add(self,session):
		Room.add(self,session)
		#用户进入时，发出问候
		msg = 'Welcome to {}\r\n'.format(self.server.name)
		self.broadcast(msg)

	def unknown(self,session,cmd):
		#除login和logout命令外都会导致系统提示消息
		msg = 'Please log in,input"login <name>\r\n"'
		session.push(msg.encode())

	def do_login(self,session,line):
		name = line.strip()
		#确保输入了用户名
		if not name:
			msg = 'Please log in,input"login <name>\r\n"'
			session.push(msg.encode())
		#确保用户名未被占用
		elif name in self.server.users:
			msg1 = 'The name {} is taken\r\n'.format(name)
			msg2 = 'Please try again.\r\n'
			session.push(msg1.encode())
			session.push(msg2.encode())
		else:
			#用户名没有问题，储存到会话中并将用户移到聊天室
			session.name = name
			session.enter(self.server.main_room)

class ChatRoom(Room):
	'''
	为多个用户相互聊天准备的聊天室
	'''
	def add(self,session):
		#告诉所有用户有新用户进来
		self.broadcast(session.name+'has entered the room.\r\n')
		self.server.users[session.name] = session
		Room.add(self,session)

	def remove(self,session):
		Room.remove(self,session)
		#告诉所有人有用户离开
		self.broadcast(session.name + 'has left the room.\r\n')

	def do_say(self,session,line):
		self.broadcast(session.name + ': ' + line + '\r\n')

	def do_look(self,session,line):
		'处理命令look,这个命令用于查看聊天室李都有谁'
		msg = other.name + '\r\n'
		session.push(msg.encode())

	def do_who(self,session,line):
		'处理命令who，这个命令用于查看聊天室里都有谁'
		msg = name+'\r\n'
		session.push(msg.encode())


class Logout(Room):
	'''
	为单个用户准备的聊天室，仅用于将用户从服务器中删除
	'''
	def add(self,session):
		#将进入LogoutRoom的用户删除
		try:
			del self.server.users[session.name]
		except KeyError:
			pass

class ChatSession(async_chat):
	'''
	单个会话，负责与单个用户对话
	'''
	def __init__(self,server,sock):
		super().__init__(sock)
		self.server = server
		self.set_terminator('\r\n')
		self.data = []
		self.name = None
		#所有会话最初都位于LoginRoom
		self.enter(LoginRoom(server))

	def enter(self,room):	
		#从当前聊天室离开，进入下一个聊天室
		try:
			cur = self.room
		except AttributeError:
			pass
		else:
			cur.remove(self)
			self.room = room
			room.add(self)

	def collect_incoming_data(self,data):
		bianma = chardet.detect(data)['encoding']
		print(bianma)
		if bianma == 'utf-8':
			data = data.decode()
			print(data)
			self.data.append(data)	
		elif bianma == 'ascii':
			data = data.decode('ascii')
			print(data)
			self.data.append(data)
		else:
			pass

	def found_terminator(self):
		line = ''.join(self.data)
		self.data = []
		try:
			self.room.handle(self,line)
		except EndSeesion:
			self.handle_close()

	def handle_close(self):
		async_chat.handle_close(self)
		self.enter(LoginRoom(self.server))

class ChatServer(dispatcher):
	'''
	只有一个聊天室的聊天服务器
	'''
	def __init__(self,port,name):
		super().__init__()
		self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind(('',port))
		self.listen(5)
		self.name = name 
		self.users = {}
		self.main_room = ChatRoom(self)

	def handle_accept(self):
		conn,addr = self.accept()
		ChatSession(self,conn)

if __name__ == '__main__':
	s = ChatServer(PORT,NAME)
	try:
		asyncore.loop()
	except KeyboardInterrupt:
		print()		
