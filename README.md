# Box Selector — Shipping Box Recommendation System

A Django-based system that recommends the most suitable shipping box for an order based on product dimensions and weight.

## How it works
1. Each **Product** has length, width, height, and weight.
2. Each **Box** has length, width, height, max_weight, and cost.
3. The system checks which boxes can fit the product (dimensions + weight).
4. Among the boxes that fit, it selects the one with the **lowest cost**.

## Tech Stack
- Python
- Django

## Setup Instructions

1. Clone the repo: # Box Selector — Shipping Box Recommendation System

A Django-based system that recommends the most suitable shipping box for an order based on product dimensions and weight.

## How it works
1. Each **Product** has length, width, height, and weight.
2. Each **Box** has length, width, height, max_weight, and cost.
3. The system checks which boxes can fit the product (dimensions + weight).
4. Among the boxes that fit, it selects the one with the **lowest cost**.

## Tech Stack
- Python
- Django

## Setup Instructions

1. Clone the repo:# Box Selector — Shipping Box Recommendation System

A Django-based system that recommends the most suitable shipping box for an order based on product dimensions and weight.

## How it works
1. Each **Product** has length, width, height, and weight.
2. Each **Box** has length, width, height, max_weight, and cost.
3. The system checks which boxes can fit the product (dimensions + weight).
4. Among the boxes that fit, it selects the one with the **lowest cost**.

## Tech Stack
- Python
- Django

## Setup Instructions

1. Clone the repo:# Box Selector — Shipping Box Recommendation System

A Django-based system that recommends the most suitable shipping box for an order based on product dimensions and weight.

## How it works
1. Each **Product** has length, width, height, and weight.
2. Each **Box** has length, width, height, max_weight, and cost.
3. The system checks which boxes can fit the product (dimensions + weight).
4. Among the boxes that fit, it selects the one with the **lowest cost**.

## Tech Stack
- Python
- Django

## Setup Instructions

1. Clone the repo: git clone <https://github.com/sayyed-mohd-soheb/django-shipping>  ##ctrl + click

cd box_selector

2. Create and activate virtual environment:
 python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies: pip install -r requirements.txt

4. Run migrations: python manage.py migrate 

5. (Optional) Create a superuser to add Box/Product data via admin: python manage.py createsuperuser

6. Run the server:python manage.py runserver

Open `http://127.0.0.1:8000/` and enter product dimensions to get the recommended box.
## Running Tests

box_selector/

├── core/

│   ├── models.py      # Product and Box models

│   ├── utils.py        # find_best_box() — selection logic

│   ├── views.py        # form view

│   └── tests.py         # test cases

├── templates/index.html

├── static/style.css

└── manage.py

