# -*- coding: utf-8 -*-
import os.path
'''File management classes and methods'''

class FileError(Exception):
	'''Exception raised for errors accessing and manipulating files.
	
	Attributes:
		path -- path to the file that is generating the errors
		msg -- explanation of the errors
        '''
	def __init__(self, path, msg):
		self.path = path
		self.msg = msg
		
class FileInterface(object):
	'''Base class that holds the basic operation files
	   
	Attributes:
		path -- path to the file	
	'''
	
	def __init__(self,filePath):
		'''builds the file interface, if file does not exist
		raises a file error.
		'''
		if os.path.isfile(filePath):
			self.filePath = filePath 
		else: 
			raise FileError(self.filePath,'File does not exist')
		
class PlainTextFileHandler(FileInterface):
	'''Plain text file handler
	
	Attributes:
		fd -- the file descriptor used for this file.
		mode -- equivalent to file open modes. See built-in open() function
	'''
	_mode = 'r'
	
	def __init__(self,filePath,mode='r'):
		super(PlainTextFileHandler, self).__init__(filePath)
		self.fd = None
		self.mode = mode
		
	@property
	def mode(self):
		return self._mode
		
	@mode.setter	
	def mode(self, mode):
		'''set the mode to open the file '''
		self._mode = str(mode)

	def __enter__(self):
		self.fd = open(self.filePath, mode=self.mode)
	
	def __exit__(self, type, value, tb):
		self.fd.close()
		self.fd = None
		
	def __getattr__(self, attr):
		if self.fd and hasattr(self.fd, attr):
			def wrapper(*args, **kw):
				return getattr(self.fd, attr)(*args, **kw)
			return wrapper
		raise AttributeError(attr)
		
	#to implement getter setter     things read this (use for mode attr) 	
	#https://docs.python.org/2/library/functions.html#property
	
	
		
