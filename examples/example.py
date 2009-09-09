# coding: spec
from should_dsl import should_be

class Bowling:
    score = 0
    def hit(self, v):
        self.score += v

describe Bowling:
    def before_each:
        self._bowling = Bowling()

    it "should score 0 for gutter game":
        self._bowling.hit(0)
        self._bowling.score |should_be.equal_to| 0

    it "should score 1 for just one hit":
        self._bowling.hit(1)
        self._bowling.score |should_be.equal_to| 1

bar = 1
describe Foo:
    def before_each:
        self._bar = bar

    def after_each:
        global bar
        bar += self._bar

    it "should do nothing":
        self._bar |should_be.equal_to| 1

    it "should do nothing2":
        self._bar |should_be.equal_to| 2
