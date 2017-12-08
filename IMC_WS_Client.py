# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')  # python的str默认是ascii编码，和unicode编码冲突,把 str 编码由 ascii 改为 utf8
from suds.client import Client
import json
from suds import cache

# import logging
#
# logging.basicConfig(level=logging.INFO)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logging.getLogger('suds.transport').setLevel(logging.DEBUG)
# logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
# logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)

header = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Connection': 'keep-alive',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'}

service_list = {'1': 'imcplatResServiceWithPolicy', '2': 'customQueryService', '3': 'imcperfService',
                '4': 'imcplatResService', '5': 'imcplatTestService', '6': 'acmUserService', '7': 'feeService',
                '8': 'imcplatServiceWithPolicy', '9': 'imcplatUserService', '10': 'Version',
                '11': 'imcplatOperatorService', '12': 'imcplatService', '13': 'imcplatOperatorServiceWithPolicy'}

# WSDL File URL
imcplatResServiceWithPolicy = 'http://172.21.160.114:8080/imcws/services/imcplatResServiceWithPolicy?wsdl'  # n
'''# Service Description : imcplatResServiceWithPolicy?wsdl'
# Service Status : Active
# Available Operations  
#    modifyDevIfAdminStatusForWS 
#    RequestSecurityToken
#    queryDataBySQL
#    queryDeviceByIpForWS
#    queryIfsByIpForWS
'''
customQueryService = 'http://172.21.160.114:8080/imcws/services/customQueryService?wsdl'  # num2
'''# Service Description : customQueryService
# Service Status : Active
# Available Operations 
#    multiQuery
 #    singleQuery'''
imcperfService = 'http://172.21.160.114:8080/imcws/services/imcperfService?wsdl'  # num3
'''# Service Description : imcperfService
# Service Status : Active
# Available Operations
#    queryIndexHisData
#    queryIndexInstance
#    queryIndexData'''
imcplatResService = 'http://172.21.160.114:8080/imcws/services/imcplatResService?wsdl'  # num4
'''# Service Description : imcplatResService
# Service Status : Active
# Available Operations
#    queryIfsByIpForWS
#    queryDataBySQL
#    modifyDevIfAdminStatusForWS
#    queryDeviceByIpForWS'''
imcplatTestService = 'http://172.21.160.114:8080/imcws/services/imcplatTestService?wsdl'  # num5
'''# Service Description : imcplatTestService
# Service Status : Active
# Available Operations
#    queryById'''
acmUserService = 'http://172.21.160.114:8080/imcws/services/acmUserService?wsdl'  # num6
'''# Service Description : acmUserService
# Service Status : Active
# Available Operations

#    querySyncPolicyUserInfoList
#    queryAcmUserByPlatUserId
#    queryBlackList
#    randomReq
#    forceDelete
#    cancelAcmUser
#    kickOut
#    addAcmUser
#    applyService
#    queryAcmUserPassword
#    modifyAcmUserCreateTime
#    queryServiceTemplateList
#    modifyAcctUser
#    queryAcctByName
#    modifyAcmUser
#    queryAcmOnlineUserList
#    cancelAcctUser
#    cancelService
#    sendMessage
#    queryAcmUser
#    queryAcmUserFullInfo
#    modifyInvalidTime
#    querySyncPolicyInfoList
#    cancelBindingUser
#    modifyUserPassword
#    addBindingUser
#    forceLogout
#    queryAcmUserServiceInfo
#    queryAcmUserList
#    clearOnlineInfo
#    queryAcmAccessDetailList
#    queryParameterByName
#    removeBlackList
#    addBlackList
'''
feeService = 'http://172.21.160.114:8080/imcws/services/feeService?wsdl'  # num7
'''# Service Description : feeService
# Service Status : Active
# Available Operations

#    selfPay
#    suspendUserById
#    pay
#    cancelSuspendUserById
#    queryBillDetailByBillId
#    queryBillByUserId
#    queryBalance
#    queryPaymentRecord
#    randomReq
#    queryAcmUserService
'''
imcplatServiceWithPolicy = 'http://172.21.160.114:8080/imcws/services/imcplatServiceWithPolicy?wsdl'  # num8
'''# Service Description : imcplatServiceWithPolicy
# Service Status : Active
# Available Operations

#    logout
#    RequestSecurityToken
#    login
'''
imcplatUserService = 'http://172.21.160.114:8080/imcws/services/imcplatUserService?wsdl'  # num9
'''# Service Description : imcplatUserService
# Service Status : Active
# Available Operations
# 
#    cancelUserForPreReg
#    addUserForPreReg
#    queryUserById
#    deleteUserGroup
#    queryUserByNameAndIdentity
#    modifyUser
#    addUser
#    modifyUserGroup
#    addUserGroup
#    changeUserGroup
#    queryAllUser
#    modifyUserForPreReg
#    queryUserByIdForPreReg
#    queryAllUserAppendsForPreRegister
#    cancelUser
#    queryAllUserGroup
#    queryUserByNameAndIdentityForPreReg
#    queryUserGroupById
#    queryAllUserAppend
'''
Version = 'http://172.21.160.114:8080/imcws/services/Version?wsdl'  # num10
'''
# Service Description : Version
# Service Status : Active
# Available Operations
#    getVersion
# imcplatUserServiceWithPolicy='http://172.21.160.114:8080/imcws/services/imcplatUserServiceWithPolicy?wsdl'
# Service Description : imcplatUserServiceWithPolicy
# Service Status : Active
# Available Operations

#    addUserForPreReg
#    queryUserById
#    RequestSecurityToken
#    queryUserByNameAndIdentityForPreReg
#    addUser
#    cancelUser
#    queryAllUserAppendsForPreRegister
#    queryAllUser
#    queryAllUserGroup
#    modifyUserForPreReg
#    queryUserGroupById
#    queryUserByIdForPreReg
#    modifyUser
#    queryAllUserAppend
#    queryUserByNameAndIdentity
#    cancelUserForPreReg
'''
imcplatOperatorService = 'http://172.21.160.114:8080/imcws/services/imcplatOperatorService?wsdl'  # num11
'''
# Service Description : imcplatOperatorService
# Service Status : Active
# Available Operations

#    insertLog
#    isOperatorExisted
#    queryUserGroupsOfOperatorName
#    modifyPassword
'''
imcplatService = 'http://172.21.160.114:8080/imcws/services/imcplatService?wsdl'  # num12
''' Service Description : imcplatService
# Service Status : Active
# Available Operations

#    logout
#    login
'''

imcplatOperatorServiceWithPolicy = 'http://172.21.160.114:8080/imcws/services/imcplatOperatorServiceWithPolicy?wsdl'  # num13
'''
 Service Description : imcplatOperatorServiceWithPolicy
 Service Status : Active
 Available Operations
    modifyPassword
    RequestSecurityToken
    queryUserGroupsOfOperatorName
    isOperatorExisted
    insertLog
'''


def login():
    url = imcplatService
    username = raw_input("Enter the username:")
    password = raw_input('Enter the password:')
    client = Client(url)
    client.service.login(username, password)  # 调用imcplatService服务下的login方法登录。
    print client.options.transport.cookiejar
    return client.options.transport.cookiejar


def logout():
    url = imcplatService
    client = Client(url)
    client.service.logout()  # 调用imcplatService服务下的logout方法注销。


def get_service_url():
    print 'number\tService\'s Name'
    for i in range(1, 14):  # 顺序输出字典类型的无序服务列表
        for key in service_list:
            if int(key) == i:
                print key, '\t\t', service_list[key]
    print '\r'
    num = raw_input('input the Service\'s number you want query:')
    if num == '1':
        return imcplatResServiceWithPolicy
    elif num == '2':
        return customQueryService
    elif num == '3':
        return imcperfService
    elif num == '4':
        return imcplatResService
    elif num == '5':
        return imcplatTestService
    elif num == '6':
        return acmUserService
    elif num == '7':
        return feeService
    elif num == '8':
        return imcplatServiceWithPolicy
    elif num == '9':
        return imcplatUserService
    elif num == '10':
        return Version
    elif num == '11':
        return imcplatOperatorService
    elif num == '12':
        return imcplatService
    elif num == '13':
        return imcplatServiceWithPolicy


def query_wsdl_service(url):
    client = Client(url)
    print client


def acm_user_service_query():
    url = acmUserService
    client = Client(url)
    client.set_options(port='acmUserServiceHttpSoap12Endpoint')
    client.set_options(headers=header)
    print client.set_options(headers=header)
    client.options.transport.cookiejar = login()
    AcmUserListQueryParam = client.factory.create('ns0:AcmUserListQueryParam')  # 创建参数工厂模式
    # print AcmUserListQueryParam

    AcmUserListQueryParam = {"accountName": "",  # 帐号名 系统中唯一标识一个接入用户帐号。数据类型：字符串约束条件：最大长度为32个字符。
                             "boundDomain": "",  # 绑定域名称 数据类型：字符串 约束条件：最大长度为256个字符。
                             "computerName": "",  # 计算机名称 数据类型：字符串 约束条件：最大长度为256个字符。
                             "contactAddress": "",  # 通讯地址 数据类类型：字符串 约束条件：最大长度为39个字符
                             "creationEndDate": None,  # 开户结束日期 数据类型：日期 约束条件：格式为“yyyy-MM-dd””。
                             "creationStartDate": None,
                             # 开户起始日期 数据类型：日期  约束条件：格式为“yyyy-MM-dd”，日期和时间之间用字母“T”连接，当开户起始日期和结束日期同时存在时，起始日期必须小于或等于结束日期。
                             "deviceEndIp": "",  # 设备IP地址结束值 数据类型：字符串 约束条件
                             "deviceStartIp": "",  # 设备IP起始地址 数据类型：字符串 约束条件：IPv4。当设备IP地址起始值和结束值同时有值时，起始值必须小于或等于结束值。
                             "email": "",  # 电子邮件 数据类型：字符串 约束条件：最大长度为32个字符。
                             "feeType": None,  # 账号付费类型  0 免费 2 预付费 3 后付费 数据类型：整型 约束条件：无。
                             "fullName": "",  # 用户姓名 数据类型：字符串 约束条件：最大长度为32个字符。
                             "guest": None,  # 访问人 数据类型：字符串 约束条件：无。
                             "guestDepartment": "",  # 访问单位 数据类型：字符串 约束条件：无。
                             "guestManagerId": None,  # 可管理该访客的普通接入帐号ID 数据类型：字符串 约束条件：无。
                             "identityNumber": None,  # 证件号码 数据类型：字符串 约束条件：最大长度为32个字符。
                             "ifManageGuest": None,  # 可否管理访客 0 不可以 1 可以 数据类型：整型 约束条件：无。
                             "innerVlanId": -9999,  # VLAN ID/内层VLAN ID 数据类型：长整型 约束条件：[-9999 - 99999]之间的整数。
                             "lastLogOffEndTime": None,  # 最后下线结束时间  数据类型：日期 约束条件：格式为“yyyy-MM-dd HH:mm:ss”。
                             "lastLogOffStartTime": None,
                             # 最后下线开始时间 数据类型：日期 约束条件：格式为“yyyy-MM-dd HH:mm:ss”，当最后下线开始时间和结束时间同时存在时，开始时间必须小于或等于结束时间。
                             "logonDomain": "",  # 登录域名称 数据类型：字符串 约束条件：最大长度为256个字符。
                             "maxConcurrentLimit": -9999,  # 在线数量限制 数据类型：整型 约束条件：[-9999 - 99999]之间的整数。
                             "maxIdleTime": -9999,  # 最大闲置时间 数据类型：整型 约束条件：[-9999 - 99999]之间的整数。
                             "outerVlanId": -9999,  # 外层VLAN ID 数据类型：长整型 约束条件：[-9999 - 99999]之间的整数。
                             "port": -9999,  # 设备端口 数据类型：整型 约束条件：[-9999 - 99999]之间的整数。
                             "resultCount": 10,  # 默认为200，表示最多返回的查询记录数
                             "resultIndex": 1000,  # 默认为1，表述从第一条查询结果开始返回客户端
                             "resultSort": 1,  # 数据类型：整型 1 表示按“帐号名”排序 2 表示按“用户姓名”排序 3 表示按“失效时间”排序其他值等同于按照“帐号名”排序
                             # "resultSortType ": 1,  # 数据类型：整型 0 表示升序排列 1 表示降序排列 其他值等同于升序排列。 约束条件：无 缺省值：默认为0，表示升序排列。
                             "serviceID": None,  # 服务ID 系统中唯一标识一个服务编号。 数据类型：长整型 约束条件：无
                             "state": 1,  # 帐号状态 1 正常 2 注销 3 未激活 4 暂停 数据类型：整型 约束条件：无。
                             "userEndIp": "",  # 用户IP地址结束值 数据类型：字符串 约束条件：IPv4。
                             "userGroupId": None,  # 用户分组ID 系统中唯一标识一个用户分组编号。 数据类型：长整型 约束条件：无
                             "userMac": "",  # 用户MAC地址 数据类型：字符串
                             # 约束条件：满足正则表达式"([a-fA-F0-9]{2})((-|:)[a-fA-F0-9]{2}){0,5}"或"[a-fA-F0-9]{4}(-[a-fA-F0-9]{4}){0,2}"的字符串。
                             "userSsid": "",  # 用户SSID 数据类型：字符串 约束条件：最大长度为120个字符。
                             "userStartIp": ""  # 用户IP地址起始值 数据类型：字符串 约束条件：IPv4。当用户IP地址起始值和结束值同时有值时，起始值必须小于或等于结束值。#
                             }
    # print json.dumps(AcmUserListQueryParam, indent=4) #格式化字符串后输出
    print client.service.queryAcmUserList(AcmUserListQueryParam)  # 调用方法queryAcmUserList，传入参数，输出接入用户列表。
    logout()


class User(object):
    pass


def plat_user_add():
    url = imcplatUserService
    client = Client(url)
    # print client # 打印方法名及参数类型
    client.set_options(port='imcplatUserServiceHttpSoap12Endpoint')
    client.set_options(headers=header)
    print client.set_options(headers=header)  # 设置header
    client.options.transport.cookiejar = login()  # 调用login()函数返回的Cookie JSESSIONID，保持会话
    # print client.service.queryAllUserGroup()# 查询所有的用户分组信息
    # print client.service.queryUserById(8824)# 查询用户ID为8824的用户信息
    # AddUserParam = client.factory.create('ns2:User')  # 创建参数工厂模式
    # print AddUserParam # 打印工厂模式参数



    # 平台用户增加参数构造
    AddUserParam = {"address": "11",
                    "certification": "222222222222222226",
                    "email": "",
                    "phone": "12345678901",
                    "id": None,
                    "status": 0,
                    "userAppend": {
                        "column_01": "imcws-test",
                        "id": None
                    },
                    "userCancelTime": None,
                    "userCreateTime": None,
                    "userGroup": {"desc": "毕业班学生组", "id": 4, "name": "毕业班学生组"},
                    "userName": "IMCWS-TEST"
                    }
    print client.service.addUser(AddUserParam)  # 调用addUser方法增加平台用户，并返回结果。


def add_acm_user():
    url = acmUserService
    client = Client(url)
    # print client
    client.set_options(port='acmUserServiceHttpSoap12Endpoint')  # soap报文端口设置
    client.set_options(headers=header)
    print client.set_options(headers=header)
    client.options.transport.cookiejar = login()  # 调用login()函数返回的Cookie JSESSIONID，保持会话
    AddAcmUserParam = client.factory.create('ns0:AddAcmUserParam')  # 创建参数工厂模式
    print AddAcmUserParam
    # AcmServiceTemplateQueryParam = client.factory.create('ns8:AcmServiceTemplateQueryParam')
    # print AcmServiceTemplateQueryParam
    AcmServiceTemplateQueryParam = {"resultSort": 0, "resultSortType": 1}  # 接入服务模板参数构造
    print client.service.queryServiceTemplateList(AcmServiceTemplateQueryParam)  # 查询服务模板列表
    AddUserParam = {"accountName": "",  # 帐号名 系统中唯一标识一个接入用户帐号。数据类型：字符串约束条件：最大长度为32个字符。
                    "boundDomain": "",  # 绑定域名称 数据类型：字符串 约束条件：最大长度为256个字符。
                    "computerName": "",  # 计算机名称 数据类型：字符串 约束条件：最大长度为256个字符。
                    "contactAddress": "",  # 通讯地址 数据类类型：字符串 约束条件：最大长度为39个字符
                    "creationEndDate": None,  # 开户结束日期 数据类型：日期 约束条件：格式为“yyyy-MM-dd””。
                    "creationStartDate": None,
                    # 开户起始日期 数据类型：日期  约束条件：格式为“yyyy-MM-dd”，日期和时间之间用字母“T”连接，当开户起始日期和结束日期同时存在时，起始日期必须小于或等于结束日期。
                    "deviceEndIp": "",  # 设备IP地址结束值 数据类型：字符串 约束条件
                    "deviceStartIp": "",  # 设备IP起始地址 数据类型：字符串 约束条件：IPv4。当设备IP地址起始值和结束值同时有值时，起始值必须小于或等于结束值。
                    "email": "",  # 电子邮件 数据类型：字符串 约束条件：最大长度为32个字符。
                    "feeType": None,  # 账号付费类型  0 免费 2 预付费 3 后付费 数据类型：整型 约束条件：无。
                    "fullName": "",  # 用户姓名 数据类型：字符串 约束条件：最大长度为32个字符。
                    "guest": None,  # 访问人 数据类型：字符串 约束条件：无。
                    "guestDepartment": "",  # 访问单位 数据类型：字符串 约束条件：无。
                    "guestManagerId": None,  # 可管理该访客的普通接入帐号ID 数据类型：字符串 约束条件：无。
                    "identityNumber": None,  # 证件号码 数据类型：字符串 约束条件：最大长度为32个字符。
                    "ifManageGuest": None,  # 可否管理访客 0 不可以 1 可以 数据类型：整型 约束条件：无。
                    "innerVlanId": -9999,  # VLAN ID/内层VLAN ID 数据类型：长整型 约束条件：[-9999 - 99999]之间的整数。
                    "lastLogOffEndTime": None,  # 最后下线结束时间  数据类型：日期 约束条件：格式为“yyyy-MM-dd HH:mm:ss”。
                    "lastLogOffStartTime": None,
                    # 最后下线开始时间 数据类型：日期 约束条件：格式为“yyyy-MM-dd HH:mm:ss”，当最后下线开始时间和结束时间同时存在时，开始时间必须小于或等于结束时间。
                    "logonDomain": "",  # 登录域名称 数据类型：字符串 约束条件：最大长度为256个字符。
                    "maxConcurrentLimit": -9999,  # 在线数量限制 数据类型：整型 约束条件：[-9999 - 99999]之间的整数。
                    "maxIdleTime": -9999,  # 最大闲置时间 数据类型：整型 约束条件：[-9999 - 99999]之间的整数。
                    "outerVlanId": -9999,  # 外层VLAN ID 数据类型：长整型 约束条件：[-9999 - 99999]之间的整数。
                    "port": -9999,  # 设备端口 数据类型：整型 约束条件：[-9999 - 99999]之间的整数。
                    "resultCount": 10,  # 默认为200，表示最多返回的查询记录数
                    "resultIndex": 1000,  # 默认为1，表述从第一条查询结果开始返回客户端
                    "resultSort": 1,  # 数据类型：整型 1 表示按“帐号名”排序 2 表示按“用户姓名”排序 3 表示按“失效时间”排序其他值等同于按照“帐号名”排序
                    # "resultSortType ": 1,  # 数据类型：整型 0 表示升序排列 1 表示降序排列 其他值等同于升序排列。 约束条件：无 缺省值：默认为0，表示升序排列。
                    "serviceID": None,  # 服务ID 系统中唯一标识一个服务编号。 数据类型：长整型 约束条件：无
                    "state": 1,  # 帐号状态 1 正常 2 注销 3 未激活 4 暂停 数据类型：整型 约束条件：无。
                    "userEndIp": "",  # 用户IP地址结束值 数据类型：字符串 约束条件：IPv4。
                    "userGroupId": None,  # 用户分组ID 系统中唯一标识一个用户分组编号。 数据类型：长整型 约束条件：无
                    "userMac": "",  # 用户MAC地址 数据类型：字符串
                    # 约束条件：满足正则表达式"([a-fA-F0-9]{2})((-|:)[a-fA-F0-9]{2}){0,5}"或"[a-fA-F0-9]{4}(-[a-fA-F0-9]{4}){0,2}"的字符串。
                    "userSsid": "",  # 用户SSID 数据类型：字符串 约束条件：最大长度为120个字符。
                    "userStartIp": "",  # 用户IP地址起始值 数据类型：字符串 约束条件：IPv4。当用户IP地址起始值和结束值同时有值时，起始值必须小于或等于结束值。#
                    }  # 增加接入用户参数构造
    # print json.dumps(AcmUserListQueryParam, indent=4)  # 格式化字符串后输出
    # print client.service.addUser(AddUserParam)


if __name__ == '__main__':
    # login()
    # query_wsdl_service(get_service_url())
    # acm_user_service_query()
    # get_service_url()
    #plat_user_add()
    add_acm_user()
