class Car():
    
    def __init__(self,type,model,color,castName) -> None:
        self.type=type
        self.color = color
        self.model = model
        self.castName = castName
        
    def __str__(self) -> str:
        return f"type:{self.type}, model:{self.model}, color:{self.color}, castName:{self.castName}"    
    
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Car(**data)