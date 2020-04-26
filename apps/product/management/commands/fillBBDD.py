from apps.product.models import Tag, Product
from apps.users.models import CustomUser
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="Creates tags"

    def handle(self, *args, **kwargs):
        farmer = CustomUser.objects.create(username="EcoEgg", first_name="Ecoegg",last_name="S.L",email="info@ecoegg.com" ,description="Lorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat.", tin="47218389D", country="ES", fiscal_address="C/ Major n 32", phone="000000000", lat=41.6180137, lon=0.6575223)
        ironman = CustomUser.objects.create(username="ScrewMan", first_name="ScrewMan",last_name="S.L",email="info@screwman.com" ,description="Lorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat.", tin="47648289D", country="ES", fiscal_address="Av Princep de Viana n 24", phone="000000000", lat=41.6180137, lon=0.6575223)
        tag_all = Tag.objects.create(name='all')
        tag_farming = Tag.objects.create(name='farming')
        tag_metallurgy = Tag.objects.create(name='metallurgy')
        ous = Product.objects.create(photo="ecoeggs.jpg", creator=farmer, tag=tag_farming, name="Ecologic Eggs", description="Lorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat.")
        tornillos = Product.objects.create(photo= "screw.jpg", creator=ironman, tag=tag_metallurgy, name="Screw", description="Lorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat.")
        farmer.save()
        ironman.save()
        tag_all.save()
        tag_metallurgy.save()
        tag_farming.save()
        ous.save()
        tornillos.save()
