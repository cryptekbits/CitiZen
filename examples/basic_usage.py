#!/usr/bin/env python3
"""
Basic usage example for the citizen module.
"""
import json
import os
import sys

# Add the project root directory to Python path
# This allows importing the citizen module regardless of where script is run from
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now import from citizen
from citizen import CityData

def print_json(data):
    """Print data as formatted JSON."""
    print(json.dumps(data, indent=2, ensure_ascii=False))

def main():
    """Main function."""
    # Create a CityData instance
    city_data = CityData()
    
    # Search for cities
    print("Searching for 'New York'...")
    cities = city_data.search_cities('New York', limit=5)
    print_json(cities)
    
    # Get cities near coordinates
    print("\nFinding cities near New York coordinates...")
    cities = city_data.get_cities_by_coordinates(40.7128, -74.0060, radius_km=10)
    print_json(cities)
    
    # Get a city by ID
    if cities:
        city_id = cities[0]['id']
        print(f"\nGetting city with ID {city_id}...")
        city = city_data.get_city_by_id(city_id)
        print_json(city)
    
    # Get a list of countries
    print("\nGetting a list of countries...")
    countries = city_data.get_countries()
    print(f"Found {len(countries)} countries")
    print(countries[:10])  # Print first 10 countries
    
    # Get states in a country
    print("\nGetting states in the United States...")
    states = city_data.get_states('United States')
    print(f"Found {len(states)} states")
    print(states[:10])  # Print first 10 states
    
    # Get cities in a state
    print("\nGetting cities in California, United States...")
    cities = city_data.get_cities_in_state('California', 'United States')
    print(f"Found {len(cities)} cities")
    print_json(cities[:5])  # Print first 5 cities
    
    # Close the connection
    city_data.close()

if __name__ == '__main__':
    main() 