<a name="readme-top"></a>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/itsmejayd/filter-duplicate-lines">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Duplicate Line Remover</h3>

  <p align="center">
    A Python tool with a Flask web interface designed to remove duplicate entries from line break delimited lists while maintaining the relative position of blank lines in the input text. Originally created to clean up OneTab exports (maintaining tab groups), it can be used for any text list with similar requirements.
    <br />
    <a href="https://github.com/itsmejayd/filter-duplicate-lines"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!--
    <a href="https://github.com/itsmejayd/filter-duplicate-lines">View Demo</a>
    -->
    ·
    <a href="https://github.com/itsmejayd/filter-duplicate-lines/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/itsmejayd/filter-duplicate-lines/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/itsmejayd/filter-duplicate-lines)



### Built With


* [![Python][Python.org]][Python-url]
* [![Flask][flask.palletsprojects.com]][Flask-url]



<!-- GETTING STARTED -->
## Getting Started

This guide provides instructions on setting up and using the "Duplicate Line Remover" tool locally.

### Prerequisites

To run this project, you'll need:
- Python (version 3.11.0 recommended)
- Flask (for the web application)

Note: I've added `.python-version` to `.gitignore` to ensure compatibility across different Python versions. For reference, the version used during development was 3.11.0.

You may want to set up a virtual environment (venv) to manage dependencies, for exmaple:
```sh
python -m venv env
```
```sh
source env/bin/activate
```

Install Flask:
```sh
pip install flask
```

### Installation

   Clone the repo:
   ```sh
   git clone https://github.com/itsmejayd/filter-duplicate-lines.git
   ```
   ```sh
   cd filter-duplicate-lines
   ```


<!-- USAGE EXAMPLES -->
## Usage

1. Removing Duplicate Lines:
  - Use `remove_duplicates(input_file, output_file)` function from `filter_duplicate_lines.py` to process your input file and generate a cleaned output file without duplicate lines.

  Example usage:
  ```python
  from filter_duplicate_lines import remove_duplicates

  input_file = "your_input_file_name.txt"
  output_file = "cleaned_output.txt"

  remove_duplicates(input_file, output_file)
  ```

2. Using the Web Application:

  - Start the Flask application by running python app.py in your terminal.
  - Access the application in your web browser at http://localhost:5000.
  - Upload a text file or paste text into the text box, then click download button to remove duplicates and download the cleaned file.




<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See the [open issues](https://github.com/itsmejayd/filter-duplicate-lines/issues) for a full list of proposed features (and known issues).



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Joseph Dwyer - josephdwyer20@gmail.com - [Twitter](https://twitter.com/jdlately)



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [OneTab](https://www.one-tab.com/) Browser Extension: A wonderful tool I love, inspired me to make my tool specifically to increase OneTab's functionality and to share it for others to use.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/itsmejayd/filter-duplicate-lines.svg?style=for-the-badge
[forks-url]: https://github.com/itsmejayd/filter-duplicate-lines/network/members
[stars-shield]: https://img.shields.io/github/stars/itsmejayd/filter-duplicate-lines.svg?style=for-the-badge
[stars-url]: https://github.com/itsmejayd/filter-duplicate-lines/stargazers
[issues-shield]: https://img.shields.io/github/issues/itsmejayd/filter-duplicate-lines.svg?style=for-the-badge
[issues-url]: https://github.com/itsmejayd/filter-duplicate-lines/issues
[license-shield]: https://img.shields.io/github/license/itsmejayd/filter-duplicate-lines.svg?style=for-the-badge
[license-url]: https://github.com/itsmejayd/filter-duplicate-lines/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/josephdwyer20
[product-screenshot]: images/flask_web_app.png
[Python.org]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org/
[Flask.palletsprojects.com]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
