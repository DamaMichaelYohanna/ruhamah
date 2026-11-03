# RUHAMAH

An editorial portfolio website for RUHAMAH, a contemporary womenswear house. The site uses Django templates, static CSS and vanilla JavaScript. It includes the home page, collection overview, story, lookbook, bespoke enquiry and contact pages.

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Start the development server with `python manage.py runserver`.
4. Open `http://127.0.0.1:8000/`.

## Content to replace before launch

- Seven customer-supplied photos are stored in `static/atelier/images/` and used across the homepage, collection pages, story and lookbook. Add further completed designs as they become available.
- The supplied transparent Ruhamah Wears logo is used in the header, side rail and footer.
- Add the business WhatsApp number, Instagram profile and email address in the footer/contact page. The WhatsApp enquiry opens a prefilled message but currently has no destination number.
- Set a deployment secret, production `DEBUG=False`, and production `ALLOWED_HOSTS` before publishing.
- The original project brief ended mid-sentence in its technical requirements section; this implementation follows the requirements available in the supplied text.
