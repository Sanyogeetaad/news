
import streamlit as st
import requests

NEWS_API_ENDPOINT = 'https://newsapi.org/v2/top-headlines'
NEWS_API_KEY = st.secrets["NEWS_API_KEY"]   

def fetch_news(country, category=None):
    params = {
        'country': country,
        'apiKey': NEWS_API_KEY  
    }
    if category:
        params['category'] = category
    response = requests.get(NEWS_API_ENDPOINT, params=params)
    return response.json()
st.set_page_config(page_title='News Aggregator')
st.title('News Aggregator')
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1585241645927-c7a8e5840c42?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8Nnx8fGVufDB8fHx8&w=1000&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
# Choose the country
countries = ['US', 'GB', 'IN', 'CA', 'AU', 'FR', 'DE', 'JP', 'CN', 'RU', 'BR', 'MX', 'IT', 'ES', 'KR']# add more countries as needed
selected_country = st.sidebar.selectbox('Select a country', countries)

# Choose the category
categories = ['All','Business', 'Entertainment', 'General', 'Health', 'Science', 'Sports', 'Technology']
selected_category = st.sidebar.selectbox('Select a category (optional)', categories)

# Fetch the news
if selected_category == 'All':
    news = fetch_news(selected_country)
else:
    news = fetch_news(selected_country, category=selected_category)

# Search bar
search_query = st.text_input("Search for news:")
# Fetch the news with search query
news = fetch_news(selected_country, category=selected_category, q=search_query)

# Display the news articles
for article in news['articles']:
    st.write('###', article['title'])
    if article['urlToImage']:
        st.image(article['urlToImage'], use_column_width=True)
    st.write(article['url'])
  