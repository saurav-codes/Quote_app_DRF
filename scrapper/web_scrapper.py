from bs4 import BeautifulSoup
import requests
import re
from math import ceil



all_quotes= {}
global_countr= 1

def clean_quote(quote_uncleaned):
    # remove unwanted characters
    cleaned_quote1= re.sub('\n','',quote_uncleaned)
    cleaned_quote2= re.sub(' +',' ',cleaned_quote1)
    cleaned_quote3= re.sub(' “','',cleaned_quote2)
    cleaned_quote4= re.sub('.”','',cleaned_quote3)    
    cleaned_quote5= cleaned_quote4.strip() # remove trailing whitespaces
    return cleaned_quote5

def clean_author(author_txt):
    # get author name.. present before comma by splitting
    author= author_txt.split(',')
    final_txt1= re.sub('\n+','',author[0])
    cleaned_author= re.sub(' +',' ',final_txt1) # remove unwanted & trailing whitespaces
    cleaned_author1= cleaned_author.strip()
    return cleaned_author1


def clean_quote_and_author(quote_txt):
    quote_with_author= []
    # txt before "―" is our quote & txt after "―" is our author & other stuff
    quote_author_unclean= quote_txt.split('―') 
    cleaned_quote= clean_quote(quote_author_unclean[0]) # format quote
    cleaned_author= clean_author(quote_author_unclean[1]) # format author name
    # append author & quote to list
    quote_with_author.append(cleaned_quote)
    quote_with_author.append(cleaned_author)
    return quote_with_author


def makeSoup(url):
    resp_by_category= requests.get(url)
    htmlContent= resp_by_category.content
    soup= BeautifulSoup(htmlContent,'html.parser')
    return soup

def get_cloud_quotes_quantity(category):
    soup= makeSoup(f'https://www.goodreads.com/quotes/tag/{category}?page=1&utf8=%E2%9C%93')
    res= soup.find('span' ,class_='smallText')
    results= res.text
    if results:
        tmp_str_val= ''
        final_extracted_val= int()
        for indx in range(len(results)-1,8,-1):
            if results[indx]== ' ':
                break
            if results[indx]== ',':
                continue
            tmp_str_val+= results[indx]
        final_extracted_val= int(tmp_str_val)
        return final_extracted_val,soup
    else:
        return 0,soup

def scrap_single_page_data(soup,quantity,total_quotes_to_scrap):  
    countr= 1
    all_quotes_div= soup.findAll('div',class_='quoteText')
    for quote_div in all_quotes_div:
        quote_txt= quote_div.text 
        quot_and_author= clean_quote_and_author(quote_txt)   
        quote= quot_and_author[0]
        author= quot_and_author[1]  
        all_quotes[quote]= author 
        if countr == quantity:
            break 
        countr += 1 
        process_unformatted= (len(all_quotes)/total_quotes_to_scrap)*100
        process_round_off= round(process_unformatted,2)        
        print(f"Processing....{process_round_off}%")

def scrap_multi_page_data(no_of_pages, category, quantity):
    global all_quotes
    while len(all_quotes) < quantity: 
        for page_no in range(1, no_of_pages+1): 
            soup= makeSoup(f'https://www.goodreads.com/quotes/tag/{category}?page={page_no}&utf8=%E2%9C%93')
            if page_no != no_of_pages: 
                scrap_single_page_data(soup,30,quantity)  
            else:
                last_page_quantity= quantity % 30 
                scrap_single_page_data(soup,last_page_quantity,quantity)  


def get_quotes(category,quantity):
    if quantity< 1:
        print('please enter a greater number than 0')
        return
    cloud_quotes_quantity,soup= get_cloud_quotes_quantity(category)
    if cloud_quotes_quantity <=0:
        print(f"Sorry! we can't find any data for that Query. \nPlease Enter proper category like 'life', 'water',etc.,")
    elif cloud_quotes_quantity< quantity:
        print(f"Sorry, we can't find that much quantity of results\nwe only have {cloud_quotes_quantity} results.")
    else:
        if quantity <= 30: 
            scrap_single_page_data(soup,quantity,quantity) 
        elif quantity > 30:
            res= quantity 
            no_of_pages= ceil(res / 30) 
            scrap_multi_page_data(no_of_pages, category, quantity)


def scrap_quotes(category,quantity):
    get_quotes(category,quantity)
    if get_quotes:
        return all_quotes
    else:
        print('No Quote Found')


rec_d = scrap_quotes('inspiration',10)
countr= 1
for key,value in rec_d.items():
    print('===========================')
    print(f"{countr}. {key}")
    print('-',value)
    countr+= 1