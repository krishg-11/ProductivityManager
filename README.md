# ProductivityManager
## Inspiration
We noticed online school is difficult for many students. After hours of staring at a screen at home and listening to virtual lectures, students must remain focused in front of their computers and complete all the assignments they may have. A lot of our peers have mentioned how they fall victim to the endless distractions of the internet or even end up falling asleep while they are studying. We wanted to fix these problems with the Productivity Manager. Though the sudden changes of online school have been jarring for most, we expect the Productivity Manager to be just as effective when we all return to in-person learning. With Productivity Manager, students will learn the practice of self-discipline as they are reminded to stay on task whenever they have the application running.

## What it does
Productivity Manager has numerous features. 1. Eye-tracking -- the student's webcam detects when the student's eyes have been closed for an extended period of time (they have fallen asleep). 2. Phone detection -- the student will be notified if they are distracted by their phone. 3. Tab-switching -- the application will be able to monitor what other tabs the students are currently using and if they prove to be distracting or not. Lastly, the Productivity Manager will present a summary graph once the student chooses to end their session, displaying their aggregate level of focus over time.

## How we built it
We deployed the website using the Flask framework and built it using HTML and Javascript. Frames of data from the user's webcam are used and analyzed for our numerous features. We also used Socket.io to communicate data from the frontend to the backend.

## Challenges we ran into
It was difficult to integrate webcam data into Flask to be processed by our machine learning models. We also had some difficulty working with Socket.io, as we had little experience with it previously.

## Accomplishments that we're proud of
We did not think we would be able to smoothly process a full video stream and have multiple layers of analysis on it. We are also proud of our website which proves to be user-friendly and appealing to look at.

## What we learned
We learned how to integrate cloud computing services with our website and process live video feed data. Compiling everything in an organized video was also a challenging task that we learned to work through.

## What's next for Productivity Manager
We aim to add more features to the Productivity Manager and remove any small issues to make it not much of a hindrance for the user, but rather have it running smoothly in the background whenever they are working. We also hope to improve the accuracy of our models to detect eyes and phones more instantaneously.
