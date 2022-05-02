
def test_basic(loadLocalScenario):
    scenario = loadLocalScenario('basic.scenic')
    scenario.generate(maxIterations=1000)


def test_video_out(loadLocalScenario):
    scenario = loadLocalScenario('video_out.scenic')
    scenario.generate(maxIterations=1000)