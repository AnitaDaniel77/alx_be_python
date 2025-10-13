import json

def process_json(data: dict, filename: str) -> dict:
    # Save the dictionary to a JSON file
    with open(filename, 'w') as f:
        json.dump(data, f)

    # Load the dictionary back from the JSON file
    with open(filename, 'r') as f:
        loaded_data = json.load(f)

    return loaded_data

# Test the function
if __name__ == "__main__":
    sample_data = {"name": "Anita", "role": "Back-End Developer"}
    result = process_json(sample_data, "sample.json")
    print("Loaded data:", result)
