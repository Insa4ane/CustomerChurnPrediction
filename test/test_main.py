from unittest.mock import patch, MagicMock
from train.train import train_model as main


@patch('main.Frontend')
@patch('main.joblib.load')
@patch('main.Path')
@patch('main.ModelAgent')
@patch('main.DataLoader')
def test_main_trains_model_when_file_missing(
    mock_loader_cls, mock_agent_cls, mock_path_cls, mock_joblib_load, mock_frontend_cls
):
    mock_path_instance = MagicMock()
    mock_path_instance.is_file.return_value = False
    mock_path_cls.return_value = mock_path_instance

    mock_loader = mock_loader_cls.return_value
    mock_agent = mock_agent_cls.return_value
    mock_joblib_load.return_value = {"age": "int64", "plan": "object"}
    mock_frontend = mock_frontend_cls.return_value
    main()
    mock_agent.run.assert_called_once_with(mock_loader)
    mock_joblib_load.assert_called_once()
    mock_frontend_cls.assert_called_once_with({"age": "int64", "plan": "object"})
    mock_frontend.run.assert_called_once()


@patch('main.Frontend')
@patch('main.joblib.load')
@patch('main.Path')
@patch('main.ModelAgent')
@patch('main.DataLoader')
def test_main_skips_training_when_file_exists(
    mock_loader_cls, mock_agent_cls, mock_path_cls, mock_joblib_load, mock_frontend_cls
):
    mock_path_instance = MagicMock()
    mock_path_instance.is_file.return_value = True
    mock_path_cls.return_value = mock_path_instance

    mock_agent = mock_agent_cls.return_value
    mock_joblib_load.return_value = {"age": "int64"}
    mock_frontend = mock_frontend_cls.return_value

    main()

    mock_agent.run.assert_not_called()
    mock_joblib_load.assert_called_once()
    mock_frontend_cls.assert_called_once_with({"age": "int64"})
    mock_frontend.run.assert_called_once()