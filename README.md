# CICD_API_Python_BDD_Automation

## Steps to take this code in your machine

Clone this project using: git clone: git clone https://github.com/sudo-anji-github/CICD_API_Python_BDD_Automation.git

##Prerequisite for this project
Python 2.7 or Python 3.7 in local machine

##Required libraries installation:
Once cloning is done, we need to navigate "CICD_API_Python_BDD_Automation" folder in your local machine, then:

- Perform this command: pip install -r requirements.txt

- Then check the below libraries are installed are not by this command: pip list

    - behave
    - requests
    - allure-behave

##Scenario execution:
###To run the all the scenarios:

- ~/CICD_API_Python_BDD_Automation/features behave cicd_api_validation.feature

###To run the individual scenarios by using tags:
- ~/CICD_API_Python_BDD_Automation/features behave --tags @test1


##Steps to run this code in your Jenkins:
 - Install Jenkins in your local machine:
 - Open the Jenkins: Example- Run this url in your browser: http://localhost:8080/
 - Once the required plugins installation is done, you can separately install the below pluggins:

    - ShingPanda
    - Allure

 - What is ShingPanda plugin?

   This plugin adds Python support to Jenkins with some useful builders (Python builder, virtualenv builder, tox builder…) and the ability to use a Python axis in multi-configuration projects (for testing on multiple versions of Python).

 - What is Allure plugin?

   This plugin allows to automatically generate Allure Report and attach it to build during Jenkins job run.

 - Better to have a JDK 9 version in your Jenkins if you face any issues while generating the Allure Report.

 ###create freestyle project and add enter the below data while configure:
 - Add the git url under source code management by choosing the 'Git' radio button:
   https://github.com/sudo-anji-github/CICD_API_Python_BDD_Automation.git
 - Choose 'Virtualenv Builder' under 'Build' step:

   Select Python version as : System-CPython-2.7

   Check the 'Clear' checkbox, so that it will clear old stuff while building the Job.

   Choose 'Shell' under 'Nature' drop down

   Add this below data in to that 'Shell command prompt'

   - pip install -r requirements.txt

   - behave -f allure_behave.formatter:AllureFormatter -o ./allure-results/ ./features

  - Select 'Allure Report' under 'Post-build Actions'

    And add the 'target/allure-results' in the 'Path' text box

  - Save the Job

 Once the Job is saved, click on the 'Build Now' to run the Job.

 Once the Job is executed successfully, we can find the Allure report by clicking on the  'Allure Report'
