import wda
import time

wda.DEBUG = False # default False
wda.HTTP_TIMEOUT = 60.0 # default 60.0 seconds

# Enable debug will see http Request and Response
# wda.DEBUG = True
c = wda.Client('http://localhost:8100')
# Show status
print (c.status())

s = c.session()
e = s(type='TextField')

words = ["曼联\n", "阿森纳\n", "切尔西\n", "热刺\n", "曼城\n", "利物浦\n", "波尔图\n", "大巴黎\n", "巴萨\n", "皇马\n", "拜仁\n"]
sec = [0, 1, 2,  3, 4, 5, 6]

count  = 0
while 1:
	index = count % len(words)
	key = words[index]
	e.clear_text()
	e.set_text(key)
	print(str(count)+key)
	time.sleep(3)
	c.screenshot('img/'+str(count)+'.png')
	count += 1


# s(type='TextField').set_text('曼联\n')
# time.sleep(3)
# s(type='TextField').clear_text()
# s(type='TextField').set_text('阿森纳\n')