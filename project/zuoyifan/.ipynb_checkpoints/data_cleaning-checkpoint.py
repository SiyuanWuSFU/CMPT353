import numpy as np
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor


# drop useless amenities
def drop_useless_amenities(data):
	data.drop(data.index[data['amenity'] == 'place_of_worship'], inplace = True)
	data.drop(data.index[data['amenity'] == 'school'], inplace = True)
	data.drop(data.index[data['amenity'] == 'community_centre'], inplace = True)
	data.drop(data.index[data['amenity'] == 'pharmacy'], inplace = True)
	data.drop(data.index[data['amenity'] == 'dentist'], inplace = True)
	data.drop(data.index[data['amenity'] == 'doctors'], inplace = True)
	data.drop(data.index[data['amenity'] == 'post_office'], inplace = True)
	data.drop(data.index[data['amenity'] == 'childcare'], inplace = True)
	data.drop(data.index[data['amenity'] == 'library'], inplace = True)
	data.drop(data.index[data['amenity'] == 'clinic'], inplace = True)
	data.drop(data.index[data['amenity'] == 'public_bookcase'], inplace = True)
	data.drop(data.index[data['amenity'] == 'university'], inplace = True)
	data.drop(data.index[data['amenity'] == 'dojo'], inplace = True)
	data.drop(data.index[data['amenity'] == 'toilets'], inplace = True)
	data.drop(data.index[data['amenity'] == 'recycling'], inplace = True)
	data.drop(data.index[data['amenity'] == 'veterinary'], inplace = True)
	data.drop(data.index[data['amenity'] == 'social_facility'], inplace = True)
	data.drop(data.index[data['amenity'] == 'post_box'], inplace = True)
	data.drop(data.index[data['amenity'] == 'college'], inplace = True)
	data.drop(data.index[data['amenity'] == 'construction'], inplace = True)
	data.drop(data.index[data['amenity'] == 'post_depot'], inplace = True)
	data.drop(data.index[data['amenity'] == 'nursery'], inplace = True)
	data.drop(data.index[data['amenity'] == 'clock'], inplace = True)
	data.drop(data.index[data['amenity'] == 'kindergarten'], inplace = True)
	data.drop(data.index[data['amenity'] == 'conference_centre'], inplace = True)
	data.drop(data.index[data['amenity'] == 'hospital'], inplace = True)
	data.drop(data.index[data['amenity'] == 'police'], inplace = True)
	data.drop(data.index[data['amenity'] == 'fire_station'], inplace = True)
	data.drop(data.index[data['amenity'] == 'charging_station'], inplace = True)
	data.drop(data.index[data['amenity'] == 'family_centre'], inplace = True)
	data.drop(data.index[data['amenity'] == 'townhall'], inplace = True)
	data.drop(data.index[data['amenity'] == 'waste_basket'], inplace = True)
	data.drop(data.index[data['amenity'] == 'music_school'], inplace = True)
	data.drop(data.index[data['amenity'] == 'meditation_centre'], inplace = True)
	data.drop(data.index[data['amenity'] == 'scrapyard'], inplace = True)
	data.drop(data.index[data['amenity'] == 'language_school'], inplace = True)
	data.drop(data.index[data['amenity'] == 'courthouse'], inplace = True)
	data.drop(data.index[data['amenity'] == 'prep_school'], inplace = True)
	data.drop(data.index[data['amenity'] == 'healthcare'], inplace = True)
	data.drop(data.index[data['amenity'] == 'cram_school'], inplace = True)
	data.drop(data.index[data['amenity'] == 'science'], inplace = True)
	data.drop(data.index[data['amenity'] == 'workshop'], inplace = True)
	data.drop(data.index[data['amenity'] == 'safety'], inplace = True)
	data.drop(data.index[data['amenity'] == 'lobby'], inplace = True)
	data.drop(data.index[data['amenity'] == 'animal_shelter'], inplace = True)
	data.drop(data.index[data['amenity'] == 'studio'], inplace = True)
	data.drop(data.index[data['amenity'] == 'storage_rental'], inplace = True)
	data.drop(data.index[data['amenity'] == 'waste_disposal'], inplace = True)
	data.drop(data.index[data['amenity'] == 'disused:restaurant'], inplace = True)
	data.drop(data.index[data['amenity'] == 'driving_school'], inplace = True)
	data.drop(data.index[data['amenity'] == 'chiropractor'], inplace = True)
	data.drop(data.index[data['amenity'] == 'monastery'], inplace = True)
	data.drop(data.index[data['amenity'] == 'telephone'], inplace = True)
	data.drop(data.index[data['amenity'] == 'casino'], inplace = True)
	data.drop(data.index[data['amenity'] == 'Pharmacy'], inplace = True)
	data.drop(data.index[data['amenity'] == 'waste_transfer_station'], inplace = True)
	data.drop(data.index[data['amenity'] == 'office|financial'], inplace = True)
	data.drop(data.index[data['amenity'] == 'research_institute'], inplace = True)
	data.drop(data.index[data['amenity'] == 'photo_booth'], inplace = True)
	data.drop(data.index[data['amenity'] == 'shower'], inplace = True)
	data.drop(data.index[data['amenity'] == 'trolley_bay'], inplace = True)
	data.drop(data.index[data['amenity'] == 'compressed_air'], inplace = True)
	data.drop(data.index[data['amenity'] == 'ATLAS_clean_room'], inplace = True)
	data.drop(data.index[data['amenity'] == 'vacuum_cleaner'], inplace = True)
	data.drop(data.index[data['amenity'] == 'smoking_area'], inplace = True)
	data.drop(data.index[data['amenity'] == 'EVSE'], inplace = True)
	data.drop(data.index[data['amenity'] == 'first_aid'], inplace = True)
	data.drop(data.index[data['amenity'] == 'ranger_station'], inplace = True)
	data.drop(data.index[data['amenity'] == 'trash'], inplace = True)
	data.drop(data.index[data['amenity'] == 'sanitary_dump_station'], inplace = True)
	data.drop(data.index[data['amenity'] == 'Observation Platform'], inplace = True)
	data.drop(data.index[data['amenity'] == 'payment_terminal'], inplace = True)
	data.drop(data.index[data['amenity'] == 'hunting_stand'], inplace = True)
	data.drop(data.index[data['amenity'] == 'letter_box'], inplace = True)
	data.drop(data.index[data['amenity'] == 'training'], inplace = True)
	data = data.reset_index(drop=True)	

	return data


# combine similar amenities: 'food' 'transportation' 'entertainment' 'living_stroage' 'shopping_banking'
def combine_samilar_amenities(data):
	# food
	data.loc[data.index[data['amenity'] == 'cafe'], ['amenity']] = ['food']
	data.loc[data.index[data['amenity'] == 'fast_food'], ['amenity']] = ['food']
	data.loc[data.index[data['amenity'] == 'bbq'], ['amenity']] = ['food']
	data.loc[data.index[data['amenity'] == 'vending_machine'], ['amenity']] = ['food']
	data.loc[data.index[data['amenity'] == 'restaurant'], ['amenity']] = ['food']
	data.loc[data.index[data['amenity'] == 'drinking_water'], ['amenity']] = ['food']
	data.loc[data.index[data['amenity'] == 'juice_bar'], ['amenity']] = ['food']
	data.loc[data.index[data['amenity'] == 'watering_place'], ['amenity']] = ['food']
	data.loc[data.index[data['amenity'] == 'water_point'], ['amenity']] = ['food']
	data.loc[data.index[data['amenity'] == 'food_court'], ['amenity']] = ['food']
	data.loc[data.index[data['amenity'] == 'ice_cream'], ['amenity']] = ['food']

	# transportation
	data.loc[data.index[data['amenity'] == 'fuel'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'parking_entrance'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'bicycle_parking'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'parking'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'ferry_terminal'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'car_rental'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'car_sharing'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'bicycle_rental'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'seaplane terminal'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'car_wash'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'bicycle_repair_station'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'parking_space'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'taxi'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'bus_station'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'motorcycle_parking'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'boat_rental'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'loading_dock'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'car_rep'], ['amenity']] = ['transportation']
	data.loc[data.index[data['amenity'] == 'motorcycle_rental'], ['amenity']] = ['transportation']

	# entertainment
	data.loc[data.index[data['amenity'] == 'pub'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'public_building'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'cinema'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'theatre'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'bar'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'arts_centre'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'fountain'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'nightclub'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'stripclub'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'gambling'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'bistro'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'playground'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'spa'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'events_venue'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'internet_cafe'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'social_centre'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'gym'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'park'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'biergarten'], ['amenity']] = ['entertainment']
	data.loc[data.index[data['amenity'] == 'leisure'], ['amenity']] = ['entertainment']

	# living_storage
	data.loc[data.index[data['amenity'] == 'bench'], ['amenity']] = ['living_stroage']
	data.loc[data.index[data['amenity'] == 'shelter'], ['amenity']] = ['living_stroage']
	data.loc[data.index[data['amenity'] == 'luggage_locker'], ['amenity']] = ['living_stroage']
	data.loc[data.index[data['amenity'] == 'lounge'], ['amenity']] = ['living_stroage']
	data.loc[data.index[data['amenity'] == 'housing co-op'], ['amenity']] = ['living_stroage']
	data.loc[data.index[data['amenity'] == 'storage'], ['amenity']] = ['living_stroage']

	# shopping_banking
	data.loc[data.index[data['amenity'] == 'atm'], ['amenity']] = ['shopping_banking']
	data.loc[data.index[data['amenity'] == 'bank'], ['amenity']] = ['shopping_banking']
	data.loc[data.index[data['amenity'] == 'bureau_de_change'], ['amenity']] = ['shopping_banking']
	data.loc[data.index[data['amenity'] == 'marketplace'], ['amenity']] = ['shopping_banking']
	data.loc[data.index[data['amenity'] == 'atm;bank'], ['amenity']] = ['shopping_banking']
	data.loc[data.index[data['amenity'] == 'money_transfer'], ['amenity']] = ['shopping_banking']
	data.loc[data.index[data['amenity'] == 'shop|clothes'], ['amenity']] = ['shopping_banking']

	return data


# remove null name rows
def remove_null_name(data):
	return data[data['name'].notna()].reset_index(drop=True)


# remove outlier
def remove_outlier(data):
	X = np.stack([data['lat'], data['lon']], axis=1)
	model = LocalOutlierFactor()
	y = model.fit_predict(X)

	for index, row in data.iterrows():
		if y[index] == -1:
			data.loc[index, ['lat']] = [0]

	data = data[data['lat'] != 0].reset_index(drop=True)

	return data


# only show some amenity of the data
def store_partial_data(data):
	food_data = data[data['amenity'] == 'food'].reset_index(drop=True)
	transportation_data = data[data['amenity'] == 'transportation'].reset_index(drop=True)
	entertainment_data = data[data['amenity'] == 'entertainment'].reset_index(drop=True)
	living_stroage_data = data[data['amenity'] == 'living_stroage'].reset_index(drop=True)
	shopping_banking_data = data[data['amenity'] == 'shopping_banking'].reset_index(drop=True)

	food_data.to_csv('data/food.csv')
	transportation_data.to_csv('data/transportation.csv')
	entertainment_data.to_csv('data/entertainment.csv')
	living_stroage_data.to_csv('data/living_stroage.csv')
	shopping_banking_data.to_csv('data/shopping_banking.csv')


def main():
	data = pd.read_json("../osm/amenities-vancouver.json.gz", lines=True)			# read data
	drop_useless_data = drop_useless_amenities(data)								# remove irrevalent amenities
	combine_samilar_data = combine_samilar_amenities(drop_useless_data)				# group similar amenities
	not_null_data = remove_null_name(combine_samilar_data)							# remove null name rows
	not_outlier_data = remove_outlier(not_null_data)								# remove  outlier

	not_outlier_data.to_csv('data/cleaned_data.csv')
	store_partial_data(not_outlier_data)

if __name__=='__main__':
	main()







