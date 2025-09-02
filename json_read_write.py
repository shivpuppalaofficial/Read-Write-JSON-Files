
import json


def main():
    try:
        # Read JSON
        with open("data.json", "r") as f:
            data = json.load(f)

        print("✅ Original JSON data:")
        print(data)

        # Modify data (add a new entry)
        new_entry = {"Name": "Eve", "Age": 26, "Department": "Design"}
        data.append(new_entry)

        # Save JSON
        with open("data_output.json", "w") as f:
            json.dump(data, f, indent=4)

        print("\n💾 Data saved to data_output.json")

    except FileNotFoundError:
        print("❌ Please make sure 'data.json' exists in this folder.")


if __name__ == "__main__":
    main()
