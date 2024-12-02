data = [
   
  {
    "Colour": "GINGER",
    "Fit": "Large",
    "Size": "2XL",
    "fromdate": "9/24/2024, 12:00:00",
    "todate": "9/30/2024, 12:00:00",
    "price": "0"
  },
  {
    "Colour": "GINGER",
    "Fit": "Regular",
    "Size": "3XL",
    "fromdate": "9/26/2024, 12:00:00",
    "todate": "9/28/2024, 12:00:00",
    "price": "0"
  },
  {
    "Colour": "GREY",
    "Fit": "Regular",
    "Size": "2XL",
    "fromdate": "10/11/2024, 12:00:00",
    "todate": "10/16/2024, 12:00:00",
    "price": "0"
  },
  {
    "Colour": "GREY",
    "Fit": "Regular",
    "Size": "2XL",
    "fromdate": "9/26/2024, 12:00:00",
    "todate": "9/28/2024, 12:00:00",
    "price": "0"
  }
]




import datetime
unique_data = []
duplicate_data = []


seen_dicts = {}


for item in data:
    
    reduced_dict = {key: value for key, value in item.items() if key not in ['fromdate', 'todate', 'price']}
    
    
    reduced_tuple = tuple(reduced_dict.items()) 
    
    if reduced_tuple not in seen_dicts:
        
        seen_dicts[reduced_tuple] = 1
        unique_data.append(item)
    else:
        
        seen_dicts[reduced_tuple] += 1
        duplicate_data.append(item)


# def compare_dates(item1, item2):
#     """Compares date ranges to ensure they don't overlap."""
#     start1 = datetime.datetime.strptime(item1['fromdate'], '%m/%d/%Y, %H:%M:%S')
#     end1 = datetime.datetime.strptime(item1['todate'], '%m/%d/%Y, %H:%M:%S')
#     start2 = datetime.datetime.strptime(item2['fromdate'], '%m/%d/%Y, %H:%M:%S')
#     end2 = datetime.datetime.strptime(item2['todate'], '%m/%d/%Y, %H:%M:%S')

#     if start1 <= end2 and start2 <= end1:
#         return True  # Overlapping date ranges
#     return False


def compare_dates(item1, item2):
    
    start1 = datetime.datetime.strptime(item1['fromdate'], '%m/%d/%Y, %H:%M:%S').date()
    end1 = datetime.datetime.strptime(item1['todate'], '%m/%d/%Y, %H:%M:%S').date()
    start2 = datetime.datetime.strptime(item2['fromdate'], '%m/%d/%Y, %H:%M:%S').date()
    end2 = datetime.datetime.strptime(item2['todate'], '%m/%d/%Y, %H:%M:%S').date()

    if start1 <= end2 and start2 <= end1:
        return True  # Overlapping date ranges
    return False

def compare_items(item1, item2, exclude_keys):
    
    for key, value in item1.items():
        if key not in exclude_keys:
            if value != item2[key]:
                return False
    return True


for item in duplicate_data:
    for existing_item in unique_data:
        if compare_items(item, existing_item, ['fromdate', 'todate', 'price']) and compare_dates(item, existing_item):
            # Handle overlapping date ranges (e.g., raise an error or modify data)
            print("Overlapping date ranges:", item, existing_item)
            break


print(unique_data)





