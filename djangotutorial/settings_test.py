# -*- coding:utf-8 -*-
from djangotutorial.settings import *
import os

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
#カバレッジレポート(html)を出力するフォルダを指定
COVERAGE_REPORT_HTML_OUTPUT_DIR = '.cover'

# テスト実行時の引数の設定(noseの引数)
NOSE_ARGS = [
    '--with-xunit',
    '--with-coverage',
    '--cover-xml',
    '--cover-html',
    '--cover-package=polls', #テストを行うapp名を指定
]

#テスト用のB環境の設定(settings.pyのDB環境と分けている)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test.db'),
    }
}
