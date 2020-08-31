


from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
zipcode1 = int(input("zipcode:"))
print("\nZipcode:",zipcode1)
location = geolocator.geocode(zipcode1)
print("Details of the said pincode:")
print(location.address)
