import requests
from .._constants import BASEURL, USERAGENT
from .._exceptions import *
from .._models import Product, IBilling
from typing import Literal

class Billing:
  def __init__(self, products:list[Product], returnURL:str, completionUrl:str, method:Literal['PIX']='pix')