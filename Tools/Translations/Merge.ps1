#! /usr/bin/pwsh

xgettext ClasetCommandLine/Utils/ArgumentParsers.py ClasetCommandLine/CmdMainClass.py --language=python --output=./Translations/new.pot
msgmerge Translations/template.pot Translations/new.pot --output=./Translations/template.pot
Remove-Item Translations/new.pot

msgmerge Translations/zh_CN.po Translations/template.pot --output=Translations/zh_CN.po
