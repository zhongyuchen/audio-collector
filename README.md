# audio-collector

Audio collecting website for building a dataset for Digital Signal Processing course project

## Parameters

* File format: `.wav`
* Sampling rate: 16kHz
* Encoding: PCM (Uncompressed audio)
    + check `formatTag`, `0001` at 0xC~0xD, which stands for PCM format
    + also, it's little endian!

## Usage

https://czhongyu.github.io/audio-collector/

* 