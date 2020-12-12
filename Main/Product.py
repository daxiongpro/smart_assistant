class Step(object):
    def __init__(self, number, step_type):
        self.number = number
        self.type = step_type
        if self.type == 'video':
            pass
        elif self.type == 'take':
            #拿零件
            pass

class Product(object):
    def __init__(self, product_id, product_name):
        self.product_id = product_id
        self.product_name= product_name
        self.steps = ['', 0,1,0,1,0] #0代表提示拿零件，1代表播放视频教学。 0好位置空着
        self.now_step = 0


