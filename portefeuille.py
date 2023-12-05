class Portefeuille:
    
    import datetime

    def __init__(Bourse):

        #Historique des transactions en liquide
        Bourse.transaction = {}
        #historique des transaction de titre
        Bourse.titre = {}


    def déposer(Bourse, montant, date=datetime.date.today()):
        
        from exceptions import ErreurDate
        
        import datetime
        if date > datetime.date.today():
            raise ErreurDate
        
        date = str(date)
        Bourse.transaction[date] = montant


    def solde(Bourse, date=datetime.date.today()):
        
        from exceptions import ErreurDate

        import datetime
        if date > datetime.date.today():
            raise ErreurDate
        
        date = str(date)
        Bourse.transaction.sort()

        solde = 0
        for clé, valeur in Bourse.transaction.items():

            if clé > date:
                break

            solde += valeur

            if clé == date:
                break
        return solde


    def acheté(Bourse, symbole, quantité, date=datetime.date.today()):

        from exceptions import ErreurDate
        from exceptions import LiquiditéInsuffisante

        import datetime
        if date > datetime.date.today():
            raise ErreurDate
        
        v = (Bourse.prix(symbole, date)) * quantité
        if v > Portefeuille.solde(date):
            raise LiquiditéInsuffisante
        
        Portefeuille.déposer(-v, date)

        Bourse.titre[str(date)] = {}
        Bourse.titre[str(date)][symbole] = quantité


    def vendre(Bourse, symbole, quantité, date=datetime.date.today()):

        from exceptions import ErreurDate
        from exceptions import ErreurQuantité

        import datetime
        if date > datetime.date.today():
            raise ErreurDate

        Bourse.titre.sort()
            
        q = 0
        for clé, dic in Bourse.titre.items():

            if clé > str(date):
                break

            for s, v in dic.items():
                if s == symbole:
                    q += v

            if clé == str(date):
                break
        
        if q < quantité:
            raise ErreurQuantité

        v = (Bourse.prix(symbole, date)) * quantité
        Portefeuille.déposer(v, date)

        Bourse.titre[str(date)] = {}
        Bourse.titre[str(date)][symbole] = -quantité


    def valeur_total(Bourse, date=datetime.date.today()):

        from exceptions import ErreurDate

        import datetime
        if date > datetime.date.today():
            raise ErreurDate
        
        v = Portefeuille.solde(date)

        Bourse.titre.sort()
        for clé, dic in Bourse.titre.items():
            if clé > str(date):
                break

            for s, q in dic.items():
                v += q*Bourse.prix(s, date)
            
            if clé == str(date):
                break
        return v
    

    def valeur_des_titres(Bourse, symbole, date=datetime.date.today()):

        from exceptions import ErreurDate

        import datetime
        if date > datetime.date.today():
            raise ErreurDate
        
        v = 0
        Bourse.titre.sort()
        for clé, dic in Bourse.titre.items():
            
            if clé > str(date):
                break

            for s, q in dic.items():
                for i in symbole:
                    if i == s:
                        v += q*Bourse.prix(s, date)
            
            if clé == str(date):
                break
        return v
    

    def titres(Bourse, date=datetime.date.today()):

        from exceptions import ErreurDate

        import datetime
        if date > datetime.date.today():
            raise ErreurDate
        
        d = {}
        Bourse.titre.sort()
        for clé, dic in Bourse.titre.items():

            if clé > str(date):
                break

            for s in dic.keys():
                d[s] = 0

            if clé == str(date):
                break

        for clé, dic in Bourse.titre.items():

            if clé > str(date):
                break

            for s, q in dic.items():
                d[s] += q

            if clé == str(date):
                break
        return d
    

    def valeur_projetée(Bourse, date, rendement):
        
        import datetime

        n = date - datetime.date.today()
        n = n.days//365
        m = date - datetime.date.today()
        m = m.days%365

        if type(rendement) == type(float()):

            vtitre = Bourse.valeur_total() - Portefeuille.solde()
            vtitre = vtitre*(1+rendement/100)**n + (m/365)*vtitre*(rendement/100)
        
            return vtitre + Portefeuille.solde()
        

        if type(rendement) == type(dict()):

            d = Bourse.titres()
            vtitre = 0

            for s, t in rendement.items():
                for key, q in d.items():
                    if s == key:
                        v = q*Bourse.prix(key, datetime.date.today())
                        vtitre += v*(1+t/100)**n + (m/365)*v*(t/100)

            for s in rendement.keys():
                d.pop(s)

            for key, q in d.items():
                vtitre += q*Bourse.prix(key, datetime.date.today())

            return vtitre + Portefeuille.sold()