class TextEditor:
    def __init__(self):
            self.left = []
      
            self.right = []

    def addText(self, text: str) -> None:
      
        for char in text:
            self.left.append(char)

    def deleteText(self, k: int) -> int:
       
        count = 0
        while k > 0 and self.left:
            self.left.pop()
            k -= 1
            count += 1
        return count

    def cursorLeft(self, k: int) -> str:
       
        while k > 0 and self.left:
            self.right.append(self.left.pop())
            k -= 1
        return self._get_left_preview()

    def cursorRight(self, k: int) -> str:
       
        while k > 0 and self.right:
            self.left.append(self.right.pop())
            k -= 1
        return self._get_left_preview()

    def _get_left_preview(self) -> str:
        
        return "".join(self.left[-10:])
