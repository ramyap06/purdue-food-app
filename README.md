# purdue-food-helper

## Objective
Web application that help Purdue students reach their nutrition goals with dining hall food.
- Show basic nutritional data for each food
- Fit dietary needs such as being vegetarian/gluten free
- Track how much much of each macro and micro you have
- Compare it to goals
- Categorize food both by macro/micro in each dining hall
- Sort macro/micro by most to least

Basically Purdue Menus + Goal-Oriented help

## Basic Design
- frontend
    - single-page app (HTML + JS).
    - show menu of one dining hall.
    - display macros (protein, carbs, fat) in sorted order.
    - button to “Add to Today’s Intake.”
    - show running totals vs. your personal hardcoded goals.
    - store progress locally (browser memory or localStorage).
- backend
    - (optional in MVP)
    - tiny API to serve the menu JSON (Flask/FastAPI).
    - endpoint to fetch today’s dining hall menu.
- database
    - start with static JSON file containing menu + macros.
    - example food entries:
        - { "name": "Grilled Chicken", "protein": 25, "carbs": 0, "fat": 5 }.
    - hardcode your daily macro goals in code.