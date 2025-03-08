# INTRU CG assignments (In progress)
## Description

This repository contains the basic files of laboratory and practical work for students of the AIB, of the Baikal school BRICS, INRTU.
Descriptions of laboratory work are presented directly in the notebook files.

## Content 
1) [Win 3.11 Screensaver](https://github.com/gruzdev-as/INRTU_CG/blob/master/Win%203.11.%20ScreenSaver%20for%20students.ipynb)

When developing tasks, the following open sources were taken into account:
1) [MIT](https://ocw.mit.edu/courses/6-837-computer-graphics-fall-2012/)
2) Watt, Alan. 3D Computer Graphics. Addison-Wesley, 1999. ISBN: 9780201398557.

## **Star simulation program**
-This is a simple star simulation program created using Python's Pygame library. By simulating the movement and visual effects of stars, it presents a dynamic starry sky on the screen.
### **Features**
-**Randomly generate a certain number of stars to simulate the vast starry sky**.
-**The stars have a dynamic movement effect, presenting a sense of depth**.
-**The brightness of the stars will increase as they get visually closer, simulating the real starry sky effect**.
### **Code structure description**
-**new_star Function**: Used to create new stars and set their initial positions, depths and colors.
-**move_and_check Function**: Handle the movement of stars, check if stars are out of screen range or need to be updated, and adjust the brightness of stars at the same time.
-**draw_star Function**: Draw a single star on the screen.
-**The main loop part**: Responsible for handling exit events, updating star states and drawing a starry sky scene.
