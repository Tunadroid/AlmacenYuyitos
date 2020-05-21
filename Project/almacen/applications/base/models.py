from django.db import models

# Create your models here.


class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    enabled = models.BooleanField('Enabled', default=True)
    creation_date = models.DateField(
        'Creation date', auto_now=False, auto_now_add=True)
    modification_date = models.DateField(
        'Modification date', auto_now=True, auto_now_add=False)
    elimination_date = models.DateField(
        'Elimination date', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class User_account(ModelBase):
    username = models.CharField('User Name', max_length=70, unique=True)
    password = models.CharField('Password', max_length=50)

    class Meta:
        verbose_name = 'User Account'
        verbose_name_plural = 'User Accounts'

    def __str__(self):
        return self.username


class Administrator(ModelBase):
    rut = models.CharField('Rut', max_length=10)
    names = models.CharField('Names', max_length=40)
    firstsurname = models.CharField('First Surname', max_length=20)
    lastsurname = models.CharField('Last Surname', max_length=20)
    birthdate = models.CharField('Birthdate', max_length=50)
    address = models.CharField('Address', max_length=100)
    phone_number = models.CharField('Phone Number', max_length=12)
    email = models.CharField('Email', max_length=150)
    useraccount = models.ForeignKey(User_account, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrators'

    def __str__(self):
        return '{0} {1}'.format(self.firstsurname, self.lastsurname)


class Seller(ModelBase):
    rut = models.CharField('Rut', max_length=10)
    names = models.CharField('Names', max_length=40)
    firstsurname = models.CharField('First Surname', max_length=20)
    lastsurname = models.CharField('Last Surname', max_length=20)
    birthdate = models.CharField('Birthdate', max_length=50)
    address = models.CharField('Address', max_length=100)
    phone_number = models.CharField('Phone Number', max_length=12)
    email = models.CharField('Email', max_length=100)
    useraccount = models.ForeignKey(User_account, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'

    def __str__(self):
        return '{0}, {1} {2}'.format(self.names, self.firstsurname, self.lastsurname)


class Debt(ModelBase):
    amount = models.IntegerField('Amount', default=0)
    start_date = models.DateField(
        'Start date', auto_now=True, auto_now_add=False)
    final_date = models.DateField('Final date')

    class Meta:
        verbose_name = 'Debt'
        verbose_name_plural = 'Debts'

    def __str__(self):
        return 'Deuda ${0}'.format(self.amount)


class Client(ModelBase):
    names = models.CharField('Names', max_length=40)
    firstsurname = models.CharField('First Surname', max_length=20)
    lastsurname = models.CharField('Last Surname', max_length=20)
    address = models.CharField('Address', max_length=100)
    phone_number = models.CharField('Phone Number', max_length=12)
    email = models.CharField('Email', max_length=100)
    debt_quota = models.IntegerField('Debt quota', default=0)
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return '{0}, {1} {2}'.format(self.names, self.firstsurname, self.lastsurname)


class Debt_payment(ModelBase):
    amount = models.IntegerField('Amount', default=0)
    payment_date = models.DateField('Payment date', auto_now=True)
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Debt payment'
        verbose_name_plural = 'Debt payments'

    def __str__(self):
        return 'Monto abonado ${0}'.format(self.amount)

class Provider(ModelBase):
    provider_name = models.CharField('Name', max_length=150)
    email = models.CharField('Email', max_length=150)
    phone_number = models.CharField('Phone Number', max_length=12)
    address = models.CharField('Address', max_length=100)

    class Meta:
        verbose_name = 'Provider'
        verbose_name_plural = 'Providers'

    def __str__(self):
        return self.provider_name


class Order(ModelBase):
    order_date = models.DateField('Order creation date', auto_now=True)
    shipping_date = models.DateField('Shipping date')
    reception_date = models.DateField('Reception date')
    total_price = models.IntegerField('Total price', default=1)
    new_produtcs = models.CharField('New products', max_length=100)
    status = models.CharField('Status', max_length=80)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    admin = models.ForeignKey(Administrator, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return 'Date: {0} - Total: {1}'.format(self.order_date, self. total_price)

class Product_type(ModelBase):
    typeProduct = models.CharField('Type', max_length=150)
    family = models.CharField('Family', max_length=50)

    class Meta:
        verbose_name = 'Product type'
        verbose_name_plural = 'Product types'

    def __str__(self):
        return self.typeProduct
        

class Product(ModelBase):
    barcode = models.CharField('barcode', max_length=100)
    brand = models.CharField('Brand', max_length=150)
    description = models.TextField('Description', default='')
    purchase_price = models.IntegerField('Purchase price', default=1)
    sale_price = models.IntegerField('Sale price', default=1)
    expiry_date = models.DateField('Expiry date')
    stock = models.IntegerField('Stock', default=1)
    critical_stock = models.IntegerField('Critical stock', default=1)
    referencial_img = models.ImageField(
        'Referencial Image', upload_to='product/')
    product_type = models.ForeignKey(Product_type, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Produtcs'

    def __str__(self):
        return self.brand


class Sale(ModelBase):
    date = models.DateField('Sale date', auto_now=True)
    amount = models.IntegerField('Amount', default=0)
    debt = models.BooleanField('Debt', default=False)
    admin = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        return 'Date: {0}'.format(self.date)


class Product_On_Sale(ModelBase):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cant_product = models.IntegerField('Cant product', default=0)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    sale_price = models.IntegerField('Sale price', default=1)

    class Meta:
        verbose_name = 'Product on sale'
        verbose_name_plural = 'Products on sale'

    def __str__(self):
        return 'product: {0} - Cant: {1}'.format(self.product, self.cant_product)
