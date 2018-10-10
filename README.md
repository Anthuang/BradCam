# BradCam
Backup camera for wheelchair using Raspberry Pi and Python  

Alpha:

When the camera and screen are both connected to the Pi, the client will be able to see the camera output on the screen, which will be placed near the armrest. 

Beta: 

There will be a distance sensor attached to the back of the wheelchair. The distance sensor will trigger a buzzer to make beeping sounds at intervals inversely proportional to the distance away from a nearby object. This gives the client an auditory warning that there is an object nearby.This release will also feature the guidance lines on the display screen. The lines will show where the wheels are (and will be), so the client can see the tentative path they are about to take. 

This release will make sure that the buzzer does not beep when the client is not backing up. To do this, we will disable the buzzer when the screen is off. 

Omega:

In this release, we will identify the camera blind spots and attach distance sensors to those spots. The distance sensors will beep different sounds, depending on which sensor is detecting an object. This way, the client will know if there is an object in the blind spot, and can take action to avoid it. We will set a time-out for the screen. The screen will turn off automatically after 2 minutes, so the client does not have to manually turn it off. When the client wants to back up, the only work that needs to be done is clicking the power button on the screen. 

Because this is the last release, we want to make sure all wires are secure. 
