import random

s=['如果你当前的房子数量最少，则房子最多的玩家给一半房子给你，否则政府没收你一个房子',
'如果你当前资产前三少，则资产最多的 玩家给一半资产给你，否则没收一半资产',
'其他玩家进行出资，出资最多的玩家出的钱被剩下的玩家平分，出资最少的玩家的资产的一半被剩下玩家平分指定一名玩家获得他的一套随机房产']

print(s[random.randint(0,3)])