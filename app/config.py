class Config:
  '''
  General configuration parent class
  '''
  pass

class ProdConfig(Config):
  '''
  Production configuration child class
  
  args:
        Config: The parent configuration class with Gen config settings
  '''
  pass

class DevConfig(Config):
  '''
  Dev config child class
  '''
  
  DEBUG = True      