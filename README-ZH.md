# SuperSimpleConfig

https://github.com/shengj1ang/SuperSimpleConfig

`SuperSimpleConfig` 是一个轻量级的 Python 库，用于读取以极其简单方式编写的用户配置文件。它旨在提供一种简单直观的方法来处理配置文件，使得读取和应用配置变得轻而易举。


[English](https://github.com/shengj1ang/SuperSimpleConfig/blob/main/README.md)

## 特性

- 无块结构，一行一个配置项。
- 忽略所有空格。
- 自动检测数据类型（整数、浮点数、字符串、bool型）。
- 默认字符串不需要打"引号"，如果是数字内容想用字符串形式可以手动加上"123456"
- 超级简单的语法。
- 只支持读取，没有写入功能

## 安装

您可以通过 `pip` 来安装 `SuperSimpleConfig`：

```bash
pip install SuperSimpleConfig
```

## 快速开始
以下是如何使用 SuperSimpleConfig 的一个简单示例：

首先，创建一个配置文件，对于文件名称和后缀名无任何要求，这里以 `config.txt` 为例，内容如下：
```makefile
//开头可以写注释
domain=example.com //这里可以写注释
//这里也可以写
max_requests=5 //自动识别int
pi=3.1415 //自动识别 float

//空行也可以

```
以下是另一份配置文件:
```makefile
// 配置文件
// pip install pyserial
// pip install telepot
 //配置文件
 //https://api.telegram.org/botxxxx

phonenum="008613588888888" //手机号，不填不影响，在多开的情况下，填了方便区分。
max_error_count=10 //错误次数上限
timezone=0 //时区, 整数型
serialPort=COM3 //串口Windows可用../test/serial_init.cmd获取
baudRate=115200 //波特率
schedule_reconnect_max=20.0 //X秒未刷新，强制重新连接串口


db_path=database/example.db //数据库路径
sms_send_allow=True //允许发送短信吗
sms_auto_send=False //开启11位来电自动回复

sms_limit=1 //自动回复短信的数量上限
sms_auto_send_content=你好，你刚拨打的电话已经改为xxxxx,有事情请联系。//自动回复的内容
current_phonenum_log=True //是否在本地消息中显示本机号码

enable_telegram=True //启用Telegram
bot=1234567890:AAAA00xxxxxxxxxx //bot参数
tg_api_base_link=https:\/\/api.telegram.org
tg_chat_id="-00000000" //TG的群组
current_phonenum_tg=True //是否在Telegram消息中显示本机号码

flask_host=0.0.0.0
flask_port=8908
flask_production_mode=False

```
然后，您可以使用以下代码来读取和使用这些配置：

```python

from SuperSimpleConfig import UserConfig

configs = UserConfig().read("config.txt")

#UserConfig().read("FilePath")  #return a dictionary
#UserConfig().show("FilePath") #print the config

print(configs)
Value1=configs['flask_host']
Value2=congis["flask_port"]

```

## 配置文件格式
您的配置文件应该遵循以下简单规则：

- 每行定义一个配置项，格式为 key=value。可以有空行。
- 可以在行尾添加注释，以 // 开始。
字符串无需引号包围，除非您想强制将整数或浮点数值视为字符串。
转义字符：使用 \/\/ 来在文本中包含 //。 e.g. https:\/\/www.python.org


## 许可
SuperSimpleConfig 在 MIT 许可下发布。有关详细信息，请参阅 LICENSE 文件。

