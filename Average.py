class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self, name, fmt=':f'):
        self.name = name
        self.fmt = fmt
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

    def __str__(self):
        fmtstr = '{name} {val' + self.fmt + '} ({avg' + self.fmt + '})'
        return fmtstr.format(**self.__dict__)

def demo():
    ## 初始化对象
    loss = AverageMeter('Loss', ':.4e')
    print("initial:\t",loss)
    avg1 = 2
    num1 = 4
    loss.update(avg1,num1)
    print("add 4*2:\t",loss)
    avg2 = 3
    num2 = 2
    loss.update(avg2,num2)
    print("add 2*3:\t",loss)
    loss.reset()
    print("Reset:  \t",loss)

if __name__ == "__main__":
    demo()