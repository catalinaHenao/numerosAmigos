import pytest 
from numerosAmigos import numeros_amigos 
respuesta=" no son amigos"

def test_Amigos():
    assert numeros_amigos(7,6)=="7 y 6 no son amigos"

@pytest.mark.parametrize(
"número1,número2,respuesta",
 [
 (1184,1210,respuesta),
 (6232, 6368,respuesta),
 (2924,2620,respuesta),
 (12285, 14595,respuesta),
 (1184,1210,respuesta),
 (2,284,respuesta),
 (63,4,respuesta),
 (10744, 10856,respuesta),
 (63,140,respuesta),
 (26,224,respuesta)

 ]

)
def test_numeroAmigos_param(número1,número2,respuesta):
    assert numeros_amigos(número1,número2)==str(número1) +" y " +str(número2)+ respuesta

if __name__=="__numeroAmigos__":
  test_Amigos()