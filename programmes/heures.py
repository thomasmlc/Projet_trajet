def HeureToDecimal(duration):
    h, m = duration.split('h')
    
    return float(h) + float(m)/60 

def DecimalToHeure(deci):
    deci = str(deci)
    h, m = deci.split('.')
    m = int(m)*60
    if m < 1000 :
        return str(h)+'h'+ '0'+str(m)[0:1]
    else:    
        return str(h)+'h'+ str(m)[0:2]
        
    
