'''
Created by auto_sdk on 2015.04.21
'''
from aliyun.api.base import RestApi
class Ecs20140526DescribeInstanceMonitorDataRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.EndTime = None
		self.InstanceId = None
		self.Period = None
		self.StartTime = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.DescribeInstanceMonitorData.2014-05-26'
