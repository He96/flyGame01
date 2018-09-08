import base64


def pic2py(picture_name):
    """
    将图像文件转换为py文件
    :param picture_name:
    :return:
    """
    open_pic = open("%s" % picture_name, 'rb')
    b64str = base64.b64encode(open_pic.read())
    open_pic.close()
    # 注意这边b64str一定要加上.decode()
    write_data = 'img = "%s"' % b64str.decode()
    f = open('%s.py' % picture_name.replace('.', '_'), 'w+')
    f.write(write_data)
    f.close()


if __name__ == '__main__':
    # pics = ["img/gou.jpg", "img/bang1.png", "img/bang2.png", "img/bang3.png","img/bg1.jpg",
    #         "img/bg2.jpg","img/dan.png","img/dan1.png","img/dan3.png","img/dan4.png","img/GG1.jpg",
    #         "img/me.png","img/other.png"
     #       ]
    #pics = ['img/gou.png']
    #for i in pics:
    pic2py('gou3.png')
    print("ok")