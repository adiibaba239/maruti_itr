# conditions.py

def get_user_conditions():
    website_name = input("Enter the name of your website: ")
    website_type = input("What type of website is it (e.g., blog, portfolio, business)? ")
    num_pages = int(input("How many pages will your website have? "))

    include_navigation = input("Do you want to include a navigation menu? (y/n): ").lower() == 'y'

    conditions = {
        "website_name": website_name,
        "website_type": website_type,
        "num_pages": num_pages,
        "include_styling": input("Do you want to include custom CSS styling? (y/n): ").lower() == 'y',
        "include_navigation": include_navigation,
        "num_nav_buttons": int(input("How many navigation buttons do you want? ")) if include_navigation else 0,
        "nav_button_style": input(
            "What kind of navigation buttons do you want (e.g., text, icons)? ") if include_navigation else None,
        "color_scheme": input("Choose a color scheme for your website (e.g., blue, green, #FF5733): "),
        "additional_features": {
            "include_footer": input("Do you want to include a footer? (y/n): ").lower() == 'y',
            "include_blog": input("Do you want to include a blog section? (y/n): ").lower() == 'y',
        },
    }

    return conditions
