from unittest.mock import patch
import pandas as pd
import numpy as np
import pytest
import pandas.testing as pdt

from scripts.DataLoader import DataLoader

@pytest.fixture
def loader_instance():
    return DataLoader()

def test_initialization():
    loader = DataLoader()
    assert loader is not None
    assert hasattr(loader, 'path')

@patch.object(DataLoader, 'load')
def test_split_data(mock_load, loader_instance):
    mock_load.return_value = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'Churn'])
    df=mock_load.return_value
    fake_x=df.drop(columns=['Churn'])
    fake_y=df['Churn']
    x,y=loader_instance.split_data_x_y()
    pdt.assert_frame_equal(fake_x, x)
    pdt.assert_series_equal(fake_y, y)

@patch.object(DataLoader, 'split_data_x_y')
def test_set_train_test_split_calls_split_correctly(mock_split, loader_instance):
    mock_split.return_value = (pd.DataFrame(np.random.rand(10, 3), columns=['A', 'B', 'C']),pd.Series(np.random.randint(0, 2, size=10), name='Churn'))
    x_train, x_test, y_train, y_test = loader_instance.set_train_test_split()
    assert len(x_train) == 8
    assert len(x_test) == 2
    assert len(y_train) == 8
    assert len(y_test) == 2

    assert len(x_train) == len(y_train)
    assert len(x_test) == len(y_test)


def test_get_column(loader_instance):
    fake_x=pd.DataFrame(np.random.rand(10, 3), columns=['A', 'B', 'C'])
    length=loader_instance.get_columns(fake_x)
    assert isinstance(length, list)
    assert length == ['A', 'B', 'C']




