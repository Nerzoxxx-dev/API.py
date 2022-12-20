class APIException(Exception):
  def __init__(self, code):
    self.__code = code
    
  @property
  def code(self) -> int:
      return self.__code