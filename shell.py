from shop.models import Item, Purchase

product1 = Item.objects.create(name='Mac', price=6452)
product1.purchases.create(name='Olya',age=27)
product1.purchases.create(name='Dima',age=30)
product1.purchases.all()

product2 = Item.objects.create(name='Linux', price=1234)
product2.purchases.create(name='Polina',age=27)
product2.purchases.create(name='Kon',age=30)
product2.purchases.all()

product3 = Item.objects.create(name='iPad', price=1503)
product3.purchases.create(name='Olya',age=27)
product3.purchases.create(name='Dima',age=30)
product3.purchases.all()

product4 = Item.objects.create(name='MP3', price=400)
product4.purchases.create(name='Nina',age=40)
product4.purchases.create(name='Failya',age=15)
product4.purchases.all()

product5 = Item.objects.create(name='Mac', price=543)
product5.purchases.create(name='Mila',age=23)
product5.purchases.create(name='Hadicha',age=45)
product5.purchases.all()

product6 = Item.objects.create(name='Mac', price=2000)
product6.purchases.create(name='Olya',age=27)
product6.purchases.create(name='Dima',age=30)
product6.purchases.all()

product7 = Item.objects.create(name='Linux 2015', price=2054300)
product7.purchases.create(name='Olya',age=27)
product7.purchases.create(name='Dima',age=30)
product7.purchases.all()

product8 = Item.objects.create(name='Mac', price=2000)
product8.purchases.create(name='Olya',age=27)
product8.purchases.create(name='Dima',age=30)
product8.purchases.all()

product9 = Item.objects.create(name='Linux 2020', price=20765400)
product9.purchases.create(name='Ogongolya',age=98)
product9.purchases.create(name='Dima',age=30)
product9.purchases.all()

product10 = Item.objects.create(name='Mac', price=430)
product10.purchases.create(name='Dion',age=23)
product10.purchases.create(name='DJoniima',age=45)
product10.purchases.all()
