# CLI based facebook posts scraping tool

usage: main.py [-h] [-s] [--fetch_all]

This application collects facebook posts about a certain subject

optional arguments:<br>
  -h, --help      : show this help message and exit<br>
  -s , --subject  : Subject to research<br>
  --fetch_all     : Show subjects in database

  <hr>

To use this app please use these commands

To collect data from facebook use the following command then enter your credential (don't worry no one will see your password)

```bash
facebook_posts_scraper>python ./main.py -s 'subject name'
```
or
```bash
facebook_posts_scraper>python ./main.py --suject 'subject name'
```

to display collected data inside the mongodb collection please use the following command

```bash
facebook_posts_scraper>python ./main.py --fetch_all
```

To display help : 

```bash
facebook_posts_scraper>python ./main.py -h
```
or
```bash
facebook_posts_scraper>python ./main.py --help
```