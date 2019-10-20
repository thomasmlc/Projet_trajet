def HeureToDecimal(st):
    h, m = st.split('h')
    print( float(h) + float(m)/60 )

def DecimalToHeure(dec):
    dec = str(dec)
    h, m = dec.split('.')
    m = int(m)*60
    print ( str(h),'h', str(m)[0:2])
