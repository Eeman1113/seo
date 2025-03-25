import requests
from bs4 import BeautifulSoup

def extract_keywords(url):
    try:
        # Send a request to the website
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with class="tileKeyword"
        keywords = soup.find_all(class_='tileKeyword')

        # Extract and return the text from these elements
        return [keyword.get_text(strip=True) for keyword in keywords]

    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")
        return []

# Example usage
url = 'https://explodingtopics.com/'
keywords = extract_keywords(url)

# Print the extracted keywords
print("Extracted Keywords:")
for keyword in keywords:
    print(keyword)

df = open("seo.html", "a+")
df.write(f"<h1>Extracted Keywords:</h1>")
for i in range(0, 10000000):
    for keyword in keywords:
        df.write(f"<p>{keyword}</p>")
df.close()
