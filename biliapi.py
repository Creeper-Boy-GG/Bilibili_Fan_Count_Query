import requests
import tkinter as tk

def update_text():
    global u
    u = entry.get()
    entry.delete(0, tk.END)  # 清空文本框
    root.destroy()
root = tk.Tk()

# 更改窗口名字
root.title("B站粉丝数查询器")

# 设置窗口大小
root.geometry("300x200")
label = tk.Label(root, text="请输入你的uid:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="确定", command=update_text)
button.pack()


root.mainloop()


h = {
    "authority": "api.bilibili.com",
    "method": "POST",
    "path": "/x/relation/stat?vmid="+u,
    "scheme": "https",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    'Accept-Encoding': 'gbk'
}


req = requests.get("https://api.bilibili.com/x/relation/stat?vmid="+u, headers= h).json()
if req != None:
    print("请求成功")
else:
    print("请求失败")
print(req["data"]["follower"])

# 创建主窗口
root = tk.Tk()

# 设置窗口大小
root.geometry("300x200")

# 更改窗口名字
root.title("B站粉丝数查询器")

# 创建一个Label widget
label = tk.Label(root, text="你的粉丝数是："+str(req["data"]["follower"]))

# 将Label widget添加到主窗口
label.pack()

# 运行Tkinter事件循环
root.mainloop()
