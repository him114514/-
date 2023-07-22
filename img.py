from PIL import Image 
import numpy as np
while True:
    try:
        file=input('请输入图片路径:\n或将图片拖拽此处:\n')

        orgimg = file

        outimg = file+'处理结果.jpg'
        a = np.asarray(Image.open(orgimg).convert('L')).astype('float')

        depth = 10.             
        grad = np.gradient(a)   
        gradx, grady = grad   


        gradx = gradx * depth / 100.
        grady = grady * depth / 100. 
    
        A = np.sqrt(gradx ** 2 + grady ** 2 + 1.)
        unix = gradx / A 
        uniy = grady / A 
        uniz = 1./ A


        a = np.pi / 2.1                    
        c = np.pi / 4.                     
        dx = np.cos(a) * np.cos(c)    
        dy = np.cos(a) * np.sin(c)    
        dz = np.sin(a)                     

        b = 255 * (dx * unix + dy * uniy + dz * uniz) 
        b = b.clip(0, 255)                              
        im = Image.fromarray(b.astype( 'uint8'))         
        im.save(outimg)
        print('完成\n')
    except FileNotFoundError as e:
        print('错误:{0} \n找不到文件{1} '.format(e,file))
    except AttributeError as e1:
        print('错误:{0} \n属性错误 '.format(e1))    
    except OSError as e2:
        print('错误:{0} \n系统错误\n请去掉""或者\n有可能是不支持的图片格式 '.format(e2))    
