import wda
import time

# default False
# Enable debug will see http Request and Response
# wda.DEBUG = True
wda.DEBUG = False 
# default 60.0 seconds
wda.HTTP_TIMEOUT = 60.0 

# build connection
c = wda.Client('http://localhost:8100')

# Show status
print (c.status())

# instance
s = c.session()
e = s(type='TextField')

# const
words = ["123\n", "新浪\n", "mip\n", "秋葵的做法大全\n", "海草舞\n", 
		 "曼联\n", "阿森纳\n", "切尔西\n", "热刺\n", "曼城\n", "利物浦\n", "波尔图\n", "大巴黎\n", "巴塞罗那\n", "皇马\n", "拜仁\n",
         "尤文图斯\n", "都灵\n", "AC米兰\n", "罗马\n", "威尼斯\n", "桑普多利亚\n", "乌迪内斯\n", "那不勒斯\n", "阿贾克斯\n", 
         "费耶诺德\n", "埃因霍温\n", "塞维利亚\n", "西班牙人\n", "拉齐奥\n", "法兰克福\n", "多特蒙德\n", "马德里竞技\n", "凯尔特人\n",
         "费内巴切\n", "狼堡\n", "霍芬海姆\n", "海牙\n", "里斯本竞技\n", "热那亚\n", "尼斯\n", "里昂\n", "南特\n", 
         "贝尔格莱德\n", "雷丁\n", "诺丁汉\n", "莫尔德\n", "苏黎世\n", "柏林赫塔\n", "博尔顿\n", "圣保罗\n", "科特布斯\n"]

sec = [0, 1, 2,  3, 4, 5, 6]


def waiting():
	time.sleep(1)


def inputKeywords(key):
	e.clear_text()

	for w in key:
		e.set_text(w)
		pass


def output(count):
	waiting()
	c.screenshot('img/'+str(count)+'.png')



def main():
	count  = 0

	while True:

		if count > 0 and count%3 == 0:
			e.click()
			if s(type='Cell').exists:
				s(type='Cell', index=0).tap()
				pass
			pass

		else:
			index = count % len(words)
			key = words[index]
			inputKeywords(key)
			print(str(count)+key)
			pass

		output(count)
		count += 1

		if count % 10 == 0:
			if s(name='回首页').exists:
				s(name='回首页').tap();
				pass
			pass

		pass

if __name__ == '__main__':
    main()

# s(type='TextField').set_text('曼联\n')
# time.sleep(3)
# s(type='TextField').clear_text()
# s(type='TextField').set_text('阿森纳\n')