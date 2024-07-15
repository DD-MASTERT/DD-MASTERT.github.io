from PIL import Image

# 打开一个图片文件
with Image.open('2.jpg') as img:
    # 使用transpose方法，参数Image.FLIP_LEFT_RIGHT实现左右翻转
    flipped_img = img.transpose(method=Image.FLIP_LEFT_RIGHT)
    
    # 保存翻转后的图片
    flipped_img.save('21.jpg')
