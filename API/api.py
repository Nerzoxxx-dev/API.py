import requests
from .Exceptions import APIException

class Api:
  "API est la classe qui nous permettra de récupérer des informations depuis une api souhaitée, avec le module requests"
  
  """FQDN (Fully Qualified Domain Name): le nom de domaine de l'api souhaitée.
  expectedOutputFormat: Le format de renvoie d'une réponse voulu, seuls JSON, content et text sont les choix possibles
  baseHeaders: Les headers à inclure dans toutes les requêtes envoyées à l'api.
  controllErrorCode: si une erreur doit être envoyée lorsque le code de status de la requête n'est pas celui attendu (200)
  debug: si les requêtes doivent être transmises sous la forme d'une classe, mais aussi si des logs doivent être envoyées pour chaque requête
  """
  def __init__(self, fqdn: str, expectedOutputFormat: str = "json", baseHeaders: object = {}, controllErrorCode: bool = False, debug: bool = False):
    if not fqdn.endswith('/'):
      fqdn = f"{fqdn}/"
    self.fqdn = fqdn
    self.expectedOutputFormat = expectedOutputFormat
    self.baseHeaders = baseHeaders
    self.controllErrorCode = controllErrorCode
    self.debug = debug
  
    """
    Renvoie la requête sous le format voulu
    r: Objet Response fourni lors de l'envoie de la requête
    """
  def resolveResponse(self, r: requests.Response) -> object or str:
    responseToReturn: object or str = None
    if self.expectedOutputFormat == "json":
      responseToReturn = r.json()
    elif self.expectedOutputFormat == "text":
      responseToReturn = r.text
    elif self.expectedOutputFormat == "content":
      responseToReturn = r.content
    else:
      responseToReturn = r.json()
    
    return responseToReturn
  
  def resolveCode(self, code: int):
    accepted_codes = [200, 201]
    if code in accepted_codes:
      return True, f"The code {code} is received, all is good !"
    else:
      return False, f"The code {code} is received, there is maybe an error in your request."   
    
  """
  Envoie une requête GET
  uri: L'uri sur laquelle le module doit envoyer une requête (e.g: /api/users)
  params: Les paramètres envoyés avec la requête
  additionnalHeaders: Les headers qui doivent être transmis aux headers de base (ceux qui ont été définis lors de la création d'une instance de la classe Api)
  """      
  def get(self, uri: str, params: object = {}, additionnalHeaders: object = {}):
    headersToSend: object = self.baseHeaders
    headersToSend.update(additionnalHeaders)
    r = requests.get(f"{self.fqdn}{uri}", params=params, headers=headersToSend)
    errorState, message = self.resolveCode(r.status_code)
    if self.controllErrorCode:
      if not errorState:
        raise APIException(r.status_code)
    if not self.debug:
      r = self.resolveResponse(r)
    else:
      print(message)
    return r
  
  """
  Envoie une requête POST
  uri: L'uri sur laquelle le module doit envoyer une requête (e.g: /api/users)
  params: Les paramètres envoyés avec la requête (équivalent aux -d avec curl)
  additionnalHeaders: Les headers qui doivent être transmis aux headers de base (ceux qui ont été définis lors de la création d'une instance de la classe Api)
  """  
  def post(self, uri: str, params: object = {}, additionnalHeaders:object = {}):
    headersToSend: object = self.baseHeaders
    headersToSend.update(additionnalHeaders)
    r = requests.post(f"{self.fqdn}{uri}", params=params, headers=headersToSend)
    print(params)
    errorState, message = self.resolveCode(r.status_code)
    if self.controllErrorCode:
      if not errorState:
        raise APIException(r.status_code)
    if not self.debug:
      r = self.resolveResponse(r)
    else:
      print(message)
    return r
  
  """
  Envoie une requête PUT
  uri: L'uri sur laquelle le module doit envoyer une requête (e.g: /api/users)
  params: Les paramètres envoyés avec la requête
  additionnalHeaders: Les headers qui doivent être transmis aux headers de base (ceux qui ont été définis lors de la création d'une instance de la classe Api)
  """      
  def put(self, uri: str, params: object = {}, additionnalHeaders:object = {}):
    headersToSend: object = self.baseHeaders
    headersToSend.update(additionnalHeaders)
    r = requests.put(f"{self.fqdn}{uri}", params=params, headers=headersToSend)
    errorState, message = self.resolveCode(r.status_code)
    if self.controllErrorCode:
      if not errorState:
        raise APIException(r.status_code)
    if not self.debug:
      r = self.resolveResponse(r)
    else:
      print(message)
    return r
  
  """
  Envoie une requête PATCH
  uri: L'uri sur laquelle le module doit envoyer une requête (e.g: /api/users)
  params: Les paramètres envoyés avec la requête
  additionnalHeaders: Les headers qui doivent être transmis aux headers de base (ceux qui ont été définis lors de la création d'une instance de la classe Api)
  """      
  def patch(self, uri: str, params: object = {}, additionnalHeaders:object = {}):
    headersToSend: object = self.baseHeaders
    headersToSend.update(additionnalHeaders)
    r = requests.patch(f"{self.fqdn}{uri}", params=params, headers=headersToSend)
    errorState, message = self.resolveCode(r.status_code)
    if self.controllErrorCode:
      if not errorState:
        raise APIException(r.status_code)
    if not self.debug:
      r = self.resolveResponse(r)
    else:
      print(message)
    return r
  
  """
  Envoie une requête DELETE
  uri: L'uri sur laquelle le module doit envoyer une requête (e.g: /api/users)
  params: Les paramètres envoyés avec la requête
  additionnalHeaders: Les headers qui doivent être transmis aux headers de base (ceux qui ont été définis lors de la création d'une instance de la classe Api)
  """      
  def delete(self, uri: str, params: object = {}, additionnalHeaders:object = {}):
    headersToSend: object = self.baseHeaders
    headersToSend.update(additionnalHeaders)
    r = requests.delete(f"{self.fqdn}{uri}", params=params, headers=headersToSend)
    errorState, message = self.resolveCode(r.status_code)
    if self.controllErrorCode:
      if not errorState:
        raise APIException(r.status_code)
    if not self.debug:
      r = self.resolveResponse(r)
    else:
      print(message)
    return r
  

  

  

