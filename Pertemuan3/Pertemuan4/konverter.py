from kurs import kurs

def konversi(dari, ke, nominal):
    if dari == "IDR":
        return nominal / kurs[ke]
    elif ke == "IDR":
        return nominal * kurs[dari]
    else:
        return nominal * kurs[dari] / kurs[ke]

