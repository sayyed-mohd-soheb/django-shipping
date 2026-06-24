# AI Usage Documentation

## 1. AI Tool Used
- Claude (claude.ai)

## 2. Prompts Given
- Asked to guide step-by-step to build a Django box recommendation system
- Asked to help write test cases for find_best_box() logic
- Asked to fix CSS layout (heading center, form below)
- Asked to create README.md structure

## 3. What I Accepted
- Project structure and setup commands
- Model structure (Product and Box fields)
- Test case structure in tests.py
- README.md template

## 4. What I Rejected / Modified
- Modified CSS layout based on my own HTML structure
- Adjusted test data values to match my actual box sizes

## 5. Mistakes AI Made
- AI suggested fixtures approach for sample data, but I chose simpler solution (keep db.sqlite3 in repo)

## 6. How I Verified
- Ran all 3 tests: python manage.py test core → all passed (OK)
- Manually tested form in browser with different product sizes
- Confirmed cheapest fitting box is returned correctly