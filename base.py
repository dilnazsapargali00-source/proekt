from abc import ABC, abstractmethod

class MovieAnalyzer(ABC):
    """Фильм статистикасының негізгі абстрактілі класы"""
    
    @abstractmethod
    def analyze(self):
        pass
    
    @abstractmethod
    def show_report(self):
        pass
