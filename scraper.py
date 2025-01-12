import requests
from bs4 import BeautifulSoup
import re
 

def scrape_countries():
    url = "https://www.infoplease.com/countries"
    response = requests.get(url)
    # response2 = requests.get("https://www.infoplease.com/countries/Colombia")
    if response.status_code == 200:        
        soup = BeautifulSoup(response.content, 'html.parser')
        countries = []
        country_wrappers = soup.find_all(class_='country-wrapper')
        for child in country_wrappers:
            children=child.find('a').get('href')
            children=children.replace('/countries/','')
            children=children.replace('/country/','')
            # print(children)
            countries.append(children)
        # for wrapper in country_wrappers:
        #     country_name = wrapper.get_text()
        #     country_name = country_name.replace('\n', '').strip()
        #     country_name = country_name.replace(' ', '-').strip()
        #     country_name = country_name.replace('\'', '').strip()
        #     country_name = country_name.replace(',', '-').strip()
        #     countries.append(country_name)
        # soup2 = BeautifulSoup(response2.content, 'html.parser')
        keywords = [
            "President",
            "Chairman of the Presidency",
            "Prime Minister",
            "Land Area",
            "Population",
            "Capital City",
            "Other Large Cities",
            "Monetary Unit",
            "Languages",
            "Ethnicity/Race",
            "Religions",
            "Literacy Rate",
            "Economic Summary",
            "Communication",
            "Transportation",
            "International Disputes"
        ]
        for country in countries:
            f = open("countries", "a")
            f.write("\n")
            f.write("\n")
            f.write(f"{country.upper()}")
            f.write("\n")
            f.write("\n")
            f.write("\n")
            f.close()
            for keyword in keywords:
                country_url= requests.get(f"https://www.infoplease.com/countries/{country}")
                country_soup = BeautifulSoup(country_url.content, 'html.parser')
                match = country_soup.find(string=re.compile(keyword))
                if match:
                    if keyword == "Languages" or keyword == "Religions":
                        f = open("countries", "a")
                        f.write(match.parent.parent.parent.get_text())
                        f.write("\n")
                        f.write("\n")
                        f.close()
                    elif keyword == "Transportation" or keyword == "Communication":
                        f = open("countries", "a")
                        f.write(match.parent.parent.get_text())
                        f.write("\n")
                        f.write("\n")
                        f.close()
                    else:    
                        try:
                            f = open("countries", "a")
                            f.write(f"{keyword}: {match.parent.next_sibling.get_text()}")
                            f.write("\n")
                            f.write("\n")
                            f.close()
                            print(f"Done: {country}")
                        except AttributeError:
                            print("NoneType")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []

if __name__ == "__main__":
    countries = scrape_countries()
    # for country in countries:
    #     print(f"Country: {country['name']}, Link: {country['link']}")
