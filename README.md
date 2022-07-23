# course_mgt

A simple course mgt system(Coding challenge 2-4hours)

## Installation

- Docker:

  ` docker-compose up`

List of uncompleted tasks

- view all the courses i've completed
- view percentage of completed courses
- see which students are taking in a specifc course
- view all my students

## What i would have done give additional time.

- Write tests for my application and a Good ReadMe

- I would make validation for video file submitted in the course_create api

- Optimize how course contents are stored:
  I would have created a many-one relationship of contents->Course

  And using the django contenttype app and model inheritance, i would create a diverse model that various types of contents(Files, videos, audios, pictures) could be stored in the contents model
