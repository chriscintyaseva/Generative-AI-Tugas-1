from my_ai_project.config import LLMConfig


def test_config():
    config = LLMConfig(
        model="claude-sonnet-4-5",
        temperature=0.3,
    )

    assert config.model == "claude-sonnet-4-5"
    assert config.temperature == 0.3