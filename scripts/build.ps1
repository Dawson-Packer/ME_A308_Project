pwsh -File ./venv/Scripts/Activate.ps1
python ./scripts/build.py
arduino-cli compile --fqbn arduino:avr:uno --verbose ./source