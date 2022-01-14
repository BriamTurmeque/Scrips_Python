def clasificacion_huevos(lisHuevos):
    
    huevosA={
        "tipo_huevo":"A",
        "numero_huevos":0,
        "numero_bandejas":0
    }
    huevosAA={
        "tipo_huevo":"AA",
        "numero_huevos":0,
        "numero_bandejas":0
    }
    huevosAAA={
        "tipo_huevo":"AAA",
        "numero_huevos":0,
        "numero_bandejas":0
    }
    huevosBC={
        "tipo_huevo":"BC",
        "numero_huevos":0,
        "numero_bandejas":0
    }
    for i in lisHuevos:
        if i<60 and i>=53:
            huevosA["numero_huevos"]+=1
        elif i>=60 and i<67:
            huevosAA["numero_huevos"]+=1
        elif i>67:
            huevosAAA["numero_huevos"]+=1
        else:
            huevosBC["numero_huevos"]+=1
    huevosA["numero_bandejas"]=huevosA["numero_huevos"]//30
    huevosAA["numero_bandejas"]=huevosAA["numero_huevos"]//24
    huevosAAA["numero_bandejas"]=huevosAAA["numero_huevos"]//12
    huevosBC["numero_bandejas"]=huevosBC["numero_huevos"]//30
    
    resultado=[huevosA,huevosAA,huevosAAA,huevosBC]
    return resultado


