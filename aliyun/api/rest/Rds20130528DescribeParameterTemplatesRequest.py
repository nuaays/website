'''
Created by auto_sdk on 2015.04.21
'''
from aliyun.api.base import RestApi
class Rds20130528DescribeParameterTemplatesRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.Engine = None
		self.EngineVersion = None

	def getapiname(self):
		return 'rds.aliyuncs.com.DescribeParameterTemplates.2013-05-28'
