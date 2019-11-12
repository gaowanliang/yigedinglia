# yigedinglia —— 理财高手
基于Python的成语接龙程序，可以自动接到一个顶俩
![image.png](https://i.loli.net/2019/11/12/FVsR4bwW8reCZz5.png)
附加功能：自动接到可复读成语
![image.png](https://i.loli.net/2019/11/12/JLcdeqm4SPDso5N.png)

## 产生原因

2019年8月，qq上线了成语接龙红包。发红包者只要给出一个成语，抢红包者只要写出一个头文字和那个成语结尾拼音相同的成语即可领取红包，后继抢红包者继续重复这个步骤。这让很多群都从聊各种话题变成了聊成语，高玩梁的群也不例外。但是总有那么一群人在第一时间就发现新产品的漏洞，这个漏洞便是 **一个顶俩**,，因为这个成语无法继续接下去，因为没有以“lia”这个拼音开头的成语，这样红包就无法继续抢。所以我就想出了这个“理财工具”，可以借此来理财，让你看的见红包却不能领，或者发红包者及时止损。可谓是“理财高手”
![image.png](https://i0.hdslb.com/bfs/article/d4151d384e5d4a3b31c6d3d78bc3b39d33ccb66c.png)

## 使用方法
首先您需要安装requirements.txt中的库，使用`pip install -r requirements.txt`

然后打开`server.py`,运行，打开 http://127.0.0.1:8000/ygdl / http://127.0.0.1:8000/fudu 即可体验

*前端文件出现问题，有时间会修复，大家可以直接使用原函数,下面给出使用方法*

在此目录下新建一个.py文件，输入以下内容：
```python
from cyjl import yigedinglia, cyfd

print(yigedinglia("为所欲为")) #通过具体成语来接到一个顶俩
print(yigedinglia("wei")) #通过末尾拼音来接到一个顶俩

print(cyfd("惺惺相惜")) #通过具体成语来接到可复读成语
print(cyfd("xi")) #通过末尾拼音来接到可复读成语

```