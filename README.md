# Karma Coffee - Ethical Coffee Ecommerce

![karma-coffee](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/aa5eea7d-9988-4ad3-b80d-760e32fb1f2e)

<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About The Project</a>
    <li><a href="#my-contribution">My Contribution</a>
    <li><a href="#website">Visit the Itinera Site</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#erd">ERD</a></li>
    <li><a href="#wireframe">Wireframe</a></li>
    <li><a href="#planning">Planning</a></li>
    <li><a href="#biggest-challenge">Biggest Challenge</a></li>
    <li><a href="#user-feedback">User Feedback</a></li>
    <li><a href="#next-steps">Next Steps</a></li>
    <li><a href="#wins">Wins</a></li>
    <li><a href="#key-learnings">Key Learnings</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About

Karma coffee is a functional ecommerce website, for the sale of ethically sourced coffee. It was made as a group project during my time at General Assembly's software engineering immersive course. For this project I worked with two others and further on in this ReadMe I will specify my contributions.

The website features a landing page with information about the product and company, as well as a carousel of best seller products. Customers can purchase coffee as a 'guest' user, or they can sign up using their email, or Google 0Auth, in order to keep a track of their order history.

From the 'Coffee' page customers can use a filter menu to find coffee by roast type or country of origin. When they click to see a product each product page features a product image, information on flavour notes, and a review section where they can add a review of the product once they've purchased and their delivery is confirmed. On the product page they can select a quantity and product type and add to cart.

The cart is fully editable and there they can amend quanities or remove items before heading to checkout. For the checkout I chose to use the Stripe API, and redirect to an order confirmation page (or a cancel page depending on the outcome of payment) from where a user can continue shopping or view their order via the account page. The account page allows users to track past orders and see delivery updates, as well as amend their personal details.

## My Contribution

For this project I built:

<ul>
  <li>Landing page</li>
  <li>About page</li>
  <li>Account page</li>
  <li>Checkout page</li>
  <li>Cart page</li>
  <li>Add to cart modal</li>
  <li>Collapsible menus on Coffee page</li>
</ul>
and I also:
<ul>
  <li>Managed the GitHub repo</li>
  <li>Built our Trello and ran rituals as Scrum master</li>
  <li>Full mobile responsivity</li>
  <li>Logo and UX design</li>
</ul>

**Built With**

The fullstack application was made using these tools:

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

## Website

<strong><p><a href="https://karma-coffee-abe41bfb39f9.herokuapp.com/">Click to view the Karma Coffee website ☕</a></p></strong>

<!-- GETTING STARTED -->

## Getting Started

- Visit the <a href="https://karma-coffee-abe41bfb39f9.herokuapp.com/">website</a>

**Home Page**

- Here you can review top products, click to learn more about the company or click to 'Shop Coffee'.

**Log In and Sign Up Page**

- You can create an account via email.
- You can also sign up through Google OAuth.

**Coffee Product Page**

- If you'd like to filter the products, simply:
  - Click 'Origin' to filter down the products by origins.
  - Click 'Origin' to filter down the products by roast level.
- Click on a specific item to view the product in more detail.

**Product Detail Page**

- Add quantity and click 'Add to Cart' button to buy the coffee.
- Scroll down to explore customer reviews and ratings.

**Cart Page**

- See which products you put in your cart.
- Check quantity and price of the products you have in cart.
- Update the quantity and delete products if you need.
- You can check the total price and click 'Go to Checkout' button to purchase.

**Payment Page**

- Via Stripe, you can input your delivery address and add card details, to pay.
- Here are come test card details in order to complete stripe checkout

  - Test Card: For successful payment
    4242 4242 4242 4242
  - Test Card: For failed payment
    4000 0000 0000 0002
  - Test Card: 3DS Auth Needed
    4000 0027 6000 3184

  - Enter any expiry date, for example:
    12/34
  - Enter any 3 digit security code, for example:
    234

**Account Page**

- Check your order history.
- Update your personal account details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Planning

## ERD

This was our original ERD for the planning of the project, in actual fact we didn't need to create a payment or address model and instead just used data from the Stripe API to amend the status of our Orders.

![Karma Coffee](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/75a9cb5f-5594-4f9e-abf6-8b5bc28418e9)

## Wireframe

Drawing inspiration from a few different ecommerce and coffee websites that resonated with me and the team, I created these Wireframes to help guide our direction aesthetically, and it also helped us think about the architecture of the software itself.

![Wireframe for Karma Coffee Website](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/d37c1587-dde5-43fc-a373-57df903208fd)

**Aim**

To build a fullstack web application using Python, Django, and postgreSQL, and use atleast one external API.

**Landing Page**

- Users will land on a home page that highlights who the company is, what we do, and encourages them to enter the purchase funnel through calls to action.

**Product Selection and Filters**

- Users can easily browse through and filter our diverse product selection.

**Oauth/Login**

- Users will be able to sign up via Google OAuth or email.

**Profile Page**

- The user will have a account page where they can see all of their past orders, and update acccount details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Project Brief

- Have at least 2 data entities in addition to the User Model - one entity that represents the main functional idea for your app and another with a One:Many or Many:Many relationship with that main entity.
- Use OAuth authentication.
- Implement basic authorisation that restricts access to features that need a logged in user in order to work.
- Have full-CRUD (Create Read Update Delete) data operations somewhere within the app's features.
- Have a consistent and polished user interface.
- Be deployed online via Heroku.

## MVP - Minimum Viable Product

- [x] AAU, I want a way to login.
- [x] AAU, I want to see the products and product details.
- [x] AAU, I want to add items in the basket, and edit, delete the items in the basket.
- [x] AAU, I want to be able to purchase products.
- [x] AAU, I want to be able to leave and delete reviews for the products I purchased.

## NTH - Nice to have

- [x] AAU, I want to be able to filter the products and find what I want.
- [x] AAU, I want to see payment/order confirmation, so I know I've paid.
- [x] AAU, I'd like to see my order history, and track delivery.
- [x] AAU, I'd like to read more about the company.
- [x] AAU, I'd like to be able to log in with Google.
- [ ] AAU, I want to be able to search specific item.
- [ ] AAU, I want to be able to subscribe to an email newsletter.

## Actual Project Screenshots

Having a combined aesthetic vision before we started, and understanding the user flow intently allowed us to create a product very close to our wireframes and with a customer journey that is intuitive and clean.

![app screensot](https://github.com/SimpsonRoss/karma-coffee/assets/93015253/7bf577fa-3b69-4048-b7ef-4936ea5add04)

## Biggest Challenge

- I found the toughest part of this challenge was learning about GitHub management and having to troubleshoot commit issues and conflicts. Conversely it was what I enjoyed learning the most, and it felt empowering to learn more about how software development teams work together fluidly.

- Secondly, the most challenging aspect in the code was figuring out how we were going to create the order model and differentiate between it's different stages from Cart -> Paid -> Shipped -> Delivered and how that would alter the user experience at each step.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## User Feedback

- [x] Add a larger selection of products
- [x] Allow users to see their order history
- [x] Checkout and purchase as a guest
- [x] Add other authorisation methods
- [ ] Better mobile view

## Next Steps

- Standardise CSS styling across the site
- Improve the mobile view
- Add further order details to the order confirmation page

<!-- --------------------------- -->

## Wins

- **Working as a team, comitting to one project:**
  This was the first time I'd worked on a project from start to finish with a group of other developers. We had to overcome a lot of issues, and work tirelessly to resolve conflicts and draw diagrams of commits and rebases to form a mental picture of how we were working. In the end, working out these issues together became the task and the software was almost secondary.

- **Agile software development:**
  It was incredibly rewarding being able to go from ideation to a finished product in just one week. I facilitated a group planning session based on learnings from the bookes Agile Samurai and the Secrets of Facilitation. We managed to find a key area that we were all passionate about and take everyones ideas into consideration so that we were all equally bought into the product. We had daily standups and worked from a combined product backlog, that allowed transparency and prioritisation that was key with our short timeframe.

## Mistakes / Bugs

- **GitHub process becoming convoluted:**
  Early on we followed a process whereby we'd create superfluous branches locally and on GitHub, and after consulting a senior software engineering manager from Spotify we learnt more about rebasing and how teams work together in larger tech companies. We adapted our workflow and were able to have much more freedom and autonomy when writing code, without worrying about conflicts.

- **No edit functionality on reviews:**
  This was just below the priority cut off point when it came to functionality we had time to execute. It's something we'd like to add in the future.

- **Modal issues:**
  There is a still a lingering success message that can trigger the add to cart modal to show when a user clicks into the product detail page. This is something I'm looking to resolve shortly.

- **Pair programming:**
  We were reluctant to pair program at first and that led to more blockers for team members. The execution of the log in/ sign up feature took longer than it needed too, and I think we could have fixed that early on with better communication and more collaboration on features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Key Learnings

- **GitHub deployment communication:**
  Getting on the same page with ways of working early on, and ensuring you all fully understand the 'what' and 'why' of your workflow is something we learned the importance of. Some more time spent determining this, sharing diagrams and being honest about our understanding could have saved some time further into the project.

- **Mobile first:**
  We regretted not designing for mobile first, due to the prevalance of mobile browsing now. I retroactively managed to make the site mobile responsive, but it was much harder and led to a lesser experience than on Desktop.

- **Definition of done:**
  Defining a definition of done, clearly, so that we all knew what was expected before marking something as completed in the product backlog could have prevented some smaller tasks from falling into a grey area, or tech debt building up.

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->

## Contact

Ross Simpson - [My LinkedIn](https://www.linkedin.com/in/simpsonre/) - thisisrosssimpson@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

These resources helped us greatly in the completion of our project.

- [Bootstrap](https://getbootstrap.com/)
- [Trello](https://trello.com/)
- [Photopea](https://www.photopea.com/)
- [Google 0Auth](https://cloud.google.com/endpoints/docs/openapi/authenticating-users-auth0)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
