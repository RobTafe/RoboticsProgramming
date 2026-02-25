# RoboticsProgramming
Repo for the robotics programming course

Package Justification (3-4 paragraphs required):
Write a brief explanation including:

Why you chose this package (pros that matter for your project)
I chose to use tkinter for this project mainly because I've used it before and am familiar with it.
Pros are: familiarity, I have previous projects to pull info from, well established with good documatation and support, no need to import new packages.

Trade-offs you considered (what other options offered and why you rejected them)
Other packages: Kivy,Streamlit,PyQt among others.
why i didnt use: had to download packages, kivy didnt work on Fedora Linux, streamlit is for web-based apps.
wrote the whole script with tkinter in a adhd hyperfocused fugue state before checking out other packages, didnt want to redo code for other packages.

How it fits the MVP philosophy (simplicity, time to implement, maintainability)
Works across Windows, macOS, and Linux so no need to write multiple compatability scripts.
Clean and manageable code structure is easy to read and quick to write

One limitation you encountered and how you worked around it 
When trying to use images, the included image handling doesn't work with PNGs.
To fix this, I imported PIL(pillow) and used its image system. eg (ImageTk.PhotoImage(Image.open.)


