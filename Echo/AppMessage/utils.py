# import json
# import os
# from django.conf import settings

# class JsonDataFrame:
#     def __init__(self, filename="errors.json"):
#         self.filepath = os.path.join(settings.BASE_DIR, 'AppMessage', filename)
#         self.data = self.read_json()

#     def read_json(self):
#         try:
#             with open(self.filepath, 'r') as file:
#                 return json.load(file)
#         except FileNotFoundError:
#             return []

#     def write_json(self):
#         with open(self.filepath, 'w') as file:
#             json.dump(self.data, file, indent=4)

#     def get_all(self):
#         return self.data

#     def add_entry(self, apiname, errormessage, successmessage):
#         new_id = max(item["id"] for item in self.data) + 1 if self.data else 1
#         new_entry = {
#             "id": new_id,
#             "apiname": apiname,
#             "errormessage": errormessage,
#             "successmessage": successmessage
#         }
#         self.data.append(new_entry)
#         self.write_json()

#     def delete_entry(self, entry_id):
#         self.data = [item for item in self.data if item["id"] != entry_id]
#         self.write_json()

#     def update_entry(self, entry_id, apiname=None, errormessage=None, successmessage=None):
#         for item in self.data:
#             if item["id"] == entry_id:
#                 if apiname:
#                     item["apiname"] = apiname
#                 if errormessage:
#                     item["errormessage"] = errormessage
#                 if successmessage:
#                     item["successmessage"] = successmessage
#                 break
#         self.write_json()
import os
import json
from django.conf import settings

class JsonDataFrame:
    def __init__(self, file_name='errors.json'):
        # Initialize the file path
        self.file_path = os.path.join(settings.BASE_DIR, 'AppMessage', file_name)
        
        # Ensure the file exists and load data
        self.load_data()

    def load_data(self):
        # Create the file with empty data if it does not exist
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump({"records": []}, file)
        
        # Load the existing data from the file
        with open(self.file_path, 'r') as file:
            self.data = json.load(file)

    def save_data(self):
        # Save the current data to the file
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_all(self):
        # Return all records
        return self.data

    def get_entry(self, id):
        # Retrieve a single entry by ID
        for entry in self.data:
            if entry['id'] == id:
                return entry
        return None
    

    def add_entry(self, apiname, errormessage, successmessage):
        # Add a new entry with a unique ID
        new_id = max((entry['id'] for entry in self.data), default=0) + 1
        self.data.append({
            'id': int(new_id),
            'apiname': apiname,
            'errormessage': errormessage,
            'successmessage': successmessage,
        })
        self.save_data()

    def update_entry(self, id, apiname, errormessage, successmessage):
        # Update an existing entry
        for entry in self.data:
            if entry['id'] == id:
                entry.update({
                    'apiname': apiname,
                    'errormessage': errormessage,
                    'successmessage': successmessage,
                })
                self.save_data()
                return
        raise ValueError('Entry not found')

    def delete_entry(self, id):
        # Delete an entry by ID
        self.data = [entry for entry in self.data if entry['id'] != id]
        self.save_data()
