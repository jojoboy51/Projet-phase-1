class Bourse:
    
#cette méthode doit retourner le prix à la fermeture
    def prix(symbole, date):
        
        from exceptions import ErreurDate
        
        import datetime
        if date > datetime.date.today():
            raise ErreurDate
        if date == datetime.date.today():
            date = date - datetime.timedelta(days = 1)

        from phase1 import produire_historique
        
        x = produire_historique(symbole, 'fermeture', date, date)
        if x == []:
            while x == []:
                date = date - datetime.timedelta(days = 1)
                x = produire_historique(symbole, 'fermeture', date, date)
        return float(x[0][1])