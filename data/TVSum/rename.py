import os

text_data = """
VT AwmHb44_ouw #1306 How to change tires for off road vehicles [Davidsfarm] https://www.youtube.com/watch?v=AwmHb44_ouw 5:54
VT 98MoyGZKHXc How to use a tyre repair kit - Which? guide https://www.youtube.com/watch?v=98MoyGZKHXc 3:07
VT J0nA4VgnoCo #0001: FLAT TIRE https://www.youtube.com/watch?v=J0nA4VgnoCo 9:44
VT gzDbaEs1Rlg ŠKODA Tips How to Repair Your Tyre https://www.youtube.com/watch?v=gzDbaEs1Rlg 4:48
VT XzYM3PfTM4w When to Replace Your Tires GMC https://www.youtube.com/watch?v=XzYM3PfTM4w 1:51
VU HT5vyqe0Xaw "The stuck truck of Mark, The rut that filled an afternoon." https://www.youtube.com/watch?v=HT5vyqe0Xaw 5:22
VU sTEELN-vY30 BBC - Train crash 2013 https://www.youtube.com/watch?v=sTEELN-vY30 2:29
VU vdmoEJ5YbrQ #453 girl gets van stuck in the back fourty [Davidsfarm] https://www.youtube.com/watch?v=vdmoEJ5YbrQ 5:29
VU xwqBXPGE9pQ Smart Electric Vehicle Balances on Two Wheels https://www.youtube.com/watch?v=xwqBXPGE9pQ 3:53
VU akI8YFjEmUw Electric cars making earth more green https://www.youtube.com/watch?v=akI8YFjEmUw 2:13
GA i3wAGJaaktw "Pet Joy Spa Grooming Services | Brentwood, CA (310) 471-0088" https://www.youtube.com/watch?v=i3wAGJaaktw 2:36
GA Bhxk-O1Y7Ho "Vlog #509 I'M A PUPPY DOG GROOMER! September 13, 2014" https://www.youtube.com/watch?v=Bhxk-O1Y7Ho 7:30
GA 0tmA_C6XwfM Nail clipper Gloria Pets professional grooming https://www.youtube.com/watch?v=0tmA_C6XwfM 2:21
GA 3eYKfiOEJNs Dog Grooming in Buenos Aires https://www.youtube.com/watch?v=3eYKfiOEJNs 3:14
GA xxdtq8mxegs How to Clean Your Dog's Ears - Vetoquinol USA https://www.youtube.com/watch?v=xxdtq8mxegs 2:24
MS WG0MBPpPC6I Mexican Fried Chicken Sandwich Recipe https://www.youtube.com/watch?v=WG0MBPpPC6I 6:37
MS Hl-__g2gn_A Reuben Sandwich with Corned Beef & Sauerkraut https://www.youtube.com/watch?v=Hl-__g2gn_A 4:03
MS Yi4Ij2NM7U4 Poor Man's Meals: Spicy Sausage Sandwich https://www.youtube.com/watch?v=Yi4Ij2NM7U4 6:45
MS 37rzWOQsNIw Saigon Sandwich - Vietnamese Sandwiches in San Francisco CA https://www.youtube.com/watch?v=37rzWOQsNIw 3:11
MS LRw_obCPUt0 GoogaMooga Sneak Peek Joseph Leonard's Fried Chicken Sandwich cooking video https://www.youtube.com/watch?v=LRw_obCPUt0 4:20
PK cjibtmSLxQ4 David Belle | Fondateur du parkour | Reportage de TF1 https://www.youtube.com/watch?v=cjibtmSLxQ4 10:47
PK b626MiF1ew4 Charlotte Parkour | Charlotte Video Project https://www.youtube.com/watch?v=b626MiF1ew4 3:55
PK XkqCExn6_Us Singapore Parkour Free Running | JC Boy Late for School https://www.youtube.com/watch?v=XkqCExn6_Us 3:08
PK GsAD1KT1xo8 Parkour Camp Leipzig https://www.youtube.com/watch?v=GsAD1KT1xo8 2:25
PK PJrm840pAUI Vivencias: Jam Parkour Viña del Mar 2012 https://www.youtube.com/watch?v=PJrm840pAUI 4:34
PR 91IHQYk1IQM Chinese New Year Parade 2012 New York City Chinatown https://www.youtube.com/watch?v=91IHQYk1IQM 1:50
PR RBCABdttQmI 2013 Alumnae Parade & Laurel Chain Ceremony https://www.youtube.com/watch?v=RBCABdttQmI 6:04
PR z_6gVvQb2d0 LA Kings Stanley Cup South Bay Parade 2014 https://www.youtube.com/watch?v=z_6gVvQb2d0 4:36
PR fWutDQy1nnY Chinatown Parade https://www.youtube.com/watch?v=fWutDQy1nnY 9:45
PR 4wU_LUjG5Ic Southend-on-Sea and Kortrijk Bike Friendly Cities Parades https://www.youtube.com/watch?v=4wU_LUjG5Ic 2:47
FM VuWGsYPqAX8 "Flash mob protest for Syria | Sydney, Australia, May 2012 | #Silenceisbetrayal" https://www.youtube.com/watch?v=VuWGsYPqAX8 3:36
FM JKpqYvAdIsw ICC World Twenty20 Bangladesh 2014 Flash Mob - Pabna University of Science & Technology ( PUST ) https://www.youtube.com/watch?v=JKpqYvAdIsw 2:32
FM xmEERLqJ2kU Bluffton Teachers Flash Mob Dance (A Staff that Cares About Their Students) https://www.youtube.com/watch?v=xmEERLqJ2kU 7:26
FM byxOvuiIJV0 "ICC World Twenty 20 Bangladesh 2014, Flash Mob - UITS, Chittagong (Official)" https://www.youtube.com/watch?v=byxOvuiIJV0 2:34
FM _xMr-HKMfVA CASACL - Flashmob in Copenhagen underground - Peer Gynt https://www.youtube.com/watch?v=_xMr-HKMfVA 2:29
BK WxtbjNsCQ8A Beekeeping101.mov https://www.youtube.com/watch?v=WxtbjNsCQ8A 4:25
BK uGu_10sucQo A Year of Beekeeping https://www.youtube.com/watch?v=uGu_10sucQo 2:47
BK EE-bNr36nyA Paper Wasp Removal | From the Ground Up https://www.youtube.com/watch?v=EE-bNr36nyA 1:38
BK Se3oxnaPsz0 9/15/11 Killer Bees Kill 1000-lb Hog in Bisbee AZ https://www.youtube.com/watch?v=Se3oxnaPsz0 2:18
BK oDXZc0tZe04 Apis Mellifera in a Vertical Log Hive https://www.youtube.com/watch?v=oDXZc0tZe04 6:20
BT qqR6AEXwxoQ Motocross Tips & Tricks : How to Whip a Motocross Bike https://www.youtube.com/watch?v=qqR6AEXwxoQ 4:29
BT EYqVtI9YWJA Smage Bros. Motorcycle Stunt Show https://www.youtube.com/watch?v=EYqVtI9YWJA 3:18
BT eQu1rNs0an0 How to stop your Fixie https://www.youtube.com/watch?v=eQu1rNs0an0 2:44
BT JgHubY5Vw3Y How to lock your bike. The RIGHT way! https://www.youtube.com/watch?v=JgHubY5Vw3Y 2:23
BT iVt07TCkFM0 Pure Fix TV: How to Wheelie https://www.youtube.com/watch?v=iVt07TCkFM0 1:44
DS E11zDS9XGzg German Shepherd Dog Show (KCI) | DoHangout https://www.youtube.com/watch?v=E11zDS9XGzg 8:30
DS NyBmCxDoHJU The Dog Show HD 720p https://www.youtube.com/watch?v=NyBmCxDoHJU 3:09
DS kLxoNp-UchI Oliver's Show - Dog's tale https://www.youtube.com/watch?v=kLxoNp-UchI 2:10
DS jcoYJXDG9sw TODAY- Obie the obese dog works toward weight loss https://www.youtube.com/watch?v=jcoYJXDG9sw 3:19
DS -esJrBWj2d8 Will A Cat Eat Dog Food? https://www.youtube.com/watch?v=-esJrBWj2d8 3:50
"""

# Split the text into lines
lines = text_data.strip().split('\n')

# Extract the second word from each line
second_words = [line.split()[1] for line in lines]
# print(second_words)

# Path to the 'captions' folder
folder_path = './caption'

# Get the list of files in the folder
files = os.listdir(folder_path)

# Iterate through the files and rename them
for i, video_name in enumerate(second_words, start=1):
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