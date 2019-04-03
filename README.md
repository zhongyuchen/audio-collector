# audio-collector

![build status](https://img.shields.io/badge/build-passing-green.svg)
[![recorder version](https://img.shields.io/badge/recorder-unknown-yellow.svg)](https://github.com/xiangyuecn/Recorder)
[![d3 version](https://img.shields.io/badge/d3-5.7.0-yellow.svg)](https://d3js.org)
[![jquery version](https://img.shields.io/badge/jquery-3.3.1-yellow.svg)](https://jquery.com/)
[![Materialize version](https://img.shields.io/badge/Materialize-1.0.0-yellow.svg)](https://materializecss.com/)
[![Apache License](https://img.shields.io/badge/license-Apache2.0-blue.svg)](http://www.apache.org/licenses/)

Audio collecting website for building a dataset for Digital Signal Processing course project

## Words

Record the following 20 words 20 times each (__400 in total__)

|  00    |   01  |    02  |   03  |    04    |    05 |   06   |  07   |    08  |    09    |
| ------ | ------ | ------ | ------- | ------- |------ | ------ | ------ | ------- | ------- |
| 数字    | 语音   | 语言   | 识别     | 中国    | 总工    | 北京   | 背景   | 上海     | 商行    |

|  10    |   11  |    12  |   13  |    14    |    15 |   16   |  17   |    18  |    19    |
| ------ | ------ | ------ | ------- | ------- |------ | ------ | ------ | ------- | ------- |
| 复旦    | 饭店   | Speech | Speaker | Signal  |Process | Print | Open   | Close   | Project |

## Parameters

| file | format | channels  |   sampling rate  | length |
| ------ | ------ | ------ | ------- | ------- |
| `.wav` | PCM (Uncompressed audio) | 1 | 16 kHz | ~2 s |

If you'd like to get more information about the audio file, 
you can look closely at the header of the file.
While doing so, keep in mind that it's little endian encoding!

## Usage

https://czhongyu.github.io/audio-collector/

* Check the __toast__ appearing at the upper-right corner
    + If it's `Compatible browser` means the current browser is good to go!
    + If it's `Please use another browser!` means the browser isn't compatible and Chrome is recommended!
* Allow the browser to access your mic, otherwise the start button will remain disabled!
* Input your student ID and the `number`
    + the prompt word should change as well
    + `round = number / 20 + 1`, all 20 words will be recorded once in each round and there are 20 rounds
    + `label = number % 20`, the 20 words are labeled from `00` to `19`
* How to record:
    + Press start button to start recording, which will end in about 2 seconds
    + Say the prompt word clearly and check if there are significant changes in __the curve__ and __the bar__
    + Confirm your recording by listening to it
    + Download your recording
    + Repeat the above process as the `number` changes from 1 to 400 
* check if there are 400 correctly named recordings, 20 times for each words and 20 words in total
* submit your recordings on [elearning](http://elearning.fudan.edu.cn/portal)

### Attention

* It works best with full screen!
* Remember to enable the mic as well!
* GOOD LUCK GUYS!

## Author

Zhongyu Chen
