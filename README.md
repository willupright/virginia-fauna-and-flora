# Team27 CS374 Database Project

Project Title: **Virginia Flora & Fauna (Virginia Flora & Fauna (VFFD))**

Team Name: **Ecology Database Team**

Short Name: **EcoDB**

Team Members: **Tenley Kennett, Michael Gerber, Will Upright, Theo Mandelbaum**

# Introduction

Virginia’s ecosystems contain a wide range of flora and fauna, including plants, animals, and insects. Currently, information about species and observations in the state is available but is spread across many different sources. This makes it difficult for researchers, educators, and the public to access up-to-date, and reliable data on Virginia’s biodiversity.

We propose to develop the Virginia Flora & Fauna Database (VFFD). The VFFD is designed to store, manage, and analyze information on Virginia’s plant, animal, and insect species. The system will allow users to access detailed species data such as common and scientific names, habitat, conservation status, regional distribution, and descriptive information. Researchers will be able to submit observations that will include details like location, date, notes, and photos/videos. The submissions can also be reviewed and approved by an administrator to ensure data quality. By centralizing this information, the VFFD will enable users to track species information over time, monitor conservation, and make data driven decisions.

In addition to serving as a research tool, the system will support learning. Through data stored in the VFFD, students, educators, and the general public can explore Virginia’s biodiversity. Additionally, the user will be able to search up different species they want to learn more about, view all species in a specific habitat, or filter species by conservation status, region, etc. Ultimately, the VFFD will provide a single platform that allows for collaboration between researchers, supports learning, and promotes public engagement with Virginia’s natural ecosystems.

If the scope is too small, we can expand the database to include other east coast states' species, or even the rest of the US.

# Primary System Entities

| SYSTEM ENTITY | ATTRIBUTES |
| :---- | :---- |
| Species | Common name, scientific name, category (plant/animal/etc), conservation status, habitat, description, county(s) |
| User | User ID, Name, Role, Email, Observations |
| County | CountyID, State, Name, {Region} |
| Observation | ObservationID, Species Observed, observer ID, county, date, time, notes, media, status |
| Researcher | Observations, researcherID |
| General Public | Personal Observations, publicID |
| Admin | Permission, adminID |

# Primary System Users

| USER GROUP | ACTIVITIES & PERMISSIONS |
| :---- | :---- |
| Admin | Administrator access to the system with the permission to edit any data. Can read/manage species info, conservation status, educational resources, approve/reject content submitted by researchers etc. |
| Researcher | Submit observations, access historical data, read all species info, export datasets, and maybe suggest updates to species info (to the admin) |
| General Public | Can read species info, add personal observations, maybe some educational activities, similar to quizlets quizzes… etc |

The database will hold a centralized collection of all Virginia plant/animal/insect species. The VFFD is designed to serve multiple user groups, each with unique permissions. While this data is likely to be most useful for researchers, our team believes that it's crucial for this data to be widely available. The system is structured encourage collaboration among users through research, education, personal projects, and even conversation. We support and promote the public accessibility of all non personal data regarding biodiversity. The way that the public uses this data is up to them.

# System Functionality

## A search system that allows the user to sort flora and fauna

- Sort by name, habitat, conservation status, regional distribution
- Allow for specific searches with many requirements, or broad searches with few requirements
- Users can select or unselect these requirements by the search bar
- When the search button is clicked for a search including regional distribution, a map will appear with a visualization of the selected or described region.
- Search results will display a list of species with key details such as scientific name, common name, habitat type, and conservation status
- Results will update dynamically when filters are added or removed, making the search process more interactive and user-friendly

## Submission page for researchers

- Researchers will be able to submit observations they make about flora and fauna that they see
- There will be an option for images that researchers take or just descriptive observations

## Species and Observations

* FISH
* AMPHIBIANS
* REPTILES
* BIRDS
* BEES
* DRAGON FLIES
* MAMMALS
* MARINE MAMMALS
* MOLLUSKS
* MILLIPEDES (PARTIAL)
* CENTIPEDES (PARTIAL)
* INSECTS
* ARACHNIDS
* PLANARIANS
* ANNELIDS

* Trees
* Flowers
* Vines
* Grasses
* Aquatic Plants
* Forbs

## Other Features

* Map-based visualization of Virginia counties. Selectable, and allows you to focus on specific areas (could be tough to implement)

# About the Team

**Tenley Kennett** is a junior Computer Science major at James Madison University with a minor in GIS. She has programmed in Java, Python, and C, HTML, CSS. She enjoys front end development and data analysis, and eventually hopes to combine remote sensing/GIS data with computer science in the future. Outside of class she is an brother in Theta Tau (+ active on their volleyball team), and likes baking, arts & crafts, and watching movies.

**Will Upright** - is a senior Computer Science major at James Madison University with experience in application development and a good understanding of computer systems. He also has experience writing code in Java, Javascript, Python, C, HTML, and CSS. He is excited to expand his knowledge of databases through this project. Outside of class he enjoys going to the gym, skiing, and playing golf.

**Michael Gerber** is a Computer Science major with minors in data analytics and computer information systems. Decently skilled in full-stack development through self projects making websites and mobile applications. Looking to bring strong front end development to the project. He is also the Vice-President of Madison Motorsports and interns as a student-employee at Madison Automotive Apprentices using skills from Computer Science, Data Analytics and Engineering.

**Theo Mandelbaum** - Senior Computer Science major at James Madison University with minors in math and data analytics. Experienced in Python, JavaScript, C and Java. Has experience in full-stack web development using Django and React as frameworks. After graduation, he hopes to go straight into the workforce as a part of a data science team. Outside of academics, he likes music, sports and cooking.
