# Browser Stack + Selenium

- [Browser Stack + Selenium](#browser-stack--selenium)
  - [GET STARTED](#get-started)
    - [Set up the dependencies](#set-up-the-dependencies)
    - [Configure browserstack.yml config file](#configure-browserstackyml-config-file)
    - [Run your test suite](#run-your-test-suite)
      - [Mark session name](#mark-session-name)
      - [Mark test as passed or failed](#mark-test-as-passed-or-failed)
  - [Code Modules](#code-modules)

## GET STARTED

### Set up the dependencies

Run the following command on your terminal/command-prompt to install the required dependencies.

macOS or Linux

```bash
# create virtual environment
python3 -m venv env
source env/bin/activate
# install the required packages
pip3 install -r requirements.txt
```

Windows

```bash
python3 -m venv env
env\Scripts\activate
pip3 install -r requirements.txt
```

### Configure browserstack.yml config file

bulid browserstack.yml like this

```yaml
userName: "yourname"
accessKey: "api_key"
platforms:
  - os: Windows
    osVersion: 11
    browserName: Chrome
    browserVersion: 103.0
  - os: Windows
    osVersion: 10
    browserName: Chrome
    browserVersion: latest
  - os: OS X
    osVersion: Ventura
    browserName: Edge
    browserVersion: latest-beta
browserstackLocal: true
buildName: browserstack-build-1
projectName: BrowserStack Sample
```

The `browserstack.yml` file holds all the required capabilities to run your tests on BrowserStack

### Run your test suite

#### Mark session name

test-script.py

```python
executor_object = {
    'action': 'setSessionName',
    'arguments': {
        'name': "<test-name>"
    }
}
browserstack_executor = 'browserstack_executor: {}'.format(json.dumps(executor_object))
driver.execute_script(browserstack_executor)
```

You can use the **sessionName** capability to give your session a name (usually describing the test case) so that it is easy for you to debug later.

#### Mark test as passed or failed

testest-script.py

[Copy snippet](https://www.browserstack.com/docs/onboarding/python-sdk/integrate-your-test-suite?timestamp=1697528932290)

```python
executor_object = {
    'action': 'setSessionStatus',
    'arguments': {
        'status': "<passed/failed>",
        'reason': "<reason>"
    }
}
browserstack_executor = 'browserstack_executor: {}'.format(json.dumps(executor_object))
driver.execute_script(browserstack_executor)
```

To mark whether your test has passed or failed on BrowserStack, use the following Javascript executor in your test script.

The arguments passed in the Javascript method for setting the status and the corresponding reason of the test are `status` and `reason`

- `status` accepts either `passed` or `failed` as the value
- `reason` accepts a value in string datatype

Use this command to test

```bash
browserstack-sdk python <path-to-test-files>
```

## Code Modules
