from collections import Counter
from flask import Flask, render_template, request

app = Flask(__name__)

# Sample user profiles
user_profiles = {
    'Emma': {
        'Styles': ['Bohemian', 'Chic', 'Bohemian', 'Chic'],
        'Wishlist': ['Floral Maxi Dress', 'Silk Blouse', 'Boho Earrings', 'High-waisted Jeans']
    },
    'John': {
        'Styles': ['Streetwear', 'Streetwear', 'Minimalist', 'Streetwear'],
        'Wishlist': ['Graphic T-Shirts', 'Joggers', 'Minimalist Sneakers', 'Hoodie']
    }
}

# Function to blend preferences
def blend_preferences(profile1, profile2, profile1_name, profile2_name):
    styles1 = Counter(profile1['Styles'])
    styles2 = Counter(profile2['Styles'])

    # Blend styles
    blended_styles = styles1 + styles2

    # Generate a blend name
    top_styles = [style for style, count in blended_styles.most_common(2)]
    blend_name = f"{profile1_name[0]}{profile2_name[0]} {top_styles[0]}-{top_styles[1]}"

    # Recommendations
    combined_wishlist = list(set(profile1['Wishlist']) | set(profile2['Wishlist']))

    return blend_name, blended_styles, combined_wishlist

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blend_options')
def blend_options():
    return render_template('fashion_fusion.html', profiles=user_profiles.keys())

@app.route('/blend', methods=['POST'])
def blend():
    profile1_name = request.form.get('profile1')
    profile2_name = request.form.get('profile2')

    profile1 = user_profiles[profile1_name]
    profile2 = user_profiles[profile2_name]

    # Pass profile names to the function
    blend_name, blended_styles, combined_wishlist = blend_preferences(profile1, profile2, profile1_name, profile2_name)

    return render_template('result.html', blend_name=blend_name, blended_styles=blended_styles,
                           combined_wishlist=combined_wishlist)

@app.route('/latest_trends')
def latest_trends():

    trends = ['FLORAL', 'OVERSIZED','BEACH STYLE']
    return render_template('trends.html', trends=trends)

if __name__ == '__main__':
    app.run(debug=True)
