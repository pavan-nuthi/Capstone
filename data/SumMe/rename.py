import os

# List of video names in the desired order
video_order = [
    'Air_Force_One',
    'Base_jumping',
    'Bearpark_climbing',
    'Bike_Polo',
    'Bus_in_Rock_Tunnel',
    'Car_railcrossing',
    'Cockpit_Landing',
    'Cooking',
    'Eiffel_Tower',
    'Excavators_river_crossing',
    'Fire_Domino',
    'Jumps',
    'Kids_playing_in_leaves',
    'Notre_Dame',
    'Paintball',
    'Playing_on_water_slide',
    'Saving_dolphines',
    'Scuba',
    'St_Maarten_Landing',
    'Statue_of_Liberty',
    'Uncut_Evening_Flight',
    'Valparaiso_Downhill',
    'car_over_camera',
    'paluma_jump',
    'playing_ball'
]

# Path to the 'captions' folder
folder_path = './caption'

# Get the list of files in the folder
files = os.listdir(folder_path)

# Iterate through the files and rename them
for i, video_name in enumerate(video_order, start=1):
    # Find the corresponding file in the folder
    file_name = f"{video_name}.txt"
    file_path = os.path.join(folder_path, file_name)

    # Check if the file exists before renaming
    if os.path.exists(file_path):
        # Create the new file name with the 'video_' prefix and the order number
        new_file_name = f"video_{i}.txt"
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(file_path, new_file_path)
        print(f"Renamed {file_name} to {new_file_name}")
    else:
        print(f"File {file_name} not found in the folder.")