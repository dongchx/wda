import wda
import time
import math
import shutil
from PIL import Image, ImageDraw
import sys
import os

# default False
# Enable debug will see http Request and Response
# wda.DEBUG = True
wda.DEBUG = False 
# default 60.0 seconds
wda.HTTP_TIMEOUT = 60.0 

# port
port = sys.argv[1]

# build connection
c = wda.Client('http://localhost:'+str(port))

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

# sec = [0, 1, 2,  3, 4, 5, 6]


def waiting(t):
	time.sleep(t)


def inputKeywords(key):
	e.clear_text()

	for w in key:
		e.set_text(w)
		pass


def output_screenshot(path):
	c.screenshot(path)


def whiteScreen(im):
	w,h = im.size;
	im_pixel = im.load()

	# print("size: {}, {}".format(w, h))

	scan_x = int(w/5);
	scan_start_y = int(h/5)
	scan_end_y = int(h*4/5)

	first_pi = im_pixel[scan_x, scan_start_y]
	for y in range(scan_start_y,scan_end_y):
		pixel = im_pixel[scan_x, y]
		if pixel != first_pi:
			im.close()
			return False
			pass
		pass

	im.close()
	return True

#创建目录
def createPath(path):
	if not os.path.exists(path):
		os.mkdir(path)

def imagPath(count):
	path = 'img/'+str(port)+'/'+str(count)+'.png'
	return path


def wImagePath(count):
	path = 'wimg/'+str(port)+'/'+str(count)+'.png'
	return path

def shotAgain(count):
	waiting(7)
	imgPath = imagPath(count)
	output_screenshot(imgPath)
	im = Image.open(imgPath)

	if whiteScreen(im):
		nImagePath = wImagePath(count)
		shutil.copyfile(imgPath, nImagePath)
		pass


def main():
	count  = 0

	imgFold = 'img/'+str(port)
	wimgFold = 'wimg/'+str(port)

	createPath(imgFold)
	createPath(wimgFold)

	while True:
		# if count > 0 and count%3 == 0:
		# 	e.click()
		# 	if s(type='Cell').exists:
		# 		s(type='Cell', index=0).click()
		# 		pass
		# 	pass

		# else:
		# 	index = count % len(words)
		# 	key = words[index]
		# 	inputKeywords(key)
		# 	# print(str(count)+key)
		# 	pass

		index = count % len(words)
		key = words[index]
		inputKeywords(key)

		waiting(2)
		imgPath = imagPath(count)
		output_screenshot(imgPath)
		im = Image.open(imgPath)
		print(str(count)+key)

		if whiteScreen(im):
			print("whiteScreen")
			shotAgain(count)
			pass

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