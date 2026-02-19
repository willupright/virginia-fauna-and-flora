# GP2 Feedback

## Project title

- 27, Virginia Flora & Fauna (Virginia Flora & Fauna (VFFD))
- Team 27
Virginia Flora & Fauna
- Team 27 - Virginia Flora & Fauna (Virginia Flora & Fauna (VFFD))
- Team 27 - Virginia Flora & Fauna (Virginia Flora & Fauna (VFFD))
- Team 27
Virginia Flora & Fauna (Virginia Flora & Fauna (VFFD))
- Team 27: Virginia Flora & Fauna (Virginia Flora & Fauna (VFFD))
- Team 27: Virginia Flora & Fauna

## Consistency

- The entities described in the README.md file is entirely reflected in the EER diagram. Each entity described has a corresponding entity on the diagram. The attributes described each have a corresponding attribute in the correct entity on the diagram. Although not reflected in the README.md, relationships have been drawn to signify how these entities are connected. The README.md focuses more on the end-user experience of the product rather than these details.
- All the entities they said were going to be there are on the diagram with all the attributes that they were going to have. Their system functionality section also aligns with what the diagram is showing.
- The diagram is consistent with the readme. All of the entities are marked and make sense in the diagram, along with their corresponding connections.
- The EER diagram is very consistent with the project description from the read me. There is nothing missing that I see.
- To me, the diagram looks well structured, and replicates the relationships between each table properly, like how a country can hold 0 or many observations, and a species can have 0 or many observations.
- The only problem I see is each distinct user has their own ID. I don't think they need their own ID if User ID is present for all of them. The permissions for each should be enough to specify their role.
- The observation table probably doesn't need the observer ID if it can look at the User ID
- The README and the EER diagram are consistent with each other. Both documents describe the same entities and concepts, for example, the species entity included the attributes like common name, scientific name, habitat, conservation status and county in both documents. they also added that a User can be either a Researcher, Admin or just the General Public which was also outlined in their README documentation.
- The README.md and ERD line up quite well, particularly for the primary system users where each kind of user they described is derived from a common "User" entity. Additionally, every entity described appears in the ERD.

## Completeness

- I believe that the "observations" attributes in the user entity (and its subclasses) is unnecessary as it is encoded by their relationship. This could maybe suffice as a multivalued attribute, but it's also derived so it'd probably be best to leave this off. Relationships are using crow's foot notation correctly to the best of my understanding. Every entity has a primary key aside from those which are "subclasses," which is fine. Attributes are appropriate and reflect the purpose of the product, to my understanding. Entities and relationships are named well and reflect their usages (e.g., a user "makes" observations).
- I think the diagram is complete. Each entity has a relationship with another entity and all the attributes from the proposal are in each entity. I also don't see anything in the proposal that was left out of the diagram. The only thing I see is that in the proposal it talks about how the general public can make personal observations. Not sure if these are different than the normal observations in some way, but if they are different then maybe add a new entity for this.
- The diagram has all of the primary keys marked, the entities are named clearly, and crow's foot is shown. The only thing is that the diagram doesn't include how the admin would approve of a submission.
- I would recommend that Common name within the Species entity should be ((Common name)) since for many plant species there are several unofficial names. Other than that there is nothing missing.
- The observation table may need attributes moved to their own table or relationship, like the media attribute. Is it a video, photograph, some other kind of data?
- Their EER diagram appears complete, it has entities, attributes and relationships that obviously thought out. Along with this each entity has a clear name and identifier that allows the viewers to understand what each entity and relationship is doing. Another thing that stood out to me was the fact that the attributes for the Species entity did not only included the name of the species but also they differentiated between the common name and the scientific name as well as conservation status, description, habitat and category. This information provides all of the important factors one would need to obtain meaningful biodiversity data.
- All entities have clearly well defined attributes that reflect about every desired data point from the README and each relationship has accurate crow's foot notation.

## Correctness

- Some of the attributes (i.e., the "observations" attributes in the user entity and its subclasses) duplicate the semantics of relationships that already exist. Like also mentioned previously, I have trouble seeing how the region attribute will be derived. I once again suggest an entity like a continent or a country to encapsulate this information.
- One thing I noticed was that they said researchers are the only ones that can make observations, but it looks like all of the user attributes are going to the user which has a relationship makes with observation. Maybe switch the user entity with the other user entities and then have the makes relationship come out of the researcher entity.
- Overall, the diagram looks complete, the entities are all connected. I feel like the user id and the admin/researcher/public id's should be one thing to avoid duplicates. I'm not sure if there should be a county attribute inside of species as county is already its own entity, and could just have a 1 to many connection.
- All relationships I can see are logically correct. The connection between User and types of users was executed perfectly.
- I'm not sure if species needs the exists relationship between it and county if an observation already holds a county
- From what I can see the EER diagram correctly aligns with the README documentation. They have all of the correct data and information that they had listed along with the relationships they talked about in their README. One of the only things that stuck out to me as somewhat problematic (and my understanding may be wrong) is the fact that it says in a county their can only exist one species based on the crows foot relationship between county and species entities.
- There don't appear to be any obvious technical errors. The only thing not immediately clear is if the additional IDs for the Researcher, General Public, and Admin are supposed to override the User ID from the User entity or if they are additional unique attributes.

## Organization

- The county entity implies that its region will derived from somewhere. It's not very clear where this derivation exists (e.g., there isn't a relationship the county has with a country, continent, or other land mass).
All entities and relationships are documented in a readable and elegant manner, but there are slight inconsistencies in the casing and spacing of attribute names. Sometimes the diagram opts to use camel case but also uses normal English casing and spacing. The layout and organization of the diagram makes for an easy read. Relationship lines do not overlap to create ambiguities in the connections.
The diagram does not span page boundaries, so there are no issues that could arise from that.
Entity and relationship names are understandable. For instance, I can identify what an "observation" is from a high-level fairly easily.
- The layout of the diagram is easy to follow and understand what each entity is supposed to do. All the names of the relationships and entities all make sense when reading them using crows foot notation.
- The diagram is well organized and is easy to follow. The entities and relationships are labeled and understandable.
- The only recommendation that I would make is that it might be a little more readable if species was to the right of observation so that the relationship between county a and species wasn't so far away but I think this is a worthy trade off for it being one page instead of two. Also I don't really understand why the relationship between county and observation is "Holds", this could make much more sense if it was explained to me.
- Overall the diagram looks very clean, and there are only a few tiny issues that don't drastically effect how the system works. If you change some of the attributes, or clear up why you have some duplicate attributes in some tables, then I think you will be all good to go.
- The diagram is well structured and easy to follow, the entities and relationships are put together in a way that a user is able to easily understand the flow of the system. The names of the attributes, entities and relationships are very straightforward, easily explaining the relationships between each entity and how they relate to one another. I believe that the organization of their diagram is extremely readable, structured well, and effectively communicates the team's intended design.
- The diagram is simple, clean, and all fits on a single page. Every entity described in the README is present and have logical relationships between each other.
