from PIL import Image,ImageDraw,ImageFont
img=Image.open("D:\我的重要文件\计算机科学\python\代码练习\图像处理模块\86.png")
font=ImageFont.truetype("D:\我的重要文件\计算机科学\python\代码练习\图像处理模块\QingNiaoHuaGuangJianMeiHei\QingNiaoHuaGuangJianMeiHei-2.ttf",size=56)
draw=ImageDraw.Draw(img)
draw.text(xy=(1500,800),text="用python添加水印",fill="white",font=font)
img.show()
img.save("D:\我的重要文件\计算机科学\python\代码练习\图像处理模块\86(水印).png")
