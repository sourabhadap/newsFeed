

# Social Media Feed System

## Description
This is a social media system that allows users to sign up, log in, post feed items, follow other users, reply to feed items, upvote or downvote feed items and comments, and view their news feed. The system is designed using object-oriented principles, with classes representing different entities in the system and using in-memory to store the data.

The system is implemented in Python and the client code is implemented in main.py


## Design Patterns Implementation

The following design patterns are implemented in the system:

Singleton Pattern: The Session class is implemented using the Singleton pattern to ensure that only one instance of the class is created and used throughout the application to manage user sessions.

Strategy Pattern: The system allows users to sort their news feed based on different criteria (such as user, score, comments, or timestamp) by selecting a different sorting strategy. The Strategy pattern is implemented to encapsulate the different sorting algorithms and allow for easy swapping of sorting strategies.

Composite Pattern: The system allows users to post comments on feed items. The Composite pattern is implemented to allow users to post comments on feed items and to allow users to reply to comments.

#### Below patterns can be added for future implementation:

Observer Pattern: The system can be extended to allow users to subscribe to other users and receive notifications when the users they are subscribed to post new content. The Observer pattern can be implemented to allow users to subscribe to other users and receive notifications when the users they are subscribed to post new content.

Factory Pattern: The system can be extended to allow users to post different types of content (such as text, images, or videos). The Factory pattern can be implemented to allow users to post different types of content.
