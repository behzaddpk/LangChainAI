import os
import requests
from dotenv import load_dotenv


load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrap information from linkedIn profile
        Manually scrapp the information from the linkedin profile
    """



    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/behzaddpk/7de04a0fcc88e0355732ae72ccad3761/raw/cdbe0e4f073bda5a0017a9664c7100c9f202e7bc/behzad-json"
        response = requests.get(linkedin_profile_url, timeout=10)

    else:
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        headers = {'Authorization': f'Bearer zsqJErIJBiC8c4tzoowhOA'}
        response = requests.get(api_endpoint, params={'url': linkedin_profile_url}, headers=headers, timeout=10)


    data = response.json()

    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/behzaddpk",
        )
    )