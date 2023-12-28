<br/>
<p align="center">
  <h3 align="center">SnappFood Task</h3>
  <p align="center">
    a project for orders delay report system
    <br/>
  </p>
</p>

## Table Of Contents

- [Table Of Contents](#table-of-contents)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Authors](#authors)

## Built With

I Developed this project with these technologies:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [DRF](https://www.django-rest-framework.org/)

## Getting Started

To get a local copy up and running follow these steps.

### Installation

1. Clone the repo

```sh
git clone https://github.com/mojtabasohrabi/snappfood.git
```

2. install Docker on your OS


3. go to project root and run project with docker by this command:

```sh
Docker-compose up --build
```

> [!WARNING]
> if your OS is Windows, you should change files line separator to LF to work docker correctly.  


4. now project ups in `localhost:8000`


5. APIs are documented with swagger. to see and test them, go to `localhost:8000/api/schema/swagger`


### Usage

1. first you should create some vendors by this api: `localhost:8000/vendor/create/`


2. and some agents by this api: `localhost:8000/agent/create/`


3. and some orders by this api: `localhost:8000/orders/order/`


4. now you can test the scenarios. to create trip for order use this api: `localhost:8000/orders/ready/`


5. to report delay for order use this api: `localhost:8000/orders/delay-report/`


6. to assign a report to agents use this api: `localhost:8000/agent/check-delay-report/`


7. to get report of sum delays of each vendor in this week use this api: `localhost:8000/vendor/sum-weekly-delay/`


## Author

- **Mojtaba Sohrabi** - _Software Engineer_ - [Linkedin](https://www.linkedin.com/in/mojtabasohrabi1/) - _All Work_
