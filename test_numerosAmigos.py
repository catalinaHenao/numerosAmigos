import pytest 
from numerosAmigos import numeros_amigos 
respuesta=" no son amigos"

@pytest.mark.parametrize(
        "número1,número2,repuesta",
[(220,284,respuesta),
 (1184,1210,respuesta),
 (6,6,respuesta),
 (120,284,respuesta),
 (1184,1210,respuesta),
 (630,54,respuesta),
 (90,56,respuesta),
 (63,14,respuesta),
 (262,2924,respuesta),
 (2924,2620,respuesta)
 ]

)
def test_numeroAmigos_param(número1,número2,respuesta):
    assert numeros_amigos(número1,número2)==str(número1) +" y " +str(número2)+ respuesta