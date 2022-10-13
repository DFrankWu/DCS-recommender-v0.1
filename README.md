# DCS World Campaign Recommender v0.1 
- Donghang Wu ©2022

### Project Goals
The goal of this project is to help DCS users to browse the ever growing campaign DLC list and recommend 
appropriate campaigns for their next purchase.

The initial version of the recommender will be based on a NLP implementation using solely the product info provided on 
DCS WORLD website (just like how a user receives info), with collaborative filtering added later when data becomes available.

This project will first extract product info from [DCS-WORLD.com](https://www.digitalcombatsimulator.com) and
save as csv file form, ready for general analysis and other product usage.

To use the data on `dcs_recommender`, one first need to clean unnecessary text parts and concatenate text to form 'tags' column, a **clean** csv with proper tags aggregated is needed for `dcs_recommender` to process.
 

Here are a few questions that this project has sought to answer:
- Can the recommender accurately recommend topic related/author related campaign (content based)?
- How are those results compared to a *veteran player recommendation*?
- How can the recommender take in other domain knowledges that *veteran players* are aware of (such as gameplay quality, type of missions within, mission length, etc.) ?
- Will `dcs_recommender` perform better than the current *popular* recommendation presented on DCS website in sales?

### Data sources

The base product info was provided by [DCS-WORLD.com](https://www.digitalcombatsimulator.com).

*future purchase related data may be added from Eagle Dynamics*
