class Car(object):
    def __init__(self,model,color,company):
        self.model=model
        self.color=color
        self.company=company
    
    def start(self):
        print('started')

    def stop(self):
        print('stopped')

AUDI=Car('a6','black','audi')
print(AUDI.start())
print(AUDI.stop())

        