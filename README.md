# Together AI Chat and Image App

Welcome to the **Together AI Chat and Image App**! This application uses Flet for building interactive UIs and Together API for generating chat responses and images. The app features a chatbot interface and an image generator, all powered by Together's API.

## Project Structure

The project is organized to keep code modular and maintainable:
- **main.py**: Sets up the app and loads the chat and image generator tabs.
- **chat_page.py**: Handles the chatbot interface, allowing users to chat with an AI model.
- **image_generator_page.py**: Handles the image generation, allowing users to generate images based on text prompts.
- **utils.py**: Provides helper functions used across the application.

## Features

- **Chatbot Interface**: Communicate with an AI-powered chatbot. The chat interface includes real-time message display with auto-scrolling.
- **Image Generator**: Generate AI-based images by describing your desired image, with a built-in loading indicator during generation.

## Getting Started

Follow these steps to get the app up and running on your local machine.

### Prerequisites

- Python 3.7 or higher
- Virtual environment support

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/bernhard759/ai_chat_image_fletapp.git
   cd ai_chat_image_fletapp
   ```

2. **Set Up Virtual Environment**:
   In the project root, create a virtual environment to manage dependencies:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - **On Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **On macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   With the virtual environment activated, install the required packages from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**:
   Create a `.env` file in the project root directory to store your Together API key. The `.env` file should look like this:
   ```plaintext
   TOGETHER_API_KEY=your_together_api_key_here
   ```

6. **Run the Application**:
   ```bash
   python src/main.py
   ```

## Usage

### Chat with AI

1. Open the **Chat** tab.
2. Type a message in the input box and press **Send**.
3. The chatbot will respond, and messages will appear in the chat list view.

### Generate Images

1. Open the **Image Generator** tab.
2. Describe the image you want to create in the input field.
3. Press **Generate Image** and wait for the loading indicator to complete.
4. The generated image will appear once ready.

## Project Workflow

This app uses Flet for the frontend, Together API for AI functionalities, and dotenv for managing environment variables. The project is structured to separate logic by functionality:

- **main.py**: Sets up the tabs and loads each page view.
- **chat_page.py** and **image_generator_page.py**: Each page is a standalone component, encapsulating layout and functionality.
- **utils.py**: Contains helper functions like `add_message`, which are reusable in different parts of the project.

## Future Enhancements

- Improved error handling and user feedback.
- Adding more advanced options for the image generator, such as setting resolution or style.
- Additional customization options for the chatbot interface.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any improvements or bug fixes.

## License

This project is open-source and available under the [MIT License](LICENSE).
