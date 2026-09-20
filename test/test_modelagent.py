from unittest.mock import patch
import pandas as pd
import numpy as np
import pytest

from scripts.ModelAgent import ModelAgent


@pytest.fixture
def agent_instance():
    return ModelAgent()


def test_initialization():
    agent = ModelAgent()
    assert agent is not None
    assert hasattr(agent, 'model')


@patch.object(ModelAgent, 'predict')
def test_predict_returns_model_output(mock_predict, agent_instance):
    mock_predict.return_value = np.array([0, 1, 1])
    x_test = pd.DataFrame(np.random.rand(3, 2), columns=['A', 'B'])

    result = agent_instance.predict(x_test)

    assert list(result) == [0, 1, 1]


def test_train_calls_model_fit(agent_instance):
    with patch.object(agent_instance.model, 'fit') as mock_fit:
        x_train = pd.DataFrame(np.random.rand(5, 2), columns=['A', 'B'])
        y_train = pd.Series(np.random.randint(0, 2, size=5), name='Churn')

        agent_instance.train(x_train, y_train)

        mock_fit.assert_called_once_with(x_train, y_train)


def test_evaluate_returns_correct_accuracy(agent_instance):
    y_test = [0, 1, 1, 0]
    predictions = [0, 1, 0, 0]

    score = agent_instance.evaluate(y_test, predictions)

    assert score == 0.75


def test_evaluate_perfect_score(agent_instance):
    y_test = [1, 0, 1]
    predictions = [1, 0, 1]

    assert agent_instance.evaluate(y_test, predictions) == 1.0


@patch('scripts.ModelAgent.joblib.dump')
@patch('scripts.ModelAgent.os.makedirs')
def test_run_success(mock_makedirs, mock_dump, agent_instance):
    x_train = pd.DataFrame(np.random.rand(8, 2), columns=['A', 'B'])
    x_test = pd.DataFrame(np.random.rand(2, 2), columns=['A', 'B'])
    y_train = pd.Series(np.random.randint(0, 2, size=8), name='Churn')
    y_test = pd.Series(np.random.randint(0, 2, size=2), name='Churn')

    loader = type('Loader', (), {
        'set_train_test_split': lambda self: (x_train, x_test, y_train, y_test)
    })()

    with patch.object(agent_instance.model, 'fit') as mock_fit, \
         patch.object(agent_instance.model, 'predict', return_value=np.array([0, 1])) as mock_predict:

        score = agent_instance.run(loader)

        mock_fit.assert_called_once_with(x_train, y_train)
        mock_predict.assert_called_once_with(x_test)

    assert mock_makedirs.call_count == 2
    assert mock_dump.call_count == 2
    assert isinstance(score, float)


@patch('scripts.ModelAgent.joblib.dump', side_effect=OSError("disk full"))
@patch('scripts.ModelAgent.os.makedirs')
def test_run_handles_save_exception(mock_makedirs, mock_dump, agent_instance):
    x_train = pd.DataFrame(np.random.rand(2, 2), columns=['A', 'B'])
    x_test = pd.DataFrame(np.random.rand(1, 2), columns=['A', 'B'])
    y_train = pd.Series([0, 1], name='Churn')
    y_test = pd.Series([0], name='Churn')

    loader = type('Loader', (), {
        'set_train_test_split': lambda self: (x_train, x_test, y_train, y_test)
    })()

    with patch.object(agent_instance.model, 'fit'), \
         patch.object(agent_instance.model, 'predict', return_value=[0]):

        result = agent_instance.run(loader)

    assert isinstance(result, str)
    assert result.startswith("Error: saving model:")