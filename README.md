# News-Tile-Bot

News-Tile-Bot is a web scraping application that fetches the latest articles titles from the [Bedroom Producers Blog](https://bedroomproducersblog.com/) and sends them via email using the Gmail API.

## Features

- Scrapes titles, links, and publication dates of articles from the blog.
- Sends scraped data as an email using the Gmail API.
- Allows scheduling tasks at regular intervals using the `schedule` library.

## Requirements

- Python 3.6 or higher
- Gmail account with configured OAuth2 credentials
- API key and secret, and set environment variables:
  - `GOOGLE_OAUTH2_CLIENT_ID`
  - `GOOGLE_OAUTH2_CLIENT_SECRET`
  - `GOOGLE_OAUTH2_REFRESH_TOKEN`
- Required packages listed in `requirements.txt`

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/news-title-bot.git
   cd news-title-bot

## Configuration

Create a .env file and add your Gmail API credentials:

 ```sh
GOOGLE_OAUTH2_CLIENT_ID=your_client_id
GOOGLE_OAUTH2_CLIENT_SECRET=your_client_secret
GOOGLE_OAUTH2_REFRESH_TOKEN=your_refresh_token
```

## Task scheduling

The application uses the schedule library to automatically run the task at specified intervals. You can adjust the interval by modifying the settings in main.py.