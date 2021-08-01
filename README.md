# Web for collecting daily menu from the nearest restaurants from Technology Park in Brno 

## How is it implemented

1. Specify URLs on daily menu of restaurants (hardcoded)
2. Get todays date and week day in czech language
3. Get pages one by one from list of URLs with requests library
4. Parse content of the page with Beautiful Soup framework
5. Serialize information obtained from the page to tuple of dicts like this:<br>
   <code>({url: "https://some.url.com"<br>
       name: "JP",<br>
           menu: ("gulas", "smazak"),<br>
           polevka: ("jatrana s zeleninou", "dle denni nabidky")},<br> 
           ...)</code><br>
    If there is some error do:
    - put warning to the log
    - put None for `menu` and `polevak` in the returned tuple
    - display message like "Sorry, this page can't be parsed correctly."
    - **Link to the restaurant menu is show in any way**
6. Serialized data are sent to the HTML page and places based on the page template

## Features to do

- Map location
- How far is this restaurant is