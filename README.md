---

# Quiz System Using Computer Vision

## Project Overview
This project aims to develop an interactive quiz system that uses computer vision technology to enhance the user experience. The system allows users to take quizzes and interact with the system using hand gestures, providing a more immersive and accessible experience for users.

## Features
- **Hand Gesture Recognition**: The system captures live video streams and detects hand gestures using MediaPipe and TensorFlow. Users can navigate through quiz options by performing gestures.
- **Real-Time Feedback**: The system processes user responses and provides instant feedback, making the quiz interactive.
- **Data Storage**: All user interactions and quiz results are stored in a database for future reference.

## Objectives
- Develop a system that tracks and responds to user movements and gestures.
- Create a user-friendly interface compatible with various devices.
- Improve quiz engagement and accessibility, accommodating users with varying levels of mobility.
- Evaluate learning outcomes and compare them to traditional quiz systems.

## System Components
- **Hand Detection Module**: This module detects hand gestures and maps them to specific quiz actions.
- **Gesture Control Module**: Recognizes user gestures and triggers appropriate system responses.
- **Video Streaming Module**: Captures live video from the user's webcam and provides real-time video frames to the hand detection module.
- **Database**: Stores quiz results and user data for review and analysis.

## Technologies Used
- **OpenCV**: A computer vision library for image processing and gesture detection.
- **MediaPipe**: A machine learning framework used for real-time hand gesture recognition.
- **TensorFlow**: An open-source platform for machine learning, used for detecting and processing hand gestures.
- **CVzone**: A computer vision library that simplifies real-time hand detection using MediaPipe.

## Installation & Setup
1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/Darshan98Solanki/Quiz-System-OpenCV.git
   ```
2. **Install Dependencies**:
   Install the necessary libraries using:
   ```bash
   pip install (all required libraries)
   ```
3. **Run the Application**:
   Start the quiz system by running the following command:
   ```bash
   python quiz_system.py
   ```

## How it Works
1. **User Initialization**: The user starts by entering their enrollment number.
2. **Hand Gesture Detection**: The system captures the live video feed from the webcam, detecting hand gestures in real-time using MediaPipe and TensorFlow.
3. **Quiz Interaction**: Users select answers by performing specific gestures, such as pointing or clicking in the air.
4. **Result Compilation**: After the quiz is completed, the system calculates the score and stores the result in the database.

## Results
The system achieved a hand detection accuracy of approximately 74-76%, making it effective for basic hand gestures in a controlled environment. 
<br/>
<br/>
![image](https://github.com/user-attachments/assets/c0ae47a7-5e5f-4d11-beaa-8a842ad7b6bf)
<p>
    <em>[ Start Screen ]</em>
</p>
<br/>
<br/>

![image](https://github.com/user-attachments/assets/fcd2825d-b648-4e35-b3fe-b7cc306ca5d2)
<p>
    <em>[ Selecting Answer ]</em>
</p>
<br/>
<br/>

![image](https://github.com/user-attachments/assets/8f11bf76-40da-4b50-abef-6eab2a582d71)
<p>
    <em>[ Final Result Screen ]</em>
</p>




## Future Scope
- **Advanced Facial Recognition**: Personalize quizzes based on the user's previous performance.
- **Expression Recognition**: Analyze the user's expressions to assess engagement during the quiz.
- **Augmented Reality Integration**: Provide an immersive AR-based quiz experience.
- **Automated Grading**: Implement automatic grading of quiz results without human intervention.
- **Adaptive Difficulty**: Adjust quiz difficulty in real-time based on user performance.

## Conclusion
This project demonstrates how computer vision can be integrated into traditional quiz systems to create an engaging, interactive, and accessible learning experience. With further development, such systems could revolutionize learning environments by making quizzes more interactive and tailored to individual needs.

## References
- [SSD: Single Shot Detector for Object Detection](https://jonathan-hui.medium.com/ssd-object-detection-single-shot-multibox-detector-for-real-time-processing-9bd8deac0e06)
- [Google AI: Real-Time Hand Tracking](https://ai.googleblog.com/2019/08/on-device-real-time-hand-tracking-with.html)
- [OpenCV Documentation](https://opencv.org/about/)
  
---

You can modify the links and placeholders as needed. Let me know if you'd like further customization!
