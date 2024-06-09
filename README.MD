# Voice Assistant System
![Alt text](Cover-photo.jpg)

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

### Translation context in experiment

### Performance evaluation
