from ftw import logchecker, testrunner
import pytest
import random


class LoggerTestObj(logchecker.LogChecker):
    def __init__(self):
        self.do_nothing = False

    def generate_random_logs(self):
        if self.do_nothing:
            return []
        else:
            return [(f'{str(self.start)} rule-id-' + str(random.randint(10, 99)))]

    def get_logs(self):
        return self.generate_random_logs()


@pytest.fixture
def logchecker_obj():
    """
    Returns a LoggerTest Integration object
    """
    return LoggerTestObj()


def test_logcontains_withlog(logchecker_obj, ruleset, test):
    runner = testrunner.TestRunner()
    for stage in test.stages:
        runner.run_stage(stage, logchecker_obj)


def test_logcontains_nolog(logchecker_obj, ruleset, test):
    logchecker_obj.do_nothing = True
    runner = testrunner.TestRunner()
    for stage in test.stages:
        runner.run_stage(stage, logchecker_obj)
