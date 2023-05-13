---
title: "Project Update: Progress with Hazel's Development and Transitioning to a New Stack"
intro: In this project update, we share the progress of building Hazel, an AI assistant focused on sustainability. After starting with Flask, we decided to transition to Django for its robustness. The new stack includes Python, Django, TailwindCSS, SocketIO (possibly), GPT4, and PostgreSQL. Stay tuned for GIFs showcasing Hazel's responses once the porting is complete, as we guide users towards a sustainable lifestyle.
date: 2023-05-12
tags: hazel, flask, django
type: Diary Entry
meta_description: Discover the progress of Hazel, an AI assistant project with a sustainability focus. Transitioning from Flask to Django, the new stack incorporates Python, Django, TailwindCSS, SocketIO (possibly), GPT4, and PostgreSQL. Stay tuned for GIF updates as Hazel guides users toward a sustainable lifestyle. Join our journey of creating a greener future with this innovative AI assistant.
project: hazel
---

Hello everyone! We're back with an update on our AI assistant project, Hazel. Whether you're a developer or simply curious about our journey, we have some exciting news to share. So, let's dive right in!

In the past few weeks, we've been dedicated to bringing Hazel to life and exploring different technology stacks. Initially, we built a prototype of Hazel using Flask, a lightweight web framework. This allowed us to create a web chat interface that provided real-time responses through websockets. It was quite a whirlwind, especially since we were juggling other ongoing projects.

During this phase, we stored Hazel's memory in a server variable, which was cleared with each restart. Surprisingly, we achieved satisfying results with Hazel's responses, requiring only minor adjustments. This early success gave us a much-needed boost of confidence and motivation.

As the project progressed, we reached a crossroads. We had to decide whether to continue using Flask and build the entire stack from scratch or make a transition to Django, a more feature-rich web framework. After careful consideration, we chose to embark on a Django project. Although we have fondness for Flask's flexibility, we found that Django's extensive feature set better aligned with our long-term goals.

Let's take a look at the technology stack we used previously and the exciting new stack we're transitioning to:

**Previous Stack:**

- Python: A versatile programming language known for its simplicity and readability, widely used in various domains, including web development and artificial intelligence.
- Flask: A lightweight web framework in Python, ideal for building small to medium-sized web applications with simplicity and flexibility.
- TailwindCSS: A utility-first CSS framework that provides a collection of pre-built CSS classes, allowing for rapid and responsive UI development.
- SocketIO: A JavaScript library that enables real-time bidirectional communication between the client and the server, crucial for creating interactive web applications.
- GPT3.5: The OpenAI GPT-3.5 language model, which stands for Generative Pre-trained Transformer 3.5, known for its natural language processing capabilities and ability to generate human-like text.

**New Stack:**

- Python: A versatile programming language known for its simplicity and readability, widely used in various domains, including web development and artificial intelligence.
- Django: A high-level Python web framework that provides a full-featured toolkit for building scalable and secure web applications, offering a robust set of components and conventions.
- TailwindCSS: A utility-first CSS framework that provides a collection of pre-built CSS classes, allowing for rapid and responsive UI development.
- SocketIO (To Be Determined): A JavaScript library that enables real-time bidirectional communication between the client and the server, crucial for creating interactive web applications. The specific library to be used with Django will be determined in the future.
- GPT4: The next iteration of the OpenAI GPT language model, GPT-4, known for its advancements in natural language processing and text generation capabilities.
- PostgreSQL: A powerful open-source relational database management system known for its robustness, scalability, and extensive feature set, widely used in web applications and data-driven projects.

Making the transition to Django was a natural decision for us. While we anticipate a slight learning curve, we believe it will be a worthwhile investment. We have already set up the project and app in the Django environment, ready to port Hazel over.

In the upcoming updates, we look forward to sharing GIFs that showcase Hazel's responses once the migration is complete. With the new stack, enhanced capabilities, and the power of GPT4, we are excited to witness Hazel's growth and provide an improved AI experience.

Whether you're a developer seeking technical insights or simply fascinated by AI assistants, we invite you to stay tuned for more updates on this incredible journey. Thank you for joining us, and we can't wait to share our progress with you. Until next time, stay curious and keep exploring!
