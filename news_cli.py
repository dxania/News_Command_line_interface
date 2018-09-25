import click

import requests

@click.command()
# @click.option('--source', prompt = 'Choose a news source', help = 'News source name')

def choose_source():
    print("Press: 1 for BBC News")
    print("       2 for AL JAZEERA News")
    print("       3 for ABC News")
    print("       4 for BBC Sport")

    option = int(click.prompt("Select Preffered News Source"))
    if option == 1:
        bbc_news()
    elif option == 2:
        aljeez()
    elif option == 3:
        abc()
    elif option == 4:
        bbc_sport()
    else:
        print("Please choose an option from the list")
   
def bbc_news():
    url = ('https://newsapi.org/v2/top-headlines?' 'sources=bbc-news&' 'apiKey=7b1c53f9b76040109d71d0fc4533a21f')
    response = requests.get(url)
    json_file = response.json()
    news_articles = json_file['articles']

    for news in news_articles:
        click.secho(news['title'], fg='green', bold=True)
        click.echo(news['description'])
        click.secho("Find more on: " + click.style(news['url'], bold = True))
        click.echo("")

def aljeez():
    url = ('https://newsapi.org/v2/top-headlines?' 'sources=al-jazeera-english&' 'apiKey=7b1c53f9b76040109d71d0fc4533a21f')
    response = requests.get(url)
    json_file = response.json()
    news_articles = json_file['articles']

    for news in news_articles:
        click.secho(news['title'], fg='green', bold=True)
        click.echo(news['description'])
        click.secho("Find more on: " + click.style(news['url'], bold = True))
        click.echo("")

def abc():
    url = ('https://newsapi.org/v2/top-headlines?' 'sources=abc-news&' 'apiKey=7b1c53f9b76040109d71d0fc4533a21f')
    response = requests.get(url)
    json_file = response.json()
    news_articles = json_file['articles']

    for news in news_articles:
        click.secho(news['title'], fg='green', bold=True)
        click.echo(news['description'])
        click.secho("Find more on: " + click.style(news['url'], bold = True))
        click.echo("")

def bbc_sport():
    url = ('https://newsapi.org/v2/top-headlines?' 'sources=bbc-sport&' 'pageSize=10&' 'apiKey=7b1c53f9b76040109d71d0fc4533a21f')
    response = requests.get(url)
    json_file = response.json()
    news_articles = json_file['articles']

    for news in news_articles:
        click.secho(news['title'], fg='green', bold=True)
        click.echo(news['description'])
        click.secho("Find more on: " + click.style(news['url'], bold = True))
        click.echo("")


if __name__ == "__main__":
    choose_source()