# 🩺 First Aid Voice Assistant

A Python-based **First Aid** system with **voice command support** that can help in emergencies. The app allows users to speak their conditions (e.g., burn, cut, choking) and get the corresponding first aid steps. It can also send your **location and emergency message via WhatsApp** to your parent or contact.

---

## 🎯 Features

- ✅ **Voice command**: Speak your condition (e.g., "burn", "cut", "choking").
- ✅ **Location sharing**: Sends your current location to your parent via WhatsApp.
- ✅ **Emergency message**: Sends a custom emergency message based on your condition.
- ✅ **Data saving**: Saves user details (like name and phone number) in files for easy retrieval.
- ✅ **Future updates**: Will add automatic messaging if the mobile device is dropped (currently only on the laptop).

---

## 🚀 How to Use

1. **Run the program** (either normally or by running it from your IDE/terminal).
2. Click the **Voice Button** and **say your condition** (e.g., "burn").
3. Click **Run the Application**.
4. **Leave the app open** to continue using it.
5. Your **location** will be sent to your parent via WhatsApp, along with your **emergency message**.
6. **View the app output** in the terminal of your IDE (e.g., Visual Studio terminal).
7. All your **user data** (name, phone number, etc.) will be saved in files for later use.

---

## 🧠 Example Conditions You Can Say

- Burn  
- Cut  
- Choking  
- Nosebleed  
- Fracture

---

## 📦 Requirements

- Python 3.x
- `speechrecognition` for voice commands
- `pywhatkit` for WhatsApp integration
- `requests` for handling web requests
- `tkinter` *(usually built-in with Python)*

You can install the required packages using:

```bash
pip install -r requirements.txt
