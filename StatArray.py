import json


def add_to_json_file(frameWidth, frameHeight, spriteSheetUrl,frameCount):
    # Read the contents of the file
    with open("data.json", "r") as file:
        data = json.load(file)

    # Add a new dictionary to the list
    data.append({
        "frameWidth": frameWidth,
        "frameHeight": frameHeight,
        "spriteSheetUrl": spriteSheetUrl,
        "frameCount": frameCount,
    })

    # Write the updated JSON object back to the file
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
