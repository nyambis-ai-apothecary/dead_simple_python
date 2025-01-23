# Define variables for chapter directories
CHAPTER3_DIR=chapter_3_syntax_crash_course
CHAPTER4_DIR=chapter_4_data_types

# Lint chapter3.py
lint3:
	pylint $(CHAPTER3_DIR)/chapter3.py

# Format chapter3.py with Black
black3:
	black $(CHAPTER3_DIR)/chapter3.py

# Lint chapter4.py
lint4:
	pylint $(CHAPTER4_DIR)/chapter4.py

# Format chapter4.py with Black
black4:
	black $(CHAPTER4_DIR)/chapter4.py