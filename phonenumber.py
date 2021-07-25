import phonenumbers as phone

user = int(input("ใส่เบอร์ดทณไม่ต้องมี0 : "))
number = str(user)

x = phone.parse("+66"+number, None)

from phonenumbers import geocoder

print(geocoder.description_for_number(x, "th"));

from phonenumbers import carrier
print(carrier.name_for_number(x, "th"))

from phonenumbers import timezone
print(timezone.time_zones_for_number(x))
