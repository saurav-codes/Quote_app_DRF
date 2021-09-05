# Quote_app_DRF <img src='https://cdn-icons-png.flaticon.com/128/1067/1067357.png' style='width:50px' />
This is a simple Rest API which can be used to fetch a quote with id or a list of quote. we can also do CRUD operation on the Quote. Also this app uses Beautiful Soup to scrap data from a Quote website &amp; save the data to the DataBase by using provided commands.

## After running local django server, headover to this url ##
<img style='width:35px' src='https://img-premium.flaticon.com/png/128/1674/premium/1674715.png?token=exp=1630814376~hmac=8052cfe95753455bd36934f55928a221' />               http://127.0.0.1:8000/api/quotes

## Here are the end-points to send request ##
- `GET /quote/<pk> - Get the quote based on the primary key `
- `GET /quotes - List all the quotes`
- `POST /quotes - Create a Quote`
- `DELETE /quote/<pk> - Delete a Quote`
- `PATCH /quote/<pk> - Partial Update a Quote`
- `PUT /quote/<pk> - Update a Quote`

### Commands to Scrape data from https://www.goodreads.com/quotes & save to DataBase ###
> python manage.py category qantity
### For Example if you want to extract 50 quotes related to life ###
> python manage.py life 50
