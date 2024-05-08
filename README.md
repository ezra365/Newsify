# Newsify
LLM news summarisation tool

This tool is designed to summarise news articles from TechCrunch using the OpenAI and Langchain LLM model. The code contains a webscraper designed specifically for the html of this site, but the scraper is generelizable to any of the thematic categories on the website e.g., startups (https://techcrunch.com/category/startups/), AI (https://techcrunch.com/category/artificial-intelligence/), crypto (https://techcrunch.com/category/cryptocurrency/) and more. The model is then used to generate summaries for these news articles. The current parameter limit is set to 10 articles, but this can be changed in the code to suit the requirements of the user. 

Below is a set of general instructions on how to use the tool.

1) Clone the repository into your coding environment 

2) Install the required packages listed in requirements.txt if not already downloaded

3) Open script.qmd, and input your own OpenAI API key in the relevant section. If you want to keep your key private, you can use the .env file to store it or save it is as an environment variable in another file in your directory e.g., key.json. 

4) Run the script in chunks 1 and 2 to activate the scraper, tweaking any parameters of interest such as the topic category URL from TechCrunch, number of articles, sleep time. The code will scrape the TechCrunch website for the latest articles.

5) Run the script in chunk 3 to generate summaries for the articles scraped in chunk 2. The code will generate summaries for each article and save them in a dictionary. You may also choose to change the prompt engineering in the template to further suit your specific requirements.

6) Input some feedback on the summaries in chunk 4 and run the code to upload a feedback form to a database hosted on a Heroku SQL server. This will allow me to better understand specific use-cases and improve the quality of the model and prompt engineering accordingly.

Thanks for using!