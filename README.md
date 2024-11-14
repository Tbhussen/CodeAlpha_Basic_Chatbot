# CodeAlpha_Basic_Chatbot
In this project a basic chatbot is created using python. While working on this project we created text file containing countries with their adjacent flags' colors.
## Detailed Discription
As part of the Python Programming Internship with Code Alpha, we worked on building a chatbot that is able of doing a basic conversation with a human user. The basic operations include: `Greetings`, `Thanks`, `GoodBye`, and `Asking about the name of the chatbot`.

We also managed to make this project more category based. So, we called this chatbot, flagbot. This flagbot called Rico is able to provide the user with the colors of any country he/she/they choose. During our work on this project, we created a text file containing the country with the corresponding flag color. This file could be easily searched using regex module(re) provided by python libraries. This file is the first if its kind on the Github.

To begin with, the libraries used in this module were: `NLTK`, `random`, and `re` libraries. 

We defined a pairs list that contained the possible input and its corresponding response. Then, in order to organize the input and response we created a _CustomChat_ class. In this class, we explicitly declare the random selection of a response for the inputted statement. This will allow future users of the code to create different responses that can be used to answer a "*hi*" greeting. Coming to our twist of taking the inputted country name and generating the corresponding colors of its flag. We used regex library to match the pattern of the country name and catch the part constituting the colors. The regex expression used is: `rf"{country}:(.*)\n"`.

The file containing the countries and the falg colors needs more development but since its out of the scope of this task we only provided some countries.

_Project Done_
