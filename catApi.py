from flask import Flask, jsonify

app = Flask(__name__)

# Data for cat breeds and colors 
cat_data = {
    "breeds": [
        {
            "name": "Abyssinian",
            "description": "Abyssinian cats are known for their ticked coat and playful, active personalities.",
            "average_height": "8-10 inches",
            "average_weight": "6-10 pounds",
            "personality": ["Curious", "Playful", "Active"]
        },
        {
            "name": "American Bobtail",
            "description": "American Bobtail cats have a short, stubby tail and are known for their friendly, outgoing nature.",
            "average_height": "11-13 inches",
            "average_weight": "7-16 pounds",
            "personality": ["Friendly", "Intelligent", "Adaptable"]
        },
        {
            "name": "American Curl",
            "description": "American Curl cats have distinctive curled ears and are known for their affectionate, people-oriented nature.",
            "average_height": "8-11 inches",
            "average_weight": "5-10 pounds",
            "personality": ["Affectionate", "Social", "Playful"]
        },
        {
            "name": "American Wirehair",
            "description": "American Wirehair cats have a wiry, crimped coat and are known for their friendly, easygoing temperament.",
            "average_height": "8-10 inches",
            "average_weight": "8-12 pounds",
            "personality": ["Friendly", "Easygoing", "Affectionate"]
        },
        {
            "name": "Australian Mist",
            "description": "Australian Mist cats have a spotted coat and are known for their affectionate, sociable nature.",
            "average_height": "8-10 inches",
            "average_weight": "7-12 pounds",
            "personality": ["Affectionate", "Sociable", "Gentle"]
        },
        {
            "name": "Australian Tiffanie",
            "description": "Australian Tiffanie cats are longhaired versions of the Australian Mist, known for their luxurious coat and friendly demeanor.",
            "average_height": "8-10 inches",
            "average_weight": "7-12 pounds",
            "personality": ["Friendly", "Gentle", "Affectionate"]
        },
        {
            "name": "Balinese",
            "description": "Balinese cats are known for their sleek, silky coat and affectionate, vocal personality.",
            "average_height": "9-11 inches",
            "average_weight": "6-11 pounds",
            "personality": ["Affectionate", "Vocal", "Social"]
        },
        {
            "name": "Birman",
            "description": "Birman cats have striking blue eyes and a long, luxurious coat. They are known for their gentle, affectionate nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Gentle", "Affectionate", "Social"]
        },
        {
            "name": "Bombay",
            "description": "Bombay cats have sleek, black coats and are known for their friendly, affectionate personalities.",
            "average_height": "9-11 inches",
            "average_weight": "8-15 pounds",
            "personality": ["Friendly", "Affectionate", "Playful"]
        },
        {
            "name": "Burmese",
            "description": "Burmese cats are known for their sleek, muscular build and affectionate, outgoing personalities.",
            "average_height": "8-10 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Affectionate", "Social", "Playful"]
        },
        {
            "name": "Burmilla",
            "description": "Burmilla cats are a cross between Burmese and Chinchilla Persians, known for their playful and affectionate nature.",
            "average_height": "8-10 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Playful", "Affectionate", "Social"]
        },
        {
            "name": "California Spangled",
            "description": "California Spangled cats have a wild appearance with spotted coats and are known for their active, playful nature.",
            "average_height": "9-12 inches",
            "average_weight": "8-15 pounds",
            "personality": ["Active", "Playful", "Curious"]
        },
        {
            "name": "Chantilly-Tiffany",
            "description": "Chantilly-Tiffany cats have semi-longhair and are known for their affectionate, playful nature.",
            "average_height": "9-11 inches",
            "average_weight": "7-12 pounds",
            "personality": ["Affectionate", "Playful", "Gentle"]
        },
        {
            "name": "Chartreux",
            "description": "Chartreux cats have a robust build and blue-gray coat. They are known for their gentle, affectionate nature.",
            "average_height": "9-11 inches",
            "average_weight": "7-16 pounds",
            "personality": ["Gentle", "Affectionate", "Quiet"]
        },
        {
            "name": "Chausie",
            "description": "Chausie cats are a hybrid breed with a wild appearance and active, intelligent personality.",
            "average_height": "10-12 inches",
            "average_weight": "9-16 pounds",
            "personality": ["Active", "Intelligent", "Curious"]
        },
        {
            "name": "Cheetoh",
            "description": "Cheetoh cats are a cross between Bengal cats and Ocicats, known for their playful and energetic nature.",
            "average_height": "10-12 inches",
            "average_weight": "10-20 pounds",
            "personality": ["Playful", "Energetic", "Affectionate"]
        },
        {
            "name": "Cornish Rex",
            "description": "Cornish Rex cats have soft, curly coats and are known for their playful and affectionate nature.",
            "average_height": "10-12 inches",
            "average_weight": "5-9 pounds",
            "personality": ["Active", "Curious", "Affectionate"]
        },
        {
            "name": "Cymric",
            "description": "Cymric cats are longhaired versions of the Manx breed, known for their taillessness and friendly nature.",
            "average_height": "8-10 inches",
            "average_weight": "8-13 pounds",
            "personality": ["Friendly", "Affectionate", "Playful"]
        },
        {
            "name": "Devon Rex",
            "description": "Devon Rex cats have short, curly coats and are known for their playful, mischievous personalities.",
            "average_height": "9-11 inches",
            "average_weight": "5-10 pounds",
            "personality": ["Playful", "Mischievous", "Affectionate"]
        },
        {
            "name": "Donskoy",
            "description": "Donskoy cats are hairless and known for their affectionate, sociable nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Affectionate", "Sociable", "Curious"]
        },
        {
            "name": "Egyptian Mau",
            "description": "Egyptian Mau cats have a spotted coat and are known for their active, intelligent nature.",
            "average_height": "8-10 inches",
            "average_weight": "6-14 pounds",
            "personality": ["Active", "Intelligent", "Agile"]
        },
        {
            "name": "European Burmese",
            "description": "European Burmese cats are similar to Burmese but with a more moderate build.",
            "average_height": "8-10 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Affectionate", "Social", "Playful"]
        },
        {
            "name": "Exotic Shorthair",
            "description": "Exotic Shorthair cats have a short, plush coat and are known for their calm, affectionate nature.",
            "average_height": "8-10 inches",
            "average_weight": "8-15 pounds",
            "personality": ["Calm", "Affectionate", "Gentle"]
        },
        {
            "name": "German Rex",
            "description": "German Rex cats have a curly coat and are known for their playful, affectionate nature.",
            "average_height": "8-10 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Playful", "Affectionate", "Curious"]
        },
        {
            "name": "Havana Brown",
            "description": "Havana Brown cats have a rich, chocolate brown coat and are known for their affectionate, playful nature.",
            "average_height": "8-10 inches",
            "average_weight": "6-10 pounds",
            "personality": ["Affectionate", "Playful", "Intelligent"]
        },
        {
            "name": "Highlander",
            "description": "Highlander cats are a hybrid breed known for their large size, athletic build, and affectionate nature.",
            "average_height": "10-12 inches",
            "average_weight": "10-20 pounds",
            "personality": ["Affectionate", "Active", "Social"]
        },
        {
            "name": "Himalayan",
            "description": "Himalayan cats have a Persian-like appearance with pointed coloration and are known for their calm, affectionate nature.",
            "average_height": "9-11 inches",
            "average_weight": "7-12 pounds",
            "personality": ["Calm", "Affectionate", "Gentle"]
        },
        {
            "name": "Japanese Bobtail",
            "description": "Japanese Bobtail cats have a distinctive bobbed tail and are known for their playful, active nature.",
            "average_height": "8-10 inches",
            "average_weight": "6-10 pounds",
            "personality": ["Playful", "Active", "Intelligent"]
        },
        {
            "name": "Javanese",
            "description": "Javanese cats have a long, sleek coat and are known for their vocal, affectionate nature.",
            "average_height": "8-10 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Vocal", "Affectionate", "Social"]
        },
        {
            "name": "Khao Manee",
            "description": "Khao Manee cats have striking blue and yellow eyes and are known for their affectionate, social nature.",
            "average_height": "9-11 inches",
            "average_weight": "8-12 pounds",
            "personality": ["Affectionate", "Social", "Playful"]
        },
        {
            "name": "Korat",
            "description": "Korat cats have a silver-blue coat and are known for their affectionate, loyal nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-10 pounds",
            "personality": ["Affectionate", "Loyal", "Intelligent"]
        },
        {
            "name": "LaPerm",
            "description": "LaPerm cats have curly coats and are known for their affectionate, gentle nature.",
            "average_height": "8-10 inches",
            "average_weight": "6-10 pounds",
            "personality": ["Affectionate", "Gentle", "Playful"]
        },
        {
            "name": "Manx",
            "description": "Manx cats are tailless or have short tails and are known for their playful, social nature.",
            "average_height": "8-10 inches",
            "average_weight": "8-12 pounds",
            "personality": ["Playful", "Social", "Adaptable"]
        },
        {
            "name": "Mekong Bobtail",
            "description": "Mekong Bobtail cats have a distinctive bobbed tail and are known for their affectionate, playful nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Affectionate", "Playful", "Curious"]
        },
        {
            "name": "Minskin",
            "description": "Minskin cats are a small breed known for their short legs and affectionate, social nature.",
            "average_height": "6-8 inches",
            "average_weight": "4-7 pounds",
            "personality": ["Affectionate", "Social", "Playful"]
        },
        {
            "name": "Munchkin",
            "description": "Munchkin cats have short legs and are known for their playful, outgoing nature.",
            "average_height": "6-8 inches",
            "average_weight": "4-9 pounds",
            "personality": ["Playful", "Outgoing", "Friendly"]
        },
        {
            "name": "Napoleon",
            "description": "Napoleon cats are a cross between Munchkins and Persians, known for their playful and affectionate nature.",
            "average_height": "6-8 inches",
            "average_weight": "4-9 pounds",
            "personality": ["Playful", "Affectionate", "Curious"]
        },
        {
            "name": "Nebelung",
            "description": "Nebelung cats have a long, blue-gray coat and are known for their affectionate, shy nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Affectionate", "Shy", "Gentle"]
        },
        {
            "name": "Ocicat",
            "description": "Ocicat cats have a spotted coat and are known for their active, playful nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-14 pounds",
            "personality": ["Active", "Playful", "Curious"]
        },
        {
            "name": "Ojos Azules",
            "description": "Ojos Azules cats have striking blue eyes and are known for their affectionate, playful nature.",
            "average_height": "8-10 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Affectionate", "Playful", "Curious"]
        },
        {
            "name": "Oriental",
            "description": "Oriental cats have a slender build and are known for their vocal, affectionate nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Vocal", "Affectionate", "Social"]
        },
        {
            "name": "Oriental Bicolor",
            "description": "Oriental Bicolor cats have a spotted or marbled coat pattern and are known for their affectionate, social nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Affectionate", "Social", "Playful"]
        },
        {
            "name": "Oriental Longhair",
            "description": "Oriental Longhair cats have a long, sleek coat and are known for their vocal, affectionate nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Vocal", "Affectionate", "Social"]
        },
        {
            "name": "Peterbald",
            "description": "Peterbald cats are a hairless breed known for their affectionate, social nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Affectionate", "Social", "Curious"]
        },
        {
            "name": "Pixie-bob",
            "description": "Pixie-bob cats have a bobbed tail and are known for their affectionate, dog-like personality.",
            "average_height": "8-10 inches",
            "average_weight": "8-13 pounds",
            "personality": ["Affectionate", "Playful", "Loyal"]
        },
        {
            "name": "Ragamuffin",
            "description": "Ragamuffin cats are similar to Ragdolls, known for their large size, gentle nature, and tendency to go limp when picked up.",
            "average_height": "9-11 inches",
            "average_weight": "10-20 pounds",
            "personality": ["Gentle", "Affectionate", "Relaxed"]
        },
        {
            "name": "Savannah",
            "description": "Savannah cats are a hybrid breed with a wild appearance and are known for their energetic, playful nature.",
            "average_height": "9-11 inches",
            "average_weight": "12-25 pounds",
            "personality": ["Energetic", "Playful", "Social"]
        },
        {
            "name": "Selkirk Rex",
            "description": "Selkirk Rex cats have a curly coat and are known for their affectionate, laid-back nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-16 pounds",
            "personality": ["Affectionate", "Laid-back", "Curious"]
        },
        {
            "name": "Serengeti",
            "description": "Serengeti cats have a wild appearance with spotted coats and are known for their active, playful nature.",
            "average_height": "9-11 inches",
            "average_weight": "8-15 pounds",
            "personality": ["Active", "Playful", "Curious"]
        },
        {
            "name": "Siberian",
            "description": "Siberian cats have a thick, water-resistant coat and are known for their affectionate, dog-like nature.",
            "average_height": "9-11 inches",
            "average_weight": "8-17 pounds",
            "personality": ["Affectionate", "Friendly", "Intelligent"]
        },
        {
            "name": "Singapura",
            "description": "Singapura cats are small and have a ticked coat. They are known for their affectionate, playful nature.",
            "average_height": "6-8 inches",
            "average_weight": "4-8 pounds",
            "personality": ["Affectionate", "Playful", "Curious"]
        },
        {
            "name": "Snowshoe",
            "description": "Snowshoe cats have a pointed coat and distinctive white 'boots.' They are known for their affectionate, social nature.",
            "average_height": "8-10 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Affectionate", "Social", "Playful"]
        },
        {
            "name": "Sokoke",
            "description": "Sokoke cats have a distinctive tabby coat and are known for their active, friendly nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Active", "Friendly", "Curious"]
        },
        {
            "name": "Sokoke Forest Cat",
            "description": "Sokoke Forest Cats are a wild cat breed known for their spotted coat and active, independent nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Active", "Independent", "Curious"]
        },
        {
            "name": "Somali",
            "description": "Somali cats have a long, bushy tail and are known for their playful, affectionate nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Playful", "Affectionate", "Social"]
        },
        {
            "name": "Thai",
            "description": "Thai cats are the traditional Siamese breed with a rounder face and stockier build.",
            "average_height": "8-10 inches",
            "average_weight": "8-12 pounds",
            "personality": ["Affectionate", "Social", "Curious"]
        },
        {
            "name": "Thai Blue Point",
            "description": "Thai Blue Point cats are a color variation of the Thai breed, known for their pointed coloration and affectionate nature.",
            "average_height": "8-10 inches",
            "average_weight": "8-12 pounds",
            "personality": ["Affectionate", "Social", "Curious"]
        },
        {
            "name": "Thai Chocolate Point",
            "description": "Thai Chocolate Point cats are a color variation of the Thai breed, known for their pointed coloration and affectionate nature.",
            "average_height": "8-10 inches",
            "average_weight": "8-12 pounds",
            "personality": ["Affectionate", "Social", "Curious"]
        },
        {
            "name": "Thai Lilac",
            "description": "Thai Lilac cats are a color variation of the Thai breed, known for their pointed coloration and affectionate nature.",
            "average_height": "8-10 inches",
            "average_weight": "8-12 pounds",
            "personality": ["Affectionate", "Social", "Curious"]
        },
        {
            "name": "Thai Point Restriction",
            "description": "Thai Point Restriction cats are a color variation of the Thai breed, known for their pointed coloration and affectionate nature.",
            "average_height": "8-10 inches",
            "average_weight": "8-12 pounds",
            "personality": ["Affectionate", "Social", "Curious"]
        },
        {
            "name": "Thai Seal Point",
            "description": "Thai Seal Point cats are a color variation of the Thai breed, known for their pointed coloration and affectionate nature.",
            "average_height": "8-10 inches",
            "average_weight": "8-12 pounds",
            "personality": ["Affectionate", "Social", "Curious"]
        },
        {
            "name": "Tiffany",
            "description": "Tiffany cats are a longhaired version of the Chantilly-Tiffany breed, known for their affectionate, gentle nature.",
            "average_height": "9-11 inches",
            "average_weight": "7-12 pounds",
            "personality": ["Affectionate", "Gentle", "Playful"]
        },
        {
            "name": "Tonkinese",
            "description": "Tonkinese cats are a cross between Siamese and Burmese, known for their affectionate, playful nature.",
            "average_height": "8-10 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Affectionate", "Playful", "Social"]
        },
        {
            "name": "Toyger",
            "description": "Toyger cats have a tiger-like appearance and are known for their playful, outgoing nature.",
            "average_height": "8-10 inches",
            "average_weight": "7-15 pounds",
            "personality": ["Playful", "Outgoing", "Curious"]
        },
        {
            "name": "Turkish Angora",
            "description": "Turkish Angora cats have a long, silky coat and are known for their playful, intelligent nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Playful", "Intelligent", "Curious"]
        },
        {
            "name": "Turkish Van",
            "description": "Turkish Van cats have a white coat with colored markings and are known for their affectionate, energetic nature.",
            "average_height": "9-11 inches",
            "average_weight": "7-15 pounds",
            "personality": ["Affectionate", "Energetic", "Playful"]
        },
        {
            "name": "Ukrainian Levkoy",
            "description": "Ukrainian Levkoy cats have folded ears and are known for their affectionate, playful nature.",
            "average_height": "9-11 inches",
            "average_weight": "6-12 pounds",
            "personality": ["Affectionate", "Playful", "Curious"]
        },
        {
            "name": "York Chocolate",
            "description": "York Chocolate cats have a chocolate brown coat and are known for their affectionate, friendly nature.",
            "average_height": "8-10 inches",
            "average_weight": "7-15 pounds",
            "personality": ["Affectionate", "Friendly", "Gentle"]
        }
        # Add more breeds as needed
    ],
    "colors": [
        {"name": "Bicolor", "description": "Bicolor cats have two distinct colors, often white and another color."},
        {"name": "Black", "description": "Solid black cats are sleek and elegant."},
        {"name": "Blue (gray)", "description": "Blue (gray) cats have a bluish-gray coat."},
        {"name": "Blue-cream", "description": "Blue-cream cats have a bluish-gray and cream-colored coat."},
        {"name": "Brown", "description": "Brown cats have a solid brown coat."},
        {"name": "Calico", "description": "Calico cats have a tri-color coat with patches of white, black, and orange."},
        {"name": "Chocolate", "description": "Chocolate cats have a rich brown coat."},
        {"name": "Cinnamon", "description": "Cinnamon cats have a warm brown coat with reddish undertones."},
        {"name": "Colorpoint", "description": "Colorpoint cats have a lighter body color with darker points on the ears, face, paws, and tail."},
        {"name": "Cream", "description": "Cream cats have a pale, creamy-colored coat."},
        {"name": "Fawn", "description": "Fawn cats have a light tan coat."},
        {"name": "Lilac (lavender)", "description": "Lilac (lavender) cats have a pale, pinkish-gray coat."},
        {"name": "Red (also known as orange or ginger)", "description": "Red cats have a solid orange or ginger-colored coat."},
        {"name": "Seal", "description": "Seal cats have a dark brown coat with darker points on the ears, face, paws, and tail."},
        {"name": "Shaded", "description": "Shaded cats have a coat color that is lighter at the roots and darker at the tips."},
        {"name": "Silver", "description": "Silver cats have a coat with silver-tipped hairs."},
        {"name": "Smoke", "description": "Smoke cats have a coat color that is solid at the roots and gradually becomes lighter towards the tips."},
        {"name": "Tabby", "description": "Tabby cats have distinctive striped or marbled patterns."},
        {"name": "Tipped", "description": "Tipped cats have a coat color that is lighter at the tips."},
        {"name": "Tortoiseshell", "description": "Tortoiseshell cats have a tri-color coat with patches of black, orange, and sometimes cream."},
        {"name": "Tri-color", "description": "Tri-color cats have a coat with three distinct colors."},
        {"name": "White", "description": "White cats are often associated with purity and grace."}
        # Add more colors as needed
    ]
}



# Routes
@app.route('/breeds', methods=['GET'])
def get_breeds():
    return jsonify(cat_data['breeds'])

@app.route('/colors', methods=['GET'])
def get_colors():
    return jsonify(cat_data['colors'])

if __name__ == '__main__':
    app.run(debug=True)

