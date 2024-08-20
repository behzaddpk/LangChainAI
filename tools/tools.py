from langchain_community.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper


tavily_api_key = os.environ.get('TAVILY_API_KEY')
print(tavily_api_key)
tavilySearchApiWrapper = TavilySearchAPIWrapper(tavily_api_key=os.environ.get('TAVILY_API_KEY'))


def get_profile_url_tavily(name: str):
    """Searches for Linkedin or Twiteer profile Page."""
    search = TavilySearchResults(tavilySearchApiWrapper)
    res = search.run(f"{name}")
    return res[0]['url']