<h1> Simple Python and Selenium PageObject example </h1>

<img align="center" src="https://github.com/betaraybill/PythonAppiumExamplePO/blob/media/selenpy.png?raw=true" alt="Selenium + Python">

## Description

* Fairly simple PageObject pattern. Include
  - PyTest
  - Allure reports
  - Logging
* Easy to maintain, no unnecessary 3-rd party packages/wrappers
* Just clone it and put your url/locators/logic
  


## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com), [Pipenv](https://github.com/pypa/pipenv), Chromedriver/Geckodriver in path
```bash
# Clone this repository
$ git clone https://github.com/betaraybill/PythonSeleniumExamplePO.git

# Go into the repository
$ cd PythonSeleniumExamplePO

# Install dependencies
$ pipenv install

# You can switch between Chrome/Firefox by adding --browser= key for example --browser=firefox or --browser=chrome
# It is also possible for the Chrome to run in headless mode use --headless=1 key (turned off by default)

# Tu run dummy google.com tests 
$ pipenv run py.test tests/test_test.py --browser=chrome

# If you want to have allure report and logs
$ pipenv run py.test --log-cli-level=INFO -s --alluredir=/path/to/desired/alluredir tests/test_test.py --browser=chrome

# To get allure report
$ allure generate --clean allure/ -o allure/reports && allure open allure/reports

# To run tests with reruns
$ pipenv run py.test --log-cli-level=INFO -s -reruns=3 --browser=chrome test_test.py

# If for some reason you don't like Allure, you can use Pytest built-in reports, to do this - add --html=report.html
pipenv run py.test --log-cli-level=INFO -s --html=report.html --browser=chrome test_test.py

```


## Contact me

Feel free to make any pull-request if you have something to add or change.
Also, you can contact me by email: raijinthegodofthunder@gmail.com, in case if you have something to ask or tell me.

