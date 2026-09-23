from unittest.mock import patch, MagicMock
import pytest
from train.train import train_model


@patch('train.train.Path')
@patch('train.train.ModelAgent')
@patch('train.train.DataLoader')
def test_train_model_trains_when_file_missing(
    mock_loader_cls, mock_agent_cls, mock_path_cls
):
    mock_path_instance = MagicMock()
    mock_path_instance.is_file.return_value = False
    mock_path_cls.return_value = mock_path_instance

    mock_loader = mock_loader_cls.return_value
    mock_agent = mock_agent_cls.return_value

    train_model()

    mock_agent.run.assert_called_once_with(mock_loader)


@patch('train.train.Path')
@patch('train.train.ModelAgent')
@patch('train.train.DataLoader')
def test_train_model_skips_training_when_file_exists(
    mock_loader_cls, mock_agent_cls, mock_path_cls
):
    mock_path_instance = MagicMock()
    mock_path_instance.is_file.return_value = True
    mock_path_cls.return_value = mock_path_instance

    mock_agent = mock_agent_cls.return_value

    train_model()

    mock_agent.run.assert_not_called()


@patch('train.train.Path')
@patch('train.train.ModelAgent')
@patch('train.train.DataLoader')
def test_train_model_reraises_on_failure(
    mock_loader_cls, mock_agent_cls, mock_path_cls
):
    mock_path_instance = MagicMock()
    mock_path_instance.is_file.return_value = False
    mock_path_cls.return_value = mock_path_instance

    mock_agent = mock_agent_cls.return_value
    mock_agent.run.side_effect = RuntimeError("training blew up")

    with pytest.raises(RuntimeError, match="training blew up"):
        train_model()