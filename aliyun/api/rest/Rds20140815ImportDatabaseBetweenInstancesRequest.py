'''
Created by auto_sdk on 2015.04.21
'''
from aliyun.api.base import RestApi
class Rds20140815ImportDatabaseBetweenInstancesRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DBInfo = None
		self.DBInstanceId = None
		self.SourceDBInstanceId = None

	def getapiname(self):
		return 'rds.aliyuncs.com.ImportDatabaseBetweenInstances.2014-08-15'
