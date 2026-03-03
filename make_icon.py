from PIL import Image, ImageDraw

def make_icon():
    # 创建基于红尾水鸲（Plumbeous Water-redstart）的形象
    img = Image.new('RGBA', (256, 256), color=(0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    
    # 橙色尾巴（在身体左侧）
    d.polygon([(20, 80), (80, 150), (20, 200)], fill="#FF7F50", outline="#FF4500", width=4)
    # 修正一下尾巴形状，让它像两撮羽毛
    d.pieslice((10, 100, 90, 220), 120, 240, fill="#FF7F50")

    # 绘制可爱的蓝色身子 (水鸲那种暗蓝色，这里用稍亮一点的藏青蓝以便看得清)
    d.ellipse((60, 40, 210, 210), fill="#4682B4", outline="#2F4F4F", width=10)
    
    # 嘴巴（黑嘴巴）
    d.polygon([(190, 110), (250, 128), (190, 146)], fill="#000000") 
    
    # 眼睛
    d.ellipse((140, 70, 180, 110), fill="white") 
    d.ellipse((150, 80, 170, 100), fill="black")
    
    # 翅膀（更深的蓝色）
    d.pieslice((80, 90, 160, 190), 0, 180, fill="#2F4F4F")

    img.save("bird.ico", format="ICO", sizes=[(256, 256)])
    img.save("bird.icns", format="ICNS")

if __name__ == "__main__":
    make_icon()
