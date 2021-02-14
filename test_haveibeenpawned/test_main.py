import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

import haveibeenpawned.main
import pytest
import mock

# @pytest.mark.parametrize('dry_run', [True, False]
def test_target_url(mocker):
    def read_target_url():
        with open('test_haveibeenpawned/resources/target_url.txt', 'rb') as fobj:
            return fobj.read()
    
    sha_hex = "A94A8FE5CCB19BA61C4C0873D391E987982FBBD3"
    ret_target_url = "https://api.pwnedpasswords.com/range/A94A8"

    mock_fn = mocker.patch('haveibeenpawned.main._req')
    mock_fn.return_value = read_target_url()

    ret , ret_target_url = haveibeenpawned.main.target_url(sha_hex)

    assert ret == read_target_url()

def test_get_sha_digest(mocker):
    ret_hash = "A94A8FE5CCB19BA61C4C0873D391E987982FBBD3".lower()

    ret = haveibeenpawned.main.get_sha_digest('test')
    assert ret == ret_hash

@pytest.mark.parametrize('match', [True, False])
def test_match_no_match(mocker, match):
    def read_target_url():
        with open('test_haveibeenpawned/resources/target_url.txt', 'rb') as fobj:
            return fobj.read()

    ret_in = read_target_url()
    sha_hex_true = "A94A8FE5CCB19BA61C4C0873D391E987982FBBD3"
    sha_hex_false = "A94A8FE5CCB19BA61C4C0873D391E987982FALSE"

    ret_true , num = haveibeenpawned.main.match_no_match(read_target_url(), sha_hex_true) 

    ret_false, num = haveibeenpawned.main.match_no_match(read_target_url(), sha_hex_false)

    if match:
        assert ret_true == True
    else:
        assert ret_false == False