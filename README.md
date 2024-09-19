# Flask ISS Tracking App

**Overview**

- This project is a simple Flask application designed to track the International Space Station (ISS) location and pass times using the Open Notify API. 
- It was developed as a school assignment (for Masterschool) to practice debugging, code organization, and applying best practices in Python development.

**Features**

- Get ISS Location: Provides the current latitude, longitude, and timestamp of the ISS.
- Get ISS Pass Times: Fetches pass times for a given latitude and longitude (note: this feature is deprecated).

**Improvements and Enhancements**

During the development of this project, several improvements were made to enhance code quality and functionality:

- Error Handling
  - Enhanced Error Handling: Implemented detailed error handling in API calls to manage potential issues such as network errors and HTTP errors. Added specific error messages and status codes for better debugging and user feedback.
- Logging
  - Integrated Logging: Added a logging system to track key events and errors. Configured the logging level through environment variables to control the verbosity of log messages based on the environment (development or production). This helps in monitoring and debugging the application effectively.
- Configuration Management
  - Environment Variables: Moved all environment-specific configurations (such as API URLs, host, port) to a .env file. This makes the application more flexible and easier to configure for different environments without changing the code.
- Code Organization
  - Modular Code Structure: Refactored the code by separating the function logic into distinct modules:
    - services/iss_service.py: Handles API calls and data processing related to ISS.
    - utils/time_utils.py: Contains utility functions, such as timestamp conversion.
    - config/config.py: Manages configuration settings using environment variables.
    
    This modular approach improves code readability, maintainability, and separation of concerns.
-----------
This project is intended for educational purposes. Contributions or feedback are welcome, especially if they help in understanding debugging and improving code quality.