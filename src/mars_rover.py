class MarsRover:
    def execute(self, command: str) -> str:
        if command == 'M':
            return '0:1:N'
        
        return '0:0:N'