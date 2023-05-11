---
title: 'Ratanagiri Rebuild: Navigating the Tech Stack Selection'
intro: The Ratanagiri project is quite special to us. It's not just about creating a site; it's about building a platform that serves the Buddhist community, resonates with their beliefs, and brings them closer together.
date: 2023-05-11
tags: ratanagiri, astro, nextjs, nuxtjs, strapi
type: Diary
project: ratanagiri
---

**Hello, fellow developers! Today, I'm thrilled to share some insights from our early-stage journey on a project that [Ben Harrison](http://benmharrison.com/) and I have embarked on: the rebuild of Ratanagiri.**

**The Ratanagiri project is quite special to us. It's not just about creating a site; it's about building a platform that serves the Buddhist community, resonates with their beliefs, and brings them closer together.**

**In these early days, one of our main tasks is the selection of the right technology stack. We have three potential stacks in mind, each with its own set of benefits and challenges:**

**Stack A:**

- [Strapi](https://strapi.io/) (A Node.js based Headless CMS)
- [Nuxt.js](https://nuxtjs.org/) (A Vue.js based Front-end Framework)

**Stack B:**

- [Strapi](https://strapi.io/) (A Node.js based Headless CMS)
- [Next.js](https://nextjs.org/) (A React.js based Front-end Framework)

**Stack C:**

- [Strapi](https://strapi.io/) (A Node.js based Headless CMS)
- [Astro](https://astro.build/) (A Front-end Build Tool to provide faster site builds)
- [React](https://react.dev/)/[Vue](https://vuejs.org/) (UI Library/Framework)

---

💡
_If you're wondering what exactly Ratanagiri is, or why we've undertaken the task of rebuilding it, let me provide a bit of context._

_Ratanagiri is more than just a website; it's a digital representation of the Aruna Ratanagiri, a Buddhist Monastery located on the border of England and Scotland. It serves as an online hub for the monastery's community, offering resources, facilitating communication, and providing spiritual teachings._

_However, like any technology, it must evolve to remain relevant and effective. Our rebuild aims to infuse new life into the platform, equipping it with modern technologies and making it more accessible, faster, and more intuitive._

_For a more detailed background, related posts, and to follow our journey from the start, do visit the [Ratanagiri Project Page](/projects/ratanagiri.html). Your feedback and suggestions on our project would be greatly appreciated!_

---

A significant part of our discussions revolves around the database technology. We are pondering if we need a heavy-duty database like Postgres or MySQL, or if a simpler, file-based database like SQLite could adequately meet our needs.

Our aim is to run the Strapi CMS on a compact server, such as [DigitalOcean's basic droplet](https://www.digitalocean.com/pricing/droplets#basic-droplets), thereby eliminating the need for a dedicated database server. This approach would allow us to store our digital assets on an S3 compatible space.

The proposed workflow involves content changes triggering a webhook, which would then signal either [Netlify](https://www.netlify.com/) or [Vercel](https://vercel.com/) to rebuild the site incrementally, updating only the altered pages, and redeploy.

This methodology perfectly aligns with the [goals we have set for this rebuild](/projects/ratanagiri.html), which include reducing the overheads and creating a site that is developer-friendly, scalable, and high-performing.

Our immediate plan is to develop a proof of concept for each stack, which would involve creating a small working model for each technology combination. We will then compare the code, performance, and ease of use of each stack. The results will guide us in choosing our final stack, and we will begin setting the development standards and patterns.

Stay tuned for more updates on this fascinating journey of ours. Your feedback and suggestions are always welcome. As always, happy coding!
