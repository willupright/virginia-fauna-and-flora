# GP5 Feedback

## Project title

- 27  Ecology Database Team
- Team 27 Virginia Flora & Fauna
- Team 27, Virginia Flora & Fauna (Virginia Flora & Fauna (VFFD)
- Team 27: Virginia Flora & Fauna (Virginia Flora & Fauna (VFFD)
- 27, Virginia Flora & Fauna
- Team 27, Virginia Flora & Fauna
- team27, Virginia Flora & Fauna
- Team: 27, Project Name: Virginia Flora & Fauna (Virginia Flora & Fauna (VFFD))

## Action(s)

- I really like the observation idea and I think its implemented well
- The action that was included was to like an observation. All of the naming conventions were sound. Based on the code I couldn't tell if the amount of likes that an observation had received was displayed, if not, I think that would be an improvement.
- Their code looks pretty good, but there are some things that I noticed. They should add some error handling with validating the url parameters.
- The like observation acts as intended, but I don't think it makes sense in the context of the app. The proposal describes this app as a tool for use in research and education, while having a like system is something I'd expect on a social media platform.
- Their like action performs without error, though I do not remember if their was some sort of visual indicator next to the observations that were liked.
- Yes, all their actions perform their tasks correctly. Maybe there could be a way to add comments easier, or make it more noticeable? It seems like the user needs to tab through a few menus to get there.
- The action that lets users “like” observations seems to work well. This is a great way for users to interact with the application. I can't think of any improvements for this feature; the naming seems clear.
- all their actions seem functional. It's hard to say how they could improve them because the scope of this project might not include advanced actions. right now thier actions (and ours) are somewhat fake...they dont actually do anything. The only improvement I could see making that is in the scope of this project is maybe add some more for each table.

## Chart(s)

- I like the charts and I think they're well managed
- The 2 charts I saw were species by habitat and species by category. This is helpful information on how the type of ecosystem favors different species of plants. During the demonstration the y-axis did not start at 0, I'm assuming because of the amount of data that the database held. For readability I would see if there is a way to have the y-axis for the aggregation start at 0.
- Yes the charts are functional and relevant. Very easy to visualize and makes a lot of sense for their project. Species_By_Category and Species_By_Habitat are pretty simple and easy to understand charts for this project.
- The two charts currently present, species by category and species by habitat, both fit really well with the project topic. With the project's focus on research and education, adding more charts, such as species observations over time, can only be beneficial.
- Yes, the charts are functional, accurate, and relevant to the project's goals. The charts helped visualize the number of species grouped by category and habitat.
- The chart views work as intended. Maybe you could add one for comments or observations over time too to synthesize the different parts of your project
- I think the charts do a good job of showing relevant information. As a user, I would be interested in viewing more charts. Maybe a chart providing information about the invasive species.
- right now there are two similar charts in their project....and they are absolutely beautiful! So good, that I want to steal their idea :). I will say it would be nice to see more charts, maybe in different styles to add some variation.

## Form(s)

- The forms are good
- There were 2 forms in this application. One was for making an observation and one was for leaving a comment on an observation. Having a form for the observation is necessary since that is what most of the application is centered around. I also like having the comment form to create more interactions between users and intertwines nicely with the ability to like an observation. It transforms the application into almost a social media app instead of just being a data displaying application.
- There is no validation that the datetime implemented isn't in the future. Most everything else looks pretty good, the inserts should succeed.
- The forms act as expected and contribute well to the app's functionality.
- Yes, their form validates input properly and updates the database (demoed in class). From what I can see, their form is perfectly fine as is.
- The forms work as intended, I particularly liked the observations one. Will that be accessible to all users or just admins?
- Your form looks excellent. Allowing users to create their own observations is a great way for users to interact with the website. I don't see any need for improvement here.
- the forms work correctly and there is some good validation like required input and a max length for the comments section. It might be good to add a max/min lengths to the other fields as well. they update the corresponding table safely!

## Code Quality

- I like how theyre moved into different files. Im not sure if I can find any code to be refactored
- All directories, files, functions, variables, and classes are aptly named. The directories were also easy to navigate. The different app views were separated by commented lines in the menu file which helped the readability. I would remove the commented out @expose (I'm assuming is an action) if is not going to be used for the species views or move it to an archived folder.
- I was lost a little bit at the beginning because we don't have a views folder and our models is simply models.py so it took me a second to find the files I was looking for, but for the most part it makes sense. The function names and classes are clearly named and consistent. I think their charts are pretty good code, simple and straight to the point.
- Well organized code, pgsql is outside of database but that doesn't change much for me. In pgsql/generate.py make_media, I don't understand why the media_id is i + 1 instead of just having i start at one and extending the end of you loop by 1.
- Yes, all their files and directories are organized well and easy to navigate. Their functions, variables, and classes are all named clearly as well. For their forms, I believe combining them into one view with both definitions could simplify their code (because both are Species_By_SOMETHING). One additional small nitpick is running a formatter on their files to make reading/working on the remainder of their project easier.
- I like that you separated models and views into different python files. If possible, try to get green branding on the other webpages besides your home page.
- The dropdown menu names should eventually be updated, aside from charts. Adding public roles in addition to the admin roles will let users without admin permissions access features of the site. I really like how you added a way for users to comment.
- The overall all code is as understandable as can be, it is a project that requires many folders/files so a certain amount of jumping around is necessary but it looks very similar in structure to the profs repository
