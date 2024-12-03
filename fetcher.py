import os
import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore, Back, Style, init

# Initialize colorma
init()

SuccessfulCardCount = 0
FailedCardCount = 0

# Load card names from cards.txt
with open("cards.txt", "r") as file:
    # Remove leading numbers and spaces from each line
    card_names = [re.sub(r'^\d+\s+', '', line.strip()) for line in file]

output_folder = "mtg_images"
os.makedirs(output_folder, exist_ok=True)

for card_name in card_names:
    print(Fore.BLACK + Back.WHITE +"--------------------------" + Style.RESET_ALL)
    print(f"Processing {card_name}...")


    try:
        # Fetch the card's page
        search_url = f"https://gatherer.wizards.com/Pages/Search/Default.aspx?name=+[{card_name.replace(' ', '+')}]"
        response = requests.get(search_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Locate the image URL
        image_tag = soup.find("img", alt=card_name)
        if not image_tag:
            print(Fore.YELLOW + f"Image tag not found for {card_name}."+ Style.RESET_ALL)
            FailedCardCount += 1
            continue

        image_url = image_tag.get("src")
        if not image_url:
            print(Fore.YELLOW + f"Image URL not found for {card_name}." + Style.RESET_ALL)
            continue

        # Fix malformed URLs
        if not image_url.startswith("http"):
            if image_url.startswith("/"):
                image_url = "https://gatherer.wizards.com" + image_url
            else:
                image_url = "https://gatherer.wizards.com/" + image_url

        print(f"Constructed image URL for {card_name}: {image_url}")

        # Download the image
        img_response = requests.get(image_url, stream=True)
        img_response.raise_for_status()

        # Save the image with the card name
        image_extension = ".jpeg" if "jpeg" in image_url else ".png"
        image_path = os.path.join(output_folder, f"{card_name}{image_extension}")
        with open(image_path, "wb") as img_file:
            for chunk in img_response.iter_content(1024):
                img_file.write(chunk)

        print(Fore.GREEN + f"Successfully downloaded {card_name}." + Style.RESET_ALL)
        SuccessfulCardCount += 1

        
    except Exception as e:
        print(Fore.RED + f"An error occurred with {card_name}: {e}"+ Style.RESET_ALL)
        
