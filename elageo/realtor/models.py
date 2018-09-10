from django.db import models

# Create your models here.

class Owner(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    address= models.CharField(max_length=50)


    def __str__(self):
        return 'id{} name: {} {}  number: {}'.format(self.id, self.firstname,self.lastname,self.phone)




class Property(models.Model):
    PROPERTY_CHOICES = (
        ('apartment','Apartment'),
        ('house','House'),
        ('office','Office'),
        ('townhouse','Townhouse'),
        ('warehouse','Warehouse'),
        ('shop','Shop'),
        ('land','Land')
    )
    SALE_OR_RENT = (
        ('sale','Sale'),
        ('rent','Rent')
    )

    owner = models.ForeignKey(Owner, related_name='properties', on_delete = models.CASCADE)
    property_type = models.CharField(max_length = 20,choices=PROPERTY_CHOICES )
    disposal_type = models.CharField(max_length = 4, choices = SALE_OR_RENT)
    bed = models.PositiveIntegerField(default = 0)
    bath = models.PositiveIntegerField(default = 0)
    garage = models.PositiveIntegerField(default = 0,  null=True,blank=True)
    size = models.DecimalField(null=True,blank=True,max_digits=10, decimal_places=2)
    description = models.TextField(null=True,blank=True)
    location = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)


    class Meta:
        ordering = ('-updated',)
        verbose_name = 'property'
        verbose_name_plural = 'properties'

    def __str__(self):
        return 'id: {} {} bedroom {} located at {} :{}' .format(self.id, self.bed,self.property_type,self.location,self.disposal_type)



class Picture(models.Model):
    img_desc = models.TextField()
    property = models.ForeignKey(Property,related_name='pictures', on_delete = models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d')

    def __str__(self):
        return 'id: {}'.format(self.id)
