# Energy usage calculations

Application calculates bill based on tariff and received JSON data payload,
containing electricity usage - stored in `data` folder: `readings.json`.

## Setup

Python3.8 installation instructions: https://docs.python.org/3/using/index.html

Ensure `Python3.8` is available on the system and that you are in the directory
of the project, where `Pipfile` is.

    sudo pip install pipenv
    pipenv install

For development use:

    pipenv install --dev

## Running

Default

    pipenv run python main.py

Application is able to accept arguments:

    --member_id
    --account_id
    --bill_date
    --energy_source

E.g.:

     pipenv run python main.py \
     --member_id member-123 \
     --account_id account-abc \
     --bill_date 2020-08-21 \
     --energy_source electricity

## Testing

    pipenv run pytest
    
Examples of running specific tests:

    pipenv run pytest tests/test_bill_member.py
    pipenv run pytest tests/test_bill_member.py::TestBillMember::test_calculate_bill_for_august_2017

## CircleCI

Project is able to use Continuous Integration via CircleCI.
Please check configuration in `.circleci/config.yml`.

## Included in the implementation:

1. A small program which, given a set of meter readings, computes a member’s monthly energy bill.
2. Tests.
