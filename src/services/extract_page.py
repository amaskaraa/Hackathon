from playwright.sync_api import sync_playwright
import json

def extract_dom_attributes(url):
    with sync_playwright() as p:
        # Launch the browser (headless mode)
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the given URL
        page.goto(url)

        # Extract all elements on the page
        elements = page.query_selector_all('*')

        # Collect attributes for each element
        extracted_data = []
        for element in elements:
            attributes = element.evaluate("""el => {
                const attrs = {};
                for (const attr of el.attributes) {
                    attrs[attr.name] = attr.value;
                }
                return attrs;
            }""")
            extracted_data.append(attributes)

        # Close the browser
        browser.close()

        # Return extracted data
        return extracted_data
