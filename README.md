# Accord - Ask about Islam

<!-- <img src="docs/read-me-images/mock-up.png" ><br> -->

<hr>

## Table of contents

- [Accord - Ask about Islam](#code-innovate-chat-hub---group-chat-app)
  - [Table of contents](#table-of-contents)
  - [Overview](#overview)
  - [UX](#ux)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
      - [Colour Scheme](#colour-scheme)
      - [Fonts](#fonts)
      - [Visual Effects](#visual-effects)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [Account pages](#account-pages)
      - [Group chat/Homepage](#group-chathomepage)
      - [Messaging](#messaging)
      - [Profile Page](#profile-page)
      - [Header Navigation section](#header-navigation-section)
    - [Future Feature Considerations](#future-feature-considerations)
  - [Tools Used](#tools-used)
  - [Testing](#testing)
  - [Acknowledgements](#acknowledgements)

## Overview

"Accord" is a Python-based GUI project designed to facilitate scholarly discussions and knowledge sharing on religious topics. It features user signup and signin modules, channels for different religious topics, private messaging with scholars, Namaz reminders, and prayer timing displays. Additionally, it includes a calendar to track important dates and events, as well as the option to listen to the entire Quran and read its translation. "Accord" aims to create a user-friendly environment for seekers of knowledge and scholars to engage in meaningful discussions and receive guidance. With its intuitive navigation and engaging interface, "Accord" provides a seamless platform for individuals to deepen their understanding of religion and connect with experts in their field. Through personalized interactions and practical tools, it empowers users to navigate their spiritual journeys effectively while fostering a vibrant community of learning and exchange.
<br><br>
The full project can be accessed here [Accord](https://github.com/NoorFatimaAfzal/Accord/tree/main).
<br><br>

## UX

This App is created respecting the Five Plans Of Website Design:<br>

### Strategy<hr>

**Project Goal:**<br>
Create a website similar to Discord but specifically tailored for Religious puroposes.

**Project Objectives:**<br>

- Develop a real-time messaging platform to facilitate seamless religious communication among "Accord" community members.
- Implement a user-friendly interface with religious channels dedicated to various Religious topics, fostering organized discussions.
- Enhance user engagement in direct messages and group chat for interactive conversations.
- Establish secure user authentication, authorization, and profile management features to ensure a personalized and protected user experience.
  <br><br>

### Scope<hr>

**User Management**

- User registration and authentication with google.
- User roles and permissions for various levels of access.
- Profile creation and management.

**Communication Features**

- Real-time messaging functionality for group discussions in channels.
- Direct messaging for private one-on-one conversations.
- Notifications for Queries will be sent to scholar.

**Channel Management**

- Creation, joining, and leaving of channels.
- Categorization of channels based on Religious topics or modules.
- Ability to search relevant channels.

**User Interface and Experience**

- Intuitive and user-friendly interface for seamless navigation.
- Responsive design.
- Personalization options for user profiles.<br><br>


### Structure<hr>

The structure of the app is divided into different pages but with content depending on authentication and scholar/student status <br>

- **Register/Login/logout/email settings/password change** for this the File handling was used, the pages give the user the possibility to create an account, login or log out.<br>

- The **Home** page consists of 2 sections <br> 1.channels <b> 2.Direct messages list.They will be loaded using File Handling depending on the user clicks<br>

- The **header** is visible on all pages it consists of a search bar and a settings icon <br>


- The **Header Search bar** is used to find another user or find a specific channel the user is asked to type the @ symbol for users list or # for channels

- **Messages** contains an inbox to do the direct private messages to scholars. <br>

### Skeleton<hr>

**Wireframes**<br>
The wireframes for mobile and desktop were created with [Balsamiq]() tool and can be viewed [here]()<br>

<details>
  <summary>Wire Frames</summary>
  <h4>Channels list</h4>
  <!-- <img src="docs/read-me-images/wireframes/home-tab.png"><br> -->
  <h4>Delete account modal</h4>
  <!-- <img src="docs/read-me-images/wireframes/delete-account.png"><br> -->
  <h4>Login page</h4>
  <!-- <img src="docs/read-me-images/wireframes/login-page.png"><br> -->
  <h4>Logout page</h4>
  <!-- <img src="docs/read-me-images/wireframes/logout.png"><br> -->
  <h4>Messages</h4>
  <!-- <img src="docs/read-me-images/wireframes/messages-page.png"><br> -->
  <h4>Inbox</h4>
  <!-- <img src="docs/read-me-images/wireframes/messages-tab.png"><br> -->
  <h4>View profile</h4>
  <!-- <img src="docs/read-me-images/wireframes/profile-tab.png"><br> -->
  <h4>Sign up page</h4>
  <!-- <img src="docs/read-me-images/wireframes/register-page.png"><br> -->
  <h4>Header menu drop-down</h4>
  <!-- <img src="docs/read-me-images/wireframes/settings-drop-down.png"><br> -->
</details>
</details><br>

**FLOWCHARTS**<br>
The Flowchart for my program was created using <b>[draw.io](https://app.diagrams.net/)</b> and it visually represents how the system works.<br>
<img src="flowchart/flow.png"><br>
<br><br>


### Surface<hr>

#### Colour Scheme

- The primary colour scheme was used for body, headers and nav elements<br>
  <img src="color-scheme/clr1.jpg" width="30%">
  <img src="color-scheme/clr2.png" width="30%">
  <img src="color-scheme/clr3.jpeg" width="30%">
  <img src="color-scheme/clr4.png" width="30%">
  <img src="color-scheme/clr5.png" width="30%">
  <br>

- The secondary colour scheme was used for buttons, warnings, errors or for highlighting important information.<br>
  <img src="color-scheme/clr6.png" width="30%">
  <img src="color-scheme/clr7.png" width="30%">
  <img src="color-scheme/clr8.png" width="30%">
  <img src="color-scheme/clr9.png" width="30%">

#### Fonts

- The fonts I used for this site were imported from [Google Fonts](https://fonts.google.com/):<br>
  <!-- **H tags:** _EB Garamond, serif_<br>
  **body:** _Roboto, serif_<br> -->

#### Visual Effects

- **Box shadows** <br>
  Multiple box shadows were used for the cover, buttons and images. <br>

<details>
  <summary>Displaying notifications</summary>
<!-- <img src="docs/read-me-images/animations/notification1.png">
<img src="docs/read-me-images/animations/notification.png"><br> -->
</details>
<details>
  <summary>Search bar</summary>
<!-- <img src="docs/read-me-images/animations/search-bar.png">
<img src="docs/read-me-images/animations/search-bar1.png"><br> -->
</details>


## Features

### Existing Features<hr>

#### Account pages

   - Implement secure user signup and signin modules.
   - Allow users to create and manage their profiles.
   - Differentiate between regular users and scholars/experts.


- Sign in page<br><br>
  <!-- <img src="docs/read-me-images/sign-in.png" width="60%"><br><br> -->
- Sign up page<br><br>
  <!-- <img src="docs/read-me-images/sign-up.png" width="60%"><br><br> -->

#### Group chat/Homepage

- On the group chat homepage the page will have interface like this.

  1. The channels list <br><br>
     - The channels will be of different religious topics.
     - The scholars and users will be able to do group chat. <br><br>
       <!-- <img src="docs/read-me-images/channels-new-messages-list.png" width="60%"><br><br> -->
  2. The chat in a particular channel on which user has clicked.<br><br>
     <!-- <img src="docs/read-me-images/posts-list.png" width="60%"><br><br> -->

#### Messaging

- On the _Messages_ page, users can do private message to scholars in order to get their queries answered.
  <br><br>
  <!-- <img src="docs/read-me-images/messaging.png" width="70%"><br><br> -->

#### Profile Page

The Profile page (dashboard) is divided into three sections:
<br><br>
<!-- <img src="docs/read-me-images/profile-tab-full.png" width="70%"><br><br> -->

1.  _Profile view_ section

- The Profile view section represents how other users perceive one's profile. The menu is only visible to the current user and can be accessed by clicking their profile picture.<br>
  <br>
- This is the profile view the user can see if they click the profile tab<br><br>
  <!-- <img src="docs/read-me-images/view-profile-from-tab.png" width="70%"><br><br> -->
- This is the view when a user clicks another user's profile picture<br><br>
  <!-- <img src="docs/read-me-images/view-profile-modal-different-user.png" width="70%"><br><br> -->

#### Header Navigation section

The Header section contains the settings icon, App name and the search bar<br>
<br>
<!-- <img src="docs/read-me-images/header-nav.png" width="100%"><br><br> -->
<br>

- Settings menu<br><br>
  <!-- <img src="docs/read-me-images/header-menu.png" width="40%"><br><br> -->
- Search bar list<br><br>
  <!-- <img src="docs/read-me-images/search-box.png" width="40%"><br><br> -->


### Future Feature Considerations<hr>

- Another feature would be voice and video calls


## Tools Used

[GitHub](https://github.com/) - used for hosting the source code of the program<br>
[Visual Studio](https://code.visualstudio.com/) - for writing and testing the code<br>
[Balsamiq](https://balsamiq.com/wireframes/) - for creating the wireframes<br>
[Draw.io](http://draw.io/) - used for creating the Flowchart and Database relational schema<br>
[Favicon.io](https://favicon.io/) - used for generating the website favicon<br>
[Font Awesome](https://fontawesome.com/) - for creating atractive UX with icons<br>
[Google Fonts](https://fonts.google.com/) - for typography<br>
[PEP8 Validator](http://pep8online.com/) - used for validating the python code<br>