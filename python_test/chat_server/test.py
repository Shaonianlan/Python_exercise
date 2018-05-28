from asyncore import dispatcher
from asynchat import async_chat
import socket,asyncore
import chardet

PORT = 5005
NAME = 'TestChat'

class ChatSession(async_chat):
	'''
	一个负责处理服务器和单个用户连接的类
	'''
	def __init__(self,server,sock):
		#设置任务 初始化
		async_chat.__init__(self,sock)
		self.server = server
		self.set_terminator(('\r\n').encode())
		self.data = []
		#问候用户
		self.push(('Welcome to %s\r\n' 0% self.server.name).encode())

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
		'''
		如果遇到结束符，就意味着读取了一整行，
		一次将这行内容广播给每一个人
		'''
		line = ''.join(self.data)
		self.data = []
		self.server.broadcast(line)

	def handle_close(self):
		async_chat.handle_close(self)
		self.server.disconnect(self)	
	

class ChatServer(dispatcher):
	'''
	一个接受连接并创建对话的类，他还负责向这些会话广播
	'''
	def __init__(self,port,name):
		#设置任务
		dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind(('',port))
		self.listen(5)
		self.name = name
		self.sessions = []	

	def disconnect(self,session):
		self.sessions.remove(session)

	def broadcast(self,line):
		for session in self.sessions:
			session.push((line+'\r\n').encode())

	def handle_accept(self):
		conn, addr = self.accept()
		print('Connection attempt from',addr)
		self.sessions.append(ChatSession(self,conn))

if __name__ == '__main__':
	s = ChatServer(PORT,NAME)
	try: asyncore.loop()
	except KeyboardInterrupt:pass								