# TherapieLand test
 1. [Test cases](#test-scenarios)
 2. [Project structure](#project-structure)
 3. [Running tests](#running-tests)
 3. [Noticed bugs and suggestions](#noticed-bugs-on-page-and-suggestions)


# Test scenarios
I chose Smiley Monitor type to write a few parameterized scenarios for tests

<a name="cases"></a>
### Test Case 1:

[test_user_can_create_new_smiley_monitor_from_clean_state](https://github.com/KingaNeri/TherapieLandTest/blob/dfaf80b1de7b1002b7417ac22193bb7514d0f020/test/tests.py#L45)

GIVEN user is logged in to TherapieLand and Monitors page is clean and opened

WHEN user can use add button and follow default steps to create Smiley monitor

OR user can use Smiley monitor panel prompt and follow default steps to create Smiley monitor

THEN user can see created Smiley Monitor containing chart, details panel, emotion panel and date filter


### Test Case 2:
[test_user_can_name_smiley_monitor_when_creating](https://github.com/KingaNeri/TherapieLandTest/blob/dfaf80b1de7b1002b7417ac22193bb7514d0f020/test/tests.py#L56)

GIVEN user is logged in to TherapieLand and Monitors page is clean and opened

WHEN user can create Smiley monitor and name it in creation popup using simple string

OR using string containing numbers

OR using string containing special characters

THEN Smiley monitor is created with name properly displayed

### Test Case 3:
[test_user_can_choose_high_or_low_record_when_creating_smiley_monitor](https://github.com/KingaNeri/TherapieLandTest/blob/dfaf80b1de7b1002b7417ac22193bb7514d0f020/test/tests.py#L64)

GIVEN user is logged in to TherapieLand and Monitors page is clean and opened

WHEN user is creating new Smiley monitor

THEN user can choose high record and create monitor

OR user can choose low record and create monitor

### Test Case 4:
[test_user_can_see_starting_date_of_monitor](https://github.com/KingaNeri/TherapieLandTest/blob/dfaf80b1de7b1002b7417ac22193bb7514d0f020/test/tests.py#L68)

GIVEN user is logged in to TherapieLand and Monitors page is clean and opened

WHEN user created new Smiley monitor and has it displayed

THEN user can see starting date of monitor displaying current date

### Test Case 5:
[test_user_can_add_new_emotions_entries](https://github.com/KingaNeri/TherapieLandTest/blob/dfaf80b1de7b1002b7417ac22193bb7514d0f020/test/tests.py#L74)

GIVEN user is logged in to TherapieLand and created Smiley monitor

WHEN user adds emotions entires with all available emotions each for last 4 days

THEN user can see graph with added emotion entries in the current week panel

# Running tests
1. Install reqirements
`pip install -r requirements.txt`
2. Run all tests from main directory
`pytest test/tests.py`

# Project structure
1. [config.py](config/config.py) - separate configuration for easier editing
2. [basic_element.py](pages/components/basic_element.py) - basic element structure - separate so that waiting for element or common methods for all elements can be added here
3. [monitors_page_locators.py](pages/monitors/monitors_page_locators.py), [dashboard_page_locators.py](pages/dashboard/dashboard_page_locators.py), [login_page_locators.py](pages/login/login_page_locators.py) - elements locators by page
4. [monitors_page.py](pages/monitors/monitors_page.py), [dashboard_page.py](pages/dashboard/dashboard_page.py), [login_page.py](pages/login/login_page.py) - binding locators as class properties
5. [monitors_page_actions.py](pages/monitors/monitors_page_actions.py), [dashboard_page_actions.py](pages/dashboard/dashboard_page_actions.py), [login_page_actions.py](pages/login/login_page_actions.py) - methods that perform actions on pages
6. [tests.py](test/tests.py) - test cases and fixtures

# Noticed bugs on page and suggestions
Small remarks noticed when writing automation
1. User can choose date from calendar in the future and add emotion entry in the future (bug)
2. After creating new smiley monitor from empty page (no monitors) user by default has graph of week forward not current one (bug)
3. When choosing hour it would be nice to have like for date also input option (suggestion)
4. There could be Neutral emotion in between :) (suggestion)
