# FAQ

## Who is the project owner?

A poor college student who is majoring in Computer Science @ UCSD.

## How does it work?

The program scrapes MyAnimeList for users and will write it to a database on GCP. We then use ML/DL to generate a recommendation using two common approaches.

## Issue Posting

Title: `Bug: ` or `Suggestion: ` etc.

Content: If you are reporting a bug, please provide a screenshot of the stack trace error or what exactly went wrong. If you have a suggestion, please provide drawings or detailed descriptions of what you would like to see. Do note that we are busy and it will take a while to implement additional functionality.

## Usage

Just input your MAL username and it will return a suggested list of anime for a user to watch.

## Requirements

- MyAnimeList account with at least 5 scored anime on your list (must be completed or in progress)
- Default anime list background (we have trouble parsing the different anime list styles out there)

## Running this on your own machine

You will need the latest MySQL version, yarn, and ReactJS. Make sure your MySQL server is setup to use unicode. `CREATE DATABASE [name];` and `CREATE TABLE IF NOT EXISTS USERS (USERHASH VARCHAR(191), ANIME VARCHAR(191), SCORE INT(10), UNIQUE (USERHASH, ANIME));` are the necessary commands