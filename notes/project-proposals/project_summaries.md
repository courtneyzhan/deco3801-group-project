## Impact of Social Media on Mental Health - TearTech (60)
### System Concept Statement

**Problem Statement**: Design and develop a social media application that focuses on providing a positive social media experience for users.  

**High level description**: This application aims to provide a social experience for users that diminishes the negative aspects of social media and enhances the positive. It will be centred around gratitude journaling and sharing positive experiences with strangers and mood tracking.  

**Interaction paradigm**: User interfaces provided on both mobile and desktop devices. Interaction mode: Conversing (sharing content), exploring (viewing the social media feed) and manipulating (adding moods to be tracked)  

**Key interface metaphors**: Paper journaling (for the gratitude journaling aspect), calendar (for mood tracking), pinned pieces of paper (for newsfeed), similar to a noticeboard  

### General Functions
* Users
	* Anonymity (given an alias ala Piazza's "Anonymous Beaker")
	* Number of Posts posted today (max 1 Gratitude)
	* Calendar of Moods
	* Self Reflection Diary
	
* Posts
	* Title
	* Content
	* Associated User

* Gratitude Post (daily)
	* Subclass of Posts
	* Title is "What I am Grateful" (~)
	* Time posted

* Reflective Post (I guess as often as you want)
	* Subclass of Posts
	* Title is pulled from a predetermined sample
	* Time posted

* Self Reflection Diary
	* Subclass of Posts
	* Private (not in feed)
	
* Feed (shows chronological order 24 hours)
	* Gratitude Feed
	* Reflective Questions Feed (limited tp same question only)
	
* Mood Tracking
	* Associated User
	* Mood (5 emoji scale)
	* Date and Time (can be updated multiple times a day)

* App prompting (specific time to enter a mood)

* Self-Reflection
	* Personal Diary
	
* Mood Review
	* Section of viewing moods per time frame (day, week, month)

## UQ Car Pooling - FlashSquad (17)
### System Concept Statement
![17 System Concept Statement](/Users/courtney/work/uni/deco3801/Project_Proposals/17_System_Concept_Statement.png)

### General Functions
Users:

* Timetable (Dashboard)
	* Timetable (accessed via SSO login or uploaded)
	* Remind user of classes (typical timetable aspect)
* User Profile
	* Name
	* Major
	* Profile Picture
* Ride System
	* Current Location
	* Destination

Riding:

* Number of seats avaiable

Drivers:

* Subclass of Users -> Profile

Review:

* Driver 
* User who left review
* Review contents
* Rating

Reward System:
* If Driver, have specific rewards compared to User
* Discounts or whatever
* Point system

### Workflow
![17 Workflow](/Users/courtney/work/uni/deco3801/Project_Proposals/17_Workflow.png)

## Combating Fake News in Social Media - Here Come Ideas (24)
