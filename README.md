# Otaku Recommender

An Anime Recommender System for when you're out of ideas

## FAQ

Please read [FAQ](faq.md) before reporting bugs/suggestions and learning how to run the program.

## Core Concept

- Scrape MAL for username and ratings
- Hash username and store in database with ratings
- When user asks for recommendation pull info from database and use machine learning/deep learning to generate a response
  - Collaborative - generates a recommendation based on similar users
  - Content-Based - generates a recommendation based on content tags
  - Hybrid - Uses both and combines into one model

## Libraries/Tools

- beautifulsoup4 - scraping MAL
- lxml - parsing HTML documents
- json - sorting user data
- threading - writing to database
- numpy - required by surprise
- pandas - data transform from database
- surprise - generate recommendations / switching to using keras and tensorflow
- [Full Stack](full_stack.md) on Google Cloud Platform

## Planned Updates

- [ ] Improve Collaborative Recommendation
- [ ] Implement Content-Based Recommendation
- [ ] Implement Hybrid Recommendation
- [x] Transfer database to AWS
- [x] Create a website
- [ ] Create an app

## Donate

Please consider donating to a poor college student :)

Bitcoin: `1Ka8e2rK9d2Hywgy1zbSQtFyR6m8mjyBf`

Ethereum: `0x8c970fBCD825D7a08A914BaA5d8b85660D222078`
