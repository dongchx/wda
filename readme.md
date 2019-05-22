
#### 环境准备

+ xcode9.0 以上

+ homebrew (应该都有，没有的话如下安装)
  xcode-select --install
  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

+ brew install node -- 安装 node/npm

+ brew install Carthage -- 安装 Carthage

+ brew install libimobiledevice -- 真机端口转发所需依赖

+ brew install python3 -- 安装python3

+ pip3 install --pre facebook-wda -- 安装python依赖库

+ pip3 install pillow -- python图片处理库

#### 真机安装wda

+ git clone https://github.com/facebook/WebDriverAgent.git -- 克隆WDA工程到本地
	+ xcode 10.2 git clone git@github.com:appium/WebDriverAgent.git
	+ xcode 10.2 XCAXClient_iOS API有调整

+ cd WebDriverAgent - 切换到工程目录

+ ./Scripts/bootstrap.sh - 运行脚本，一定要在WebDriverAgent目录下运行

+ 用xcode打开WebDriverAgent.xcodeproj

+ Target 选择 WebDriverAgentRunner

+ 设置证书，用免费开发者证书即可

+ 如果用免费开发者证书，bundleId需要增加一个任意后缀，保证唯一即可

+ destination 选择真机

+ product -> test

+ xcode命令行能看到ip地址表示运行成功


#### 运行脚本

+ iproxy 8100 8100 [UDID] --> 端口转发- 运行成功命令行会提示waiting connection

+ 浏览器 打开 http://localhost:8100/inspector， 能看到终端界面的映射

+ git clone https://github.com/dongchx/wda.git -- 克隆本工程到本地

+ cd wda --  切换到工程目录

+ python3 autoscript.py -- 运行python脚本

#### 其他

+ 所有屏幕截图存放在wda/img目录下
+ 白屏屏幕截图会保存在wda/wimg目录下

#### 并行脚本

	iproxy的完整格式 iproxy LOCAL_TCP_PORT DEVICE_TCP_PORT [UDID]
    其中LOCAL_TCP_PORT是usb转发的端口号可以自定义；
    DEVICE_TCP_PORT 是移动设备上的wda端口号固定是8100；
    UDID是设备ID；

    我们可以为每台设备定义一个唯一usb转发端口号，例：
    iproxy 8101 8100 idevice_id_1
    iproxy 8102 8100 idevice_id_2
    设备id可以通过 idevice_id -l 查看

    在运行脚本时，将端口号作为参数传入，例：
    python3 autoscript.py 8101

    此外，还需要通过命令行来启动webDriverAgent
    切入WebDriverAgent目录，命令行输入
    xcodebuild -project WebDriverAgent.xcodeproj \-scheme WebDriverAgentRunner \-destination id=$(idevice_id) test
    $(idevice_id) 替换成设备id















