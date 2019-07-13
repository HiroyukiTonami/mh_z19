#!/usr/bin/env python
# -*- coding: utf-8 -*-
# original:http://pongsuke.hatenablog.com/entry/2016/08/03/135434
import time
import RPi.GPIO as GPIO

PIN_PWM = 21

def getPwm():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_PWM,GPIO.IN)
    time.sleep(0.2)

    while GPIO.input(PIN_PWM) == 1:
            last_high = time.time()
    while GPIO.input(PIN_PWM) == 0:
            last_low = time.time()
    while GPIO.input(PIN_PWM) == 1:
            last_high = time.time()

    span_high = (last_high - last_low) * 1000
    print("span_high : " + str(span_high))


    while GPIO.input(PIN_PWM) == 0:
            last_low = time.time()
    while GPIO.input(PIN_PWM) == 1:
            last_high = time.time()
    while GPIO.input(PIN_PWM) == 0:
            last_low = time.time()

    span_low = (last_low - last_high) * 1000
    print("span_low : " + str(span_low))

    print("Cycle : " + str(span_high + span_low))

    co2     = 5000 * ( span_high - 2 ) / ( span_high + span_low - 4 )
    GPIO.cleanup()
    return co2

print getPwm()