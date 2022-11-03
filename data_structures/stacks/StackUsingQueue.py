#to implement this program we use double queue to implement stack
#from one end we insert the element from one end of the queue and delete from other end of the queue
from _collections import deque
class Stack:

	def __init__(self):
		self.q1 = deque()
		self.q2 = deque()

	def push(self, x):
		self.q2.append(x)
		while (self.q1):
			self.q2.append(self.q1.popleft())
		self.q1, self.q2 = self.q2, self.q1

	def pop(self):
		if self.q1:
			self.q1.popleft()

	def top(self):
		if (self.q1):
			return self.q1[0]
		return None

	def size(self):
		return len(self.q1)

if __name__ == '__main__':
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)

	print("current size: ", s.size())
	print(s.top())
	s.pop()
	print(s.top())
	s.pop()
	print(s.top())

	print("current size: ", s.size())
