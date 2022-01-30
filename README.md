# Welcome to Ultraverse!

## Inspiration
Marvel has always been and always will be the highest-grossing film franchise in the entertainment industry. But what makes their films so special compared to the rest? The experience. Every Marvel movie teleports its audience to the Marvel Cinematic Universe and immerses them in an epic storyline and cutting-edge visuals. 

Despite numerous streaming platforms, such as Netflix and Disney+, supporting Marvel movies, the pandemic still sits as a barrier between these Marvel fans and the superheroes they love. With Ultraverse, we bring Marvel fans the ultimate all-in-one platform for Marvel watch parties, superhero yoga breaks, and a movie map to interact with other Marvel fans. 

We aim to connect people together through the unforgettable Marvel experience! 

## What it does
Ultraverse provides a much-needed and vital getaway for many Marvel fans, especially during the ongoing pandemic. Ultraverse accelerates the expansion of the entertainment industry through its three main functions. First, it allows users to stream while creating real-world connections. Through navigating the `Events` page, users can host watch parties on their desired platform as well as browse and join upcoming watch parties. 

Additionally, we have a `Super Yoga` page to encourage people to relax their eyes and take a break from watching. Users can pose as some of their favorite superheroes, such as Captain America, Black Widow, Iron Man, and Captain Marvel—all the while improving strength, balance, and flexibility. When a user strikes the pose correctly, the trained models will indicate which superhero the user’s pose matches with. Furthermore, we also encourage users to invent their own superhero pose! 

Finally, Ultraverse features an integrated movie map of Atlanta, GA with pins detailing where Marvel movies were filmed. When a pin is clicked, it takes you to a movie page with information about the movie, videos with deleted scenes, and scenes from the film. There is also a live chat section for users to interact with each other. 

## How we built it
We used `HTML`, `CSS`, `Bootstrap`, `JavaScript`, `Azure Maps API`, and the `Django` framework to create the frontend and backend interfaces. For the data, we used Django’s default `SQLite database`. Our database stores users, events, and comments. The application was containerized via `Docker` and continuously deployed on `Azure` via the container registry and App Service. To automate the container build, run, and push processes, we built scripts to help automate the commands. 

In the machine learning part of our project, we utilized `Tensorflow.js` and `Teachable Machine` to develop our models for super yoga. First, we created multiple classes to classify our data and created our data sets by collecting images of each superhero yoga pose. After training our model, we were able to test the accuracy of our model by trying out each pose. 

With `Azure Maps API`, we created an interactive map of Georgia to display the locations at which Marvel movies were filmed. Using `HTML`, we added custom markers connecting the superhero to the location, which helped visualize the proximity of these filming spots. Finally, with `Javascript`, we implemented pop-ups to our markers which when clicked, take our users to the corresponding location highlight page, where they can learn more about the film and also interact with other users. 

## Challenges we ran into
On the front-end, we ran into the issue of using the same naming conventions in our styling. We quickly learned that specific naming conventions help create fewer bugs in the long run. On the backend, we ran into the issue of restricting the user who is currently logged in when submitting a form. A solution was found using class-based views, however, to keep the codebase simple for the rest of the team, we decided to stay with function-based views because class-based views have a higher learning curve and many built-in functions under the hood that aren’t immediately relevant to those new to the Django framework. 

Since we were working throughout the day and night, the accuracy of our machine learning model dramatically changed with changes in lighting, how far away we were from the camera, and varying locations. After spending many hours training and testing our model, our model accuracy is around 95%.

When deploying to Azure, we ran into issues with rendering our css and media files. We had several bugs when using the collectstatic command. Our site is deployed but does not have the correct styling and images. We are working to solve the problem! 

## Accomplishments that we're proud of
Going into creating Ultraverse we had a lot of ideas for how we could give our users an unforgettable experience by allowing them to connect and explore. We are proud of our teamwork and how we navigated different tasks like creating our Events, Marvel Map, and Superyoga pages. Dreaming big allowed us to explore machine learning and the Azure Maps API and that added to our user experience and website features. On the backend, we were able to add user registration functionality, authentication, and restricted views so only users with accounts could see pages other than the home page. The database was built using models, successfully rendered test data, and added data to the database via built forms that we were able to connect to the front end!

## What we learned
This experience provided us with an appreciation for product development and the nuances that are essential to creating a platform that requires many parts to connect harmoniously. We had the opportunity to explore new tools like the Azure Map API and Teachable Machine. Through our work on the project, we learned how quickly new skills can be developed. Overall, we gained a better understanding of the Django framework, modeling databases, manipulating data, and how to connect backend to frontend.

## What's next for Ultraverse
The team would love to continue to work on developing additional features for the platform to enhance our user’s experience and further elevate the influence of the entertainment industry. Some possible future additions include: 
- Resolve deployment issues with rendering css and media files
- Add a search bar feature to events and implement the ability to search and filter watch party events
- Adding update and delete functionality to watch party events and interactive user comments
- Ability to make watch party events private vs. public to certain user groups
- Include additional Machine Learning poses to include other Marvel characters
- Expand the map to show locations filmed at in the united states 
- Integrate GPS location to design city tours for Marvel fans and tourists alike! :) 

