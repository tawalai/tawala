import logging

class TawalaLogger:
    def __init__(self, name: str):
        self.name = name
        
        self.logger = logging.getLogger(self.name)
        
        standard_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(standard_formatter)
        
        file_handler = logging.FileHandler(f"{self.name}.log")
        file_handler.setFormatter(standard_formatter)
        
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)
        
        
    def get_logger(self) -> logging.Logger:
        return self.logger