# Simple Blackjack with Flask
This is a simple Flask app that allows a single user to play blackjack against
a computer-controlled dealer. I created this project as a way to explore Flask
and intend to update and expand it with new features as I grow more familiar
with the framework.
Because this project is intended to help me improve my knowledge of Flask
and Python, I will not be using any Javascript for the app's frontend unless
absolutely necessary in order to force myself to make the most of the features
that a Python backend makes available to me.

## Try It Out
You can play the latest stable version [here](https://simpleblackjack.herokuapp.com).

## Features
- Play a standard game of blackjack against a computer-controlled dealer.
- Hands are dealt from a persistent deck that is reshuffled when exhausted.
- Games are tracked separately by browser session and stored
  in a free Heroku Postgres database. Each game has its own deck and dealer.

## Frameworks/Extensions
- Flask
- SQLalchemy

## Tasks
- [x] Implement Deck and Player classes
- [x] Implement Blackjack class controlling gameplay
- [x] Implement simple Flask app with index and play routes
- [x] Expand app to take user input via link/query string
- [x] Expand app to display game state using HTML template
- [x] Implement static CSS to improve readability of HTML frontend
- [x] Complete unit testing of classes used to model game
- [x] Implement database to store and load game progress
- [x] Implement session tracking to allow multiple simultaneous games
- [ ] Test session and database functionality (in progress)
- [x] Launch app on free hosting platform
- [ ] Improve user interface using Flask-Bootstrap

## Known Issues
- Game continuity is session-based, meaning that rows of data that will never
  be reused because it is tied to a browser session that has ended will
  accumulate in the database. Because SQL databases do not natively support
  expiration (unlike most relational databases), this will require either a
  process to delete old entries or a shift from session-based to user-based
  storage. In either case, modifications to the database schema
  will be necessary.
- The user interface does not scale well to small screen sizes, such as mobile
  devices. This will be addressed in an overhaul of the interface following
  Flask-Bootstrap integration.
- The database schema cannot be easily modified due to the lack of database
  migration. It is necessary to fix this issue before implementing any changes
  requiring modifications to the database. I plan to implement a fix in a future
  update using Alembic.
