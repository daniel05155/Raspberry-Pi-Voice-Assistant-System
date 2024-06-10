# Voice Assistant System
<<<<<<< HEAD

This project is an implementation of a voice assistant system using voice commands as input on a Raspberry Pi 4.  By utilizing speech-to-text and natural language understanding (NLU) libraries in Python, we are able to interpret the user's request and offer the proper controlling and output for the program. It demostrates how to integrate multiple functionalities on a evaluation board. 
=======
>>>>>>> refs/remotes/origin/master

## Demos
- [Build an offline voice assistant on Raspberry Pi](https://youtu.be/RGPhA-muTN8?si=qIpV2iwAn5oIqxBy)

## Report
- [Voice Assistant System](https://drive.google.com/file/d/1CzHvnulT5bQumzc7UzotrrenO-l9QQVI/view?usp=sharing)

## File Structure 
```bash
├── audio
│   ├── close_sys.mp3
│   ├── got_it.mp3
│   ├── language_type.mp3
│   ├── service.mp3
│   ├── start.mp3
│   ├── translate.mp3
│   ├── TW_to_En.mp3
│   ├── TW_to_French.mp3
│   ├── TW_to_Japan.mp3
│   ├── TW_to_Neth.mp3
│   └── USA_to_TW.mp3
├── function
│   ├── auxiliary
│   │   ├── __init__.py
│   │   ├── mcp_data.py
│   │   └── utils.py
│   ├── __init__.py
│   ├── led.py
│   ├── temp_control.py
│   └── translator.py
├── main.py
├── README.MD
└── requirements.txt
```


## Requirements
* Raspberry Pi OS
* Python 3.9.2

### Install dependencies using pip
```cmd
pip install -r requirements.txt

```

## Quick Start 

The following commands can be used to launch the main program and use other functions in our system after downloading the repository, installing the prerequisites, and following the remaining setup instructions:

#### 1. Run the main program
```cmd
python main.py
```

#### 2. The user can speak the following speech commands into a microphone once the software starts and a prompt such as "say something" appears on the terminal: 

* Environment Monitoring    
    *  If temperature rises above 28 degrees, the software will activate the DC Fan, if not, it will switch off.
    * Cancel execution:
    ```cmd
    Ctrl+C 
    ```
* Light Switch
    * Cancel execution:
    ```cmd
    Ctrl+C 
    ```
* Translator
    * The following translated languages can be spoken by the user using a microphone:
        * Translate Chinese into English.
        * Translate English into Chinese.
        * Translate Chinese into Japanese.
        * Translate Chinese into Dutch.
        * Translate Chinese into French.
        
    * Cancel execution:
    ```cmd
    Ctrl+C 
    ```

## Experiment
- Based on usability and performance verification, we utilize **completion rate** as an estimate for customer experience quality. 
- Make the ten queries to each functionality in our system.

### Translation context


|                Before translation                                                   | After translation                                                      |
|:----------------------------------------------------------------------------------------------------------------------:| ---------------------------------------------------------------------- |
|                                             我想去大賣場買家用品 (Chinese)                                             | I want to go to the hypermarket buyer products. (English)              |
|                                        可以加入更多的功能在這次的專案(Chinese)                                         | You can add more features in this project. (English)                   |
|                        we cannot find the definition of this word in the dictionary. (English)                         | 我們找不到這詞在辭典的定義(Chinese)                                    |
| Voice assistance have become prevalence of a range of personal devices such as smartphones and smart meters. (English) | 語音援助已成為一系列個人設備的普遍性，例如智能手機和智能電錶 (Chinese) |
|                                                我忘記帶雨傘了 (Chinese)                                                | 傘を持ってくるのを忘れました  (Japanese)                               |
|                                          我想趕快完成功課並且出去玩(Chinese)                                           | Ik wil de oefeningen snel voltooien en gaan spelen. (Dutch)            |
|                                                我忘記帶雨傘了 (Chinese)                                                | J'ai oublié d'apporter un parapluie   (French)                         |


## Performance evaluation

|Functionality                 |Completion rate(%)|
|:------------:                |:-------------:|
| Environmen Measurement       |    80%        |
| Smart light control          |    80%        |
| Translation                  |    70%        |
