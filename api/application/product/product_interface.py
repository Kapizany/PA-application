from abc import ABC
import enum

class STATUS(enum.Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

class ProductInterface(ABC) {
    
    id:str
    name:str
    price: float
    status: STATUS
    
    @abstractmethod
	def IsValid(self)-> bool:
        pass
    @abstractmethod    
	def Enable(self) -> None:
        pass
    @abstractmethod    
	def Disable(self) -> None:
        pass
    @abstractmethod    
	def GetID(self) -> str:
        pass
    @abstractmethod    
	def GetName(self) -> str:
        pass
    @abstractmethod    
	def GetStatus(self) -> str:
        pass
    @abstractmethod    
	def GetPrice(self) -> float:
        pass
}
