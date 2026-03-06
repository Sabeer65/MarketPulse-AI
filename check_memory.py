from database import get_past_data 

company = input('Enter a company name')

results = get_past_data(company)

results = get_past_data(company)

# Accessing the first result of the first query
distance = results['distances'][0][0]

if distance < 1.0:
    print(f"Found relevant past research (Distance: {distance}):")
    print(results['documents'][0][0])
else:
    print(f"No relevant research found. (Closest match was too far: {distance})")