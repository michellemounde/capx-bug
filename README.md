# Capacity Exchange (CapX) - Bug

The Capacity Exchange (CapX) is a project developing a sociotechnical platform for peer-to-peer connection and knowledge sharing towards sustainable, community-based capacity-building within the Wikimedia Movement. It intends to deliver an interactive, online platform, backed by a database, which will allow wikimedians to: publish information about themselves, their affiliates, and informal groups; conduct searches and access information published by others; connect with peers for knowledge exchange. The platform is intended to be responsive, intuitive, and accessible to all wikimedia users.

## Description

This is an application project for the Wikimedia Capacity Exchange (CapX) project through Outreachy.

The project is part of migrating the Capacity Exchang pilot software from Java to Python using the Django framework.

## Table of Contents (Optional)

If your README is long, add a table of contents to make it easy for users to find what they need.

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)
- [Technologies](#technologies)
- [Features & Implementation](#features--implementation)
- [Feedback](#feedback)
- [How to Contribute](#how-to-contribute)
- [Tests](#tests)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3
- Django 4.2.5


## Installation

1. Clone the repository:
```bash
git clone https://github.com/michellemounde/capx-bug.git
```

2. Navigate to the project directory:
```bash
cd capx-bug
```

3. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```

4. Activate the virtual environment:
* On Windows:
```bash
venv\Scripts\activate
```
* On macOS and Linux:
```bash
source venv/bin/activate
```

5. Install project dependencies:
```bash
pip install -r requirements.txt
```

6. Create the database and apply migrations:
```bash
python manage.py migrate
```

7. Create a superuser to have full control over the database:
```bash
python manage.py createsuperuser
```

9. Start the development server:
```bash
python manage.py runserver
```

You should now be able to access the project at http://localhost:8000/ in your web browser.

## Usage

1. Go to http://localhost:8000/bug/
2. Follow the provided links to access different pages
3. On the register links page, you can register a bug with a current, past or future date
4. On the bugs list page you can view all current and past bugs in descending order of report date
5. You can click on a specifi bug to open its detail view page
6. On a bug detail page you can view the bug's id, description, bug_type, status and report date

## Acknowledgements

Credits:

	Project:
		Wikimedia

	Project Access:
		Outreachy(https://www.outreachy.org/)

## Technologies
- Python
- Django
- HTML

## Features & Implementation

1. A bug index page with a welcome page and navigation menu.
2. A bug registration page with desription, bug_type, status and report_date fields.
3. A bugs list page showing current and past bugs in descending order

## Feedback
Feel free to send me feedback by filing an issue. Feature requests are always welcome.

## How to Contribute

Contributions are welcome! To contribute to Capacity Exchange (CapX) - Bug, follow these steps:

1. Fork the repository
2. Create a new branch: git checkout -b feature/your-feature
3. Make your changes and commit them: git commit -m 'Add some feature'
4. Push to the branch: git push origin feature/your-feature
5. Create a pull request on GitHub

## Tests

Run tests with the following command:
```bash
python manage.py test bug
```
