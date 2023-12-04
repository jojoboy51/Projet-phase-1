class Portefeuille:
    
    import datetime

    def __init__(Bourse):

        #Historique des transactions en liqudie
        Bourse.transaction = {}
        #historique des transaction de titre
        Bourse.titre = {}


    def déposer(Bourse, montant, date=datetime.date.today()):
        
        import datetime
        if date > datetime.date.today():
            raise ErreurDate
        
        date = str(date)
        Bourse.transaction[date] = montant


    def solde(Bourse, date=datetime.date.today()):

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

        import datetime
        if date > datetime.date.today():
            raise ErreurDate

        Bourse.titre.sort()

        for clé in Bourse.titre.Keys():
            
            date = str(date)
            if clé > date:
                break
            
            q = 0
            for d, dic in Bourse.titre.items():
                for s, v in dic.items():
                    if s == symbole:
                       q += v
            if q < quantité:
                raise ErreurQuantité
            
            if clé == date:
                break

        v = (Bourse.prix(symbole, date)) * quantité
        Portefeuille.déposer(v, date)

        Bourse.titre[str(date)] = {}
        Bourse.titre[str(date)][symbole] = -quantité


    def valeur_total(Bourse, date=datetime.date.today()):

        import datetime
        if date > datetime.date.today():
            raise ErreurDate
        
        pass