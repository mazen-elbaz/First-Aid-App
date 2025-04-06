from tkinter import *
import speech_recognition as sr
import re
def get_first_aid_steps(condition):
    steps_dict = {
        "bleeding": [
            "1. Wear protective gloves to avoid any risk of blood borne disease.",
            "2. Apply direct pressure to the bleeding site using clean gauze or cloth. If the cloth becomes soaked with blood, do not remove it. Instead, place another clean cloth on top.",
            "3. If the bleeding does not stop, consider applying pressure to specific pressure points (under the armpits or above the thighs)."
        ],
        "seizures": [
            "1. Ensure the safety of the patient.",
            "2. Avoid touching them or making loud noises that might trigger the nervous system.",
            "3. Wait 10-15 minutes for the episode to subside.",
            "4. Confirm that they are breathing naturally."
        ],
        "heart attack": [
            "1. Position the patient comfortably (semi-seated).",
            "2. Advise them not to exert any effort.",
            "3. If it is not their first episode, ask if they have medication they usually take in such situations.",
            "4. Wait 15 minutes. If the pain persists after taking the medication, transport them to the hospital."
        ],
        "choking": [
            "1. Stand behind the patient.",
            "2. Place your hands on their abdomen just below the rib cage, with your left hand forming a fist and the other hand gripping it tightly. Apply a strong upward thrust to help dislodge the object causing the choking.",
            "3. Ensure their breathing rate returns to normal."
        ],
        "burns": [
            "1. Move the victim to a cool place away from the heat of the burn area.",
            "2. Place the burned area under cool water for at least 10 minutes to cool the burn and protect the living tissue from further damage.",
            "3. Avoid applying ice or sticky substances directly to the wound, as this could make the situation worse."
        ],
        "second_degree_burns": [
            "1. Do not attempt to remove clothes that are stuck to the burn, but if necessary, gently cut them.",
            "2. Do not expose the burn area to water.",
            "3. Call for an ambulance and go to the hospital so the specialist can treat the burn."
        ],
        "poisoning": [
            "1. Lay the victim down.",
            "2. Call the doctor.",
            "3. Keep a sample of the vomit for the doctor to examine.",
            "4. Do not force the patient to vomit.",
            "5. Keep a sample of the suspected food for the doctor to examine.",
            "6. If the patient requests to drink, give them only a very small amount of water."
        ],
        "heatstroke": [
            "1. Move the patient to a cool place with air conditioning.",
            "2. Give the patient fluids.",
            "3. Cool the body by spraying it with water or using a cold cloth.",
            "4. Avoid giving the patient fever-reducing medication."
        ],
        "nosebleed": [
            "1. Ask him to sit and bend his head down to avoid swallowing blood.",
            "2. Wipe the nosebleed.",
            "3. Press on both sides of the nose and breathe through the mouth during this time."
        ],
        "unconscious": [
            "1. Call for an ambulance.",
            "2. Sit in the closest position to the injured person.",
            "3. Raise the hand on your side upwards.",
            "4. The hand on the opposite side, position it towards the patient's neck.",
            "5. Secure him around the hip and shoulder, then turn him towards the opposite side.",
            "6. Make sure he is breathing."
        ]
    }
    return steps_dict.get(condition.lower(), ["Sorry, no specific instructions available."])

def listen_for_instruction():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your voice command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Your condition is : {command}")
        label_main['text'] = f"Your condition is : {command}"
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand that. Please try again.")
        label_main['text'] = "Sorry, I could not understand that. Please try again."
        return None
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        label_main['text'] = "Sorry, there was an error with the speech recognition service."
        return None

def respond_to_command(command):
    print("Listening for your voice command...")
    label['text'] = 'Listening for your voice commands...'
    steps = get_first_aid_steps(command)
    print("\nFirst Aid Steps:")
    all_steps = ""
    for step in steps:
        print(step)
        all_steps += step + "\n"
    steps_label['text'] = all_steps


def print_conditions():
    condition = open('conditions.txt', 'r')
    all_conditions = ""
    for i in condition:
        all_conditions += i + "\n"
    condition.close()
    return all_conditions


def input_user(x):
    line = 0
    file = open('conditions.txt', 'r')
    for line_of_file in file:
        line += 1
    file.close()
    if x <= line:
        return x
    else:
        num_not_found()
        return input_user(x = int(input("Enter a number of Condition: ")))

def num_not_found():
    print("\nThe number does not exist!!!\nPlease try again!\n")

def emergency_contact(country):
    contacts = {
        "India": "112",
        "Egypt": "123",
        "South Korea":"119",
        "Switzerland":"144",
        "Italy":"118",
        "Brazil":"192",
        "Singapore":"995",
        "Malaysia":"994"
    }
    return contacts.get(country, "No contact found.")

allergy_steps = {
    "peanuts": "- Avoid exposure to peanuts.\n- Use an epinephrine injector if a reaction occurs.",
    "bees": "- Carry an epinephrine injector.\n- Move away from hives.",
    "milk": "- Avoid dairy products.\n- Carry lactic acid supplements if necessary.",
    "eggs": "- Avoid eggs.\n- Check food labels carefully for hidden egg ingredients.",
    "gluten": "- Avoid wheat and gluten-containing products.\n- Ensure food is labeled gluten-free.",
    "penicillin": "- Avoid penicillin.\n- Carry an alternative antibiotic prescription.",
    "lactic": "- Avoid contact with latex products.\n- Inform medical personnel of your allergy.",
    "dust": "- Avoid dusty environments.\n- Use a mask if necessary.",
    "pollen": "- Avoid outdoor activities during high pollen seasons.\n- Use antihistamines."
}
poison_steps = {
    "rat poison": "- Induce vomiting if directed by poison control.\n- Seek medical help.\n- Call Poison Control at 1-800-222-1222.",
    "bleach": "- Do not induce vomiting.\n- Rinse mouth and drink water.\n- Seek help.",
    "arsenic": "- Seek immediate medical attention.\n- Do not induce vomiting.",
    "carbon monoxide": "- Get to fresh air immediately.\n- Call emergency services.",
    "pesticides": "- Do not induce vomiting.\n- Rinse mouth and skin with plenty of water.\n- Call poison control immediately.",
    "acetone": "- Get fresh air immediately.\n- If swallowed, rinse mouth with water.\n- Seek medical assistance.",
    "benzene": "- Get fresh air immediately.\n- Seek medical attention.",
    "naphthalene": "- Do not induce vomiting.\n- Rinse mouth and seek medical help immediately.",
    "strong acids": "- Do not induce vomiting.\n- Rinse mouth and skin with plenty of water.\n- Seek immediate medical help.",
    "mercury": "- Do not induce vomiting.\n- Seek medical help immediately.\n- Do not touch spilled mercury.",
    "toxic gases": "- Leave the area immediately.\n- Get fresh air and call emergency services.",
    "natural pesticides": "- Rinse mouth and skin with water.\n- Call poison control for further advice.",
    "unknown": "- Call poison control immediately."
}
kit = {
        "camping": ["Bandages", "Antiseptic wipes", "Tweezers", "Pain relievers"],
        "office": ["Plasters", "Antiseptic cream", "Cold packs", "Scissors"],
        "travel": ["Motion sickness tablets", "Thermometer", "Hand sanitizer"],
        "hiking": ["Bandages", "Snake bite kit", "Blister pads", "Water purification tablets"],
        "sports": ["Ice packs", "Elastic bandages", "Pain relievers", "Splints"],
        "first aid training": ["CPR mask", "Defibrillator pads", "Bandages", "Burn pads", "Splints", "First Aid manual"],
        "swimming": ["Waterproof bandages", "Burn gel", "Sunscreen", "Antiseptic wipes"],
        "gardening": ["Bandages", "Antiseptic wipes", "Pain relievers", "Splints"],
        "air_travel": ["Motion sickness tablets", "Hand sanitizer", "Bandages", "Pain relievers"],
        "veterinary": ["Antiseptic wipes", "Bandages", "Gauze pads", "Tweezers"],
        "winter_activities": ["Thermal blankets", "Cold compresses", "Pain relievers", "Sunscreen"]
    }

def allegry(x):
    allergy_type = input("Please enter the type of allergy you have: ").lower()
    if allergy_type in allergy_steps:
        with open('conditions.txt', 'r') as file:
            for line in file:
                if x == int(line[0:2]):
                    if x == 11:
                        num=line[0:2]
                        content=line[3:]
        with open('write_conditions.txt', 'w') as file:
            file.write(f"Condition Number: {num}\n\n")
            file.write(f"Situation: {content}\n")
            file.write(f"Instructions: {allergy_steps[allergy_type]}\n" )
            file.write('*---------------------------------------------------------------------------------------------------------------------------------------------------------------------*\n')
            print("Data successfully written to 'write_conditions.txt'")
            return allergy_steps[allergy_type]
    else:
        print("Your allergy is not in our database, call 123.")
        return None

def poison(x):
    poison_type = input("\nPlease enter the type of poison you have been exposed to: ").lower()
    if poison_type in poison_steps:
        with open('conditions.txt', 'r') as file:
            for line in file:
                if x == int(line[0:2]):
                    if x == 12:
                        num=line[0:2]
                        content=line[3:]
        with open('write_conditions.txt', 'w') as file:
            file.write(f"Condition Number: {num}\n\n")
            file.write(f"Situation: {content}\n")
            file.write(f"Instructions: {poison_steps[poison_type]}\n" )
            file.write('*---------------------------------------------------------------------------------------------------------------------------------------------------------------------*\n')
            print("Data successfully written to 'write_conditions.txt'")
            return poison_steps[poison_type]
    else:
        print("No data available. Seek emergency assistance.")
        return None

def first_aid_kit(x):
    activity = input("Enter the activity (camping, office, travel, hiking, sports, First Aid training, Swimming, gardening, air_travel, Veterinary, winter_activities): ").lower()
    if activity in kit:
        with open('conditions.txt', 'r') as file:
            for line in file:
                if x == int(line[0:2]):
                    if x == 13:
                        num = line[0:2]
                        content = line[3:]
        with open('write_conditions.txt', 'w') as file:
            file.write(f"Condition Number: {num}\n\n")
            file.write(f"Situation: {content}\n")
            file.write(f"Instructions: {kit[activity]}\n")
            file.write(
                '*---------------------------------------------------------------------------------------------------------------------------------------------------------------------*\n')
            print("Data successfully written to 'write_conditions.txt'")
            return kit[activity]
    else:
        print("No data available. Seek emergency assistance.")
        return None

def read_file(x):
    list_instructions = [
        "1.wear protective gloves to avoid any risk of blood borne disease.\n"
        "2.Apply direct pressure to the bleeding site using clean gauze or cloth.if the cloth becomes soaked with blood,do not remove it instead,place another clean cloth on top.\n"
        "3.if the bleeding does not stop,consider applying pressure to specific pressure points (under the armpits or above the things.\n"
        ,
        "1.Ensure the safety of the patient.\n"
        "2.Avoid touching them or making loud noises that might trigger the nervous system.\n"
        "3.wait 10-15 minutes for the episode to subside.\n"
        "4.confirm that they are breathing naturally.\n"
        "5.check their pulse rate to ensure it is normal.\n"
        "6.tilt their head upward to open the airway.\n"
        "7.place them in the recovery position.\n"
        ,
        "1.position the patient comfortably(semi-seated).\n"
        "2.Advise them not to extra any effort.\n"
        "3.if it is not their first episode,ask if they have medication their usually take in such situations.\n"
        "4.wait 15 minutes. if the pain persists after taking the medication,transport them to the hospital.\n"
        ,
        "1.during an episode,move to a well-ventilated area away from crowds.\n"
        "2.Remove any tight clothing around the neck to facilitate breathing.\n"
        "3.for those with chronic conditions,use an inhaler during the episode by placing it in the mouth and taking a deep breath to help expand the airways.\n"
        ,
        "1.stand behind the patient.\n"
        "2.place your hands on their abdomen just below the rib cage,with your left hand forming a fist and the other hand gripping it tightly. Apply a strong upward thrust to help dislodge the object causing the choking.\n"
        "3.Ensure their breathing rate returns to normal.\n"
        ,
        '1.Move the victim to a cool place away from the heat of the burn area.\n'
        '2.Place the burned area under cool water for at least 10 minutes to cool the burn and protect the living tissue from further damage.\n'
        '3.Avoid applying ice or sticky substances directly to the wound, as this could make the situation worse.\n'
        ,
        '1.Do not attempt to remove clothes that are stuck to the burn, but if necessary, gently cut them.\n'
        '2.Do not expose the burn area to water.\n'
        '3.Call for an ambulance and go to the hospital so the specialist can treat the burn.\n'
        ,
        '1_Lay the victim down.\n'
        '2_Call the doctor.\n'
        '3_Keep a sample of the vomit for the doctor to examine.\n'
        '4_Do not force the patient to vomit.\n'
        '5_Keep a sample of the suspected food for the doctor to examine.\n'
        '6_If the patient requests to drink, give them only a very small amount of water.\n'
        ,
        '1_Move the patient to a cool place with air conditioning.\n'
        '2_Give the patient fluids.\n'
        '3_Cool the body by spraying it with water or using a cold cloth.\n'
        '4_Avoid giving the patient fever-reducing medication.\n'
        ,
        "1. Ask him to sit and bend his head down to avoid swallowing blood.\n"
        "2. Wipe the nosebleed.\n"
        "3. Press on both sides of the nose and breathe through the mouth during this time.\n"
        ,
        "1. Call for an ambulance.\n"
        "2. Sit in the closest position to the injured person.\n"
        "3. Raise the hand on your side upwards.\n"
        "4. The hand on the opposite side, position it towards the patient's neck.\n"
        "5. Secure him around the hip and shoulder, then turn him towards the opposite side.\n"
        "6. Make sure he is breathing.\n"
    ]
    file = open('conditions.txt', 'r')
    for line in file:
        if x == int(line[0]):
            file.close()
            return line[0], line[2:], list_instructions[x - 1]
        elif x== int(line[0:2]):
            if x==10:
                file.close()
                return line[0:2], line[3:], list_instructions[x]

def write_file(x):
    if x <= 10:
        num, content, info = read_file(x)
        if num and content and info:
           with open('write_conditions.txt', 'w') as file:
                file.write(f"Condition Number: {num}\n\n")
                file.write(f"Situation: {content}\n")
                file.write(f"Instructions: {info}\n" )
                file.write('*---------------------------------------------------------------------------------------------------------------------------------------------------------------------*\n')
                print("Data successfully written to 'write_conditions.txt'")
    elif x == 11:
        allegry(x)
    elif x == 12:
        poison(x)
    elif x == 13:
        first_aid_kit(x)
    else:
        print("No matching condition found.")

def validate_password(password):
    if len(password) < 6 or len(password) > 20:
        return "Password must be between 6 and 20 characters."
    if not re.search(r"[a-z]", password):
        return "Password must include at least one lowercase letter (a-z)."
    if not re.search(r"[A-Z]", password):
        return "Password must include at least one uppercase letter (A-Z)."
    if not re.search(r"[0-9]", password):
        return "Password must include at least one number (0-9)."
    if not re.search(r"[!$#@%&]", password):
        return "Password must include at least one special character (!, $, #, @, %, &)."
    return "Valid"

def ignore(x):
    num, content, info = read_file(x)
    if num and content and info:
        with open('write_conditions.txt', 'a') as file:
            file.write(f"Condition Number: {num}\n\n")
            file.write(f"Situation: {content}\n\n")
            file.write(f"instructions: {info}\n")
            file.write('*---------------------------------------------------------------------------------------------------------------------------------------------------------------------*\n')
        print("Data successfully written to 'write_conditions.txt'")
    else:
        print("No matching condition found.")
import json
from urllib.request import urlopen
import pywhatkit as kit
from datetime import datetime, timedelta
def get_location():
    try:
        url = "http://ip-api.com/json"
        response = urlopen(url, timeout=10)
        data = json.loads(response.read())
        # Extract latitude and longitude
        lat = data.get("lat")
        lon = data.get("lon")
        location_message = f"Latitude: {lat}, Longitude: {lon}"
        return location_message
    except Exception as e:
        return f"Error: {e}"

def send_emergency_message():
    phone_number = input("Please enter the phone number of your parent (beginning with +2): ")
    if not phone_number.startswith("+2"):
        print("Error: The phone number must start with +2.")
        return
    now = datetime.now()
    send_time = now + timedelta(minutes=1)  # Set the message to send after 1 minute
    hour = send_time.hour
    minute = send_time.minute
    # Get location message
    location_message = get_location()
    # Additional message to send to the parent
    parent_message =f"We are First Aid, here to assist your son/daughter.\n\nThey are in a difficult situation need your help.\n\nTheir current location is {location_message}\nplease reach them."
    # Send the message to WhatsApp
    print(f"Sending message to {phone_number}...")
    kit.sendwhatmsg(phone_number, parent_message, hour, minute)

def sign_up():
    username = input("Enter a new username: ")
    while True:
        password = input("Enter a new password: ")
        validation_result = validate_password(password)
        if validation_result == "Valid":
            with open("credentials.txt", "w") as file:
                file.write(f"{username}\n{password}")
            print("Sign-up successful!\nYour credentials have been saved.")
            return username, password
        else:
            print(f"⚠️Invalid Password: {validation_result}")

def login():
    try:
        with open("credentials.txt", "r") as file:
            saved_username = file.readline().strip()
            saved_password = file.readline().strip()
        print("Please enter your credentials to login.")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == saved_username and password == saved_password:
            print(f"Login successful!\nWelcome back, {username}!")
        else:
            print("⚠️Incorrect username or password.")
            login()
    except FileNotFoundError:
        print("⚠️No credentials found. Please sign up first.")
        sign_up()

def information():
    print("Now, please enter your personal information. This will be saved for future reference.")
    name = input("Enter your name: ").capitalize()
    age = input("Enter your age: ")
    while True:
        c = 0
        phone_1 = input("Enter \033[1mYour phone\033[0m number: ")
        phone_2 = input("Enter your \033[1mFather\033[0m or \033[1mMother number\033[0m: ")
        for i in range(len(phone_2) and len(phone_1)):
            c += 1
        if c == 11:
            break
        else:
            print("\033[1mMust 11 Number\033[0m!,",end="")
    print(f"Thank you,\033[1m{name}\033[0m")
    return name, age, phone_1, phone_2

def store_data_of_user():
    username, password = sign_up()
    name, age, phone_1, phone_2 = information()
    with open("Data_of_user.txt", "w") as file:
        file.write(f"Username: {username}\nPassword: {password}\n")
        file.write(f"Name: {name}\nAge: {age}\nHis Phone Number: {phone_1}\nParents Number: {phone_2}\n")
    print("Your data has been saved for reference.")
def sending_help_by_his_data():
    with open('Data_of_user.txt', 'r') as file:
        data = file.read()
    temp = data.split()
    if len(temp[-1]) == 11:
        phone_number = "+2" + temp[-1]
    with open('write_conditions.txt', 'r') as file:
        data = file.read()
        data = data.split()
    situation = []
    i = 0
    for word in data:
        if word == "Situation:":
            data = data[i+1 : -1]
        i += 1
    for word in data:
        if word == "instructions:":
            break
        situation.append(word)
    x = ''
    for word in situation:
        x += word + ' '
    content = x
    now = datetime.now()
    send_time = now + timedelta(minutes=1)  # Set the message to send after 1 minute
    hour = send_time.hour
    minute = send_time.minute
    # Get location message
    location_message = get_location()
    # Additional message to send to the parent
    parent_message = f"We are First Aid, here to assist your son/daughter.\n\nThey are in a difficult situation which is: {content} and need your help.\n\nTheir current location is {location_message}\nplease reach them."
    print(f"Sending message to {phone_number}...")
    kit.sendwhatmsg(phone_number, parent_message, hour, minute)

def identify():
    print("=" * 50)
    print("\033[1mWelcome to the First Aid System!\033[0m")
    print("=" * 50)
    print("In this system, we provide essential tools and support for emergencies.")
    print("To proceed, we need to confirm your role.")
    print("\033[1mOptions:\033[0m")
    print("1. Type 'Emergency Helper' or 'EH' if you are an Emergency Helper.")
    print("=" * 50)
    while True:
        identity = input("\nPlease confirm your role: ").strip().lower()
        if identity in ('emergency helper', 'eh'):
            print("✅ Thank you! Identity confirmed. Welcome, Emergency Helper!\n")
            return "Emergency Helper"
        else:
            print("\n⚠️ Invalid input! Please type 'Emergency Helper' or 'EH' to proceed.")
            print("Your role determines the features available to you in this system.")

def process_conditions():
    for i in range(5):
        try:
            x = int(input("Enter a number of Condition: "))
            input_user(x)
            read_file(x)
            write_file(x)
            country = input("Enter your country for emergency contact: ").capitalize()
            print(f"Emergency contact in {country}: {emergency_contact(country)}")
            x = input("You want to send your location for your Parents(y or n): ").lower()
            if x == 'y':
                send_emergency_message()
            else:
                continue
        except ValueError:
            print("⚠️ Please enter a valid number!")

#the_main_def
def composite_function():
    identify()
    print("1. Ignore (Free for 5 times only)\n2. Sign Up\n3. Login")
    while True:
        choice = input("Choose an option (1, 2, or 3): ").strip()
        if choice == '1':
            process_conditions()
            print("Please sign up for unlimited conditions!")
            choice = input("Do you want to sign up for unlimited access? (y/n): ").lower()
            if choice in ('y', 'yes'):
                sign_up()
                login()
                while True:
                    try:
                        x = int(input("Enter a number of Condition: "))
                        input_user(x)
                        read_file(x)
                        write_file(x)
                        country = input("Enter your country for emergency contact: ").capitalize()
                        print(f"Emergency contact in {country}: {emergency_contact(country)}")
                        sending_help_by_his_data()
                    except ValueError:
                        print("⚠️ Please enter a valid number!")
            elif choice in ('n', 'no'):
                print("No problem! Thank you for using our application!")
                break
            else:
                print("⚠️ Error! Please restart the program.")
                break
        elif choice == '2':
            store_data_of_user()
            login()
            while True:
                try:
                    x = int(input("Enter a number of Condition: "))
                    input_user(x)
                    read_file(x)
                    write_file(x)
                    country = input("Enter your country for emergency contact: ").capitalize()
                    print(f"Emergency contact in {country}: {emergency_contact(country)}")
                    x = input("You want to send your location and all you data for your Parents(y or n): ").lower()
                    if x in('y' , 'yes'):
                        sending_help_by_his_data()
                except ValueError:
                    print("⚠️ Please enter a valid number!")
        elif choice == '3':
            login()
            while True:
                try:
                    x = int(input("Enter a number of Condition: "))
                    input_user(x)
                    read_file(x)
                    write_file(x)
                    country = input("Enter your country for emergency contact: ").capitalize()
                    print(f"Emergency contact in {country}: {emergency_contact(country)}")
                    x = input("You want to send your location and all you data for your Parents(y or n): ").lower()
                    if x in ('y', 'yes'):
                        sending_help_by_his_data()
                except ValueError:
                    print("⚠️ Please enter a valid number!")
        else:
            print("⚠️ Invalid choice! Please try again.")

def main():
    print("Welcome to the First Aid Assistant!")
    #This changes the text of the label
    command = listen_for_instruction()
    if command:
        respond_to_command(command)


if __name__ == "__main__":
    root = Tk()
    root.geometry("1080x680")
    root.title("First Aid App")
    message1 = Label(root, text="Welcome to the First Aid App!", font=("cairo", 18, "bold"))
    message1.pack(pady=20)
    label= Label(root, text= "Welcome!")
    label.pack(pady=20)
    button = Button(root, text="VOICE", command = main,relief= 'flat', width = 10, height = 5, font=("Arial",12), bg = "red", fg = "white")
    button.config(width = 10, height = 5,borderwidth = 1, highlightthickness = 0 )
    button.place(x = 100, y = 100)
    button.pack(padx = 50, pady = 50)
    label_main = Label(root,text = "")
    label_main.pack()
    steps_label = Label(root,text = '')
    steps_label.pack(pady=20)
    # conditions_label = Label(root,text = '')
    # conditions_label.place(x = 10, y = 50)
    conditions_label = Label(root,text = print_conditions())
    conditions_label.place(x = 10, y = 10)
    composite_button = Button(root,text = "Run the application",command = composite_function)
    composite_button.pack(pady = 20)
    root.mainloop()







