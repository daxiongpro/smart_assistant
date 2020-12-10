class Product(object):

    def __init__(self, id, name, total_steps):
        self.id = id
        self.name= name
        self.total_steps = total_steps
        self.step = ['', 0,1,0,1,0] #0代表提示拿零件，1代表播放视频教学。 0好位置空着


