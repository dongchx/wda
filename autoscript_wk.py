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
port = 8100
if len(sys.argv)>1:
	port = sys.argv[1]
	pass

# build connection
c = wda.Client('http://localhost:'+str(port))

# show status
print (c.status())

# instance
s = c.session()
e = s(type='TextField')

# const
words = []


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
	waiting(15)
	imgPath = imagPath(count)
	output_screenshot(imgPath)
	im = Image.open(imgPath)

	if whiteScreen(im):
		nImagePath = wImagePath(count)
		shutil.copyfile(imgPath, nImagePath)
		return True

	return False

def goBackToHomePage():
	if s(name='回首页').exists:
		s(name='回首页').tap();

def queryKeyWord(count):
	index = count % len(words)
	key = words[index]
	return key

def checkWhiteScreen(count):
	imgPath = imagPath(count)
	output_screenshot(imgPath)
	im = Image.open(imgPath)
	print(str(count)+queryKeyWord(count))

	if whiteScreen(im):
		if shotAgain(count):
			return True

	return False


def readKeyWords():
	# fh = open('keywordList.txt')
	# for line in fh.readlines()
	# 	words.append(line)

	with open('keywordList.txt') as file_object:
		for line in file_object:
			words.append(line)

#点击sug关键字
def tapSugCell(idx):
	if s(type='Cell').exists:
		s(type='Cell', index=idx).click()

####### case start

#首页 - 输入query发起搜索 - 结果页 - 回首页
def case_1(count, goHome=True):
	query = queryKeyWord(count)
	inputKeywords(query)
	waiting(2)
	checkWhiteScreen(count)

	if goHome:
		goBackToHomePage()

#首页 - 点击sug发起搜索 - 结果页 - 回首页
def case_2(count, index=0, goHome=True):
	e.tap()
	tapSugCell(index)
	waiting(2)
	checkWhiteScreen(count)

	if goHome:
		goBackToHomePage()

#首页 - 输入query发起搜索 - 结果页 - 输入query发起 - 结果页 - 回首页
def case_3(count):
	case_1(count, False)
	case_1(count+1, True)

#首页 - 点击sug发起搜索 - 结果页 - 点击sug发起搜索 - 结果页 - 回首页
def case_4(count):
	case_2(count, 0, False)
	case_2(count, 1, True)

#首页 - 
def case_5(count):
	idx = count
	query = queryKeyWord(idx)
	inputKeywords(query)
	waiting(2)

	if checkWhiteScreen(idx):
		return;

	s.click(200, 200)
	checkWhiteScreen(count)
	s.swipe(100, 300, 100, 400, 0.1)

	if e.exists:
		idx += 1
		query = queryKeyWord(idx)
		inputKeywords(query)
		waiting(2)
		checkWhiteScreen(idx)

	goBackToHomePage()





####### case end

def main():
	count  = 0

	if len(sys.argv)>2:
		count = int(sys.argv[2])
		pass

	#创建目录
	imgFold = 'img/'+str(port)
	wimgFold = 'wimg/'+str(port)

	createPath(imgFold)
	createPath(wimgFold)

	#
	readKeyWords();

	while True:

		# case_1(count, True)
		# case_2(count, 0, True)
		# case_3(count)
		# case_4(count)

		case_5(count)

		count += 2

if __name__ == '__main__':
    main()



