def HeureToDecimal(duration):
    h, m = duration.split('h')
    
    return float(h) + float(m)/60 

def DecimalToHeure(deci):
    deci = str(deci)
    h, m = deci.split('.')
    m = int(m)*60
    return str(h)+'h'+ str(m)[0:2]
