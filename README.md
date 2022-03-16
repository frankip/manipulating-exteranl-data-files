# manipulating-exteranl-data-files
A short application that can perform CRUD functionalities on external data files

it fetches data from a sql file creates the table and populate the table
then fetch and display using flask



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* python 
  ```sh
  - python 3 
  - pip
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/frankip/manipulating-exteranl-data-files
   ```
2. create a virtual environment and activate it
   ```sh
   python3 -m venv venv

   and activate

   source venv/bin/activate
   ```
3. install project dependencies
   ```py
   pip install -r requirements.txt
   ```
4. export flask to environment
   ```py
   export FLASK_APP=main.py
   ```

5. Load sql databse
   ```py
   python3 init_db.py
   ```
6. start the project
   ```py
   flask run
   ```


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage


<!-- USAGE EXAMPLES -->
## Usage


|  paths 	            |   views	                    |
|-----------------------|-------------------------------|
|   `/` 	            | view all users   	  |
|   `add/`              | create new user     |
|   `update/<id>/`	    | update new user  	        |
|   `delete/<id>/`      | delete a single leave request |

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Your Name - [@frankip](https://github.com/frankip/) -

Project Link: [https://github.com/frankip/manipulating-exteranl-data-files](https://github.com/frankip/manipulating-exteranl-data-files)

<p align="right">(<a href="#top">back to top</a>)</p>

