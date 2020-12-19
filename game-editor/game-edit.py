## Game Editor ###############################################################
# This application manages data files for the Cornventure game engine.
##############################################################################

class GameObjectManager:
	def __init__(self):
		# Keep track of the maximum value used for an ID, to ensure that no
		#  duplicates arise. If you delete IDs, those numbers will simply not
		#  appear for this game. 
		self.max_id = 0
		self.rooms = []
		self.areas = []
		self.creatures = []
		self.features = []
		self.items = []


	def load_file(self, filename, type, merge):
		pass


	def add_room(self, name, desc_short, desc_full, exits, areas, creatures,
		         features, items, attributes):

		# Create a new room dict and add the universal stuff to it.
		new_room = {}
		new_room["id"] = self.max_id + 1
		self.max_id += 1

		new_room["name"] = name
		new_room["desc_short"] = desc_short
		new_room["desc_full"] = desc_full

		# A new room canhave either areas or other items, not both.
		if areas != []:
			new_room["areas"] = areas
		else:
			new_room["exits"] = exits
			new_room["creatures"] = creatures
			new_room["features"] = features
			new_room["items"] = items
			new_room["attributes"] = attributes

		# With the new room put together, add it to the list for this game.
		self.rooms.append(new_room)


	def delete_room(self, room_id):
		for i in range(len(self.rooms)):
			if self.rooms[i]["id"] == room_id:
				del self.rooms[i]


	# Gets an ID by name for a type of data.
	def get_id_by_name(self, name, type):
		pass


