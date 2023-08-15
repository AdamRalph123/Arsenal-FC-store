# __Arsenal FC store - Portfolio Project 5__
![mockup](docs/testing/responsive.png)

Arsenal Fc store is an online store were users can find Arsenal jerseys and accessories.

Users can register an account and buy products, usres can also contact the Araenal Fc store by filling out a contact form.

The aim of this project is to allow users to be able easily shop on the arsenal fc store.

[Live link to website](https://arsenal-fc-store-9dd3251c1b46.herokuapp.com/)


## UX

Some of the colours I used when developing this site, I kept the colours simple so it wouldnt distract the users from the site.

- `rgba(255, 0, 0, 0.767)` was used as the delivery banner and the welcome message displayed on the home page. I chose this colour as I thouhgt it represents the Arsenal FC team colour.
- `#fff` was used for the sign up.
- `#28a745` was used for some of the arrows seen on this site (bootstrap)
- `#6c757d` was used for some of the arrows seen on this site (bootstrap)
- `#dc3545` was used for some of the arrows seen on this site (bootstrap)
- `#ffc107`  was used for some of the arrows seen on this site (bootstrap)
- `#17a2b8` was used for some of the arrows seen on this site (bootstrap)
- `#f8f9fa` was used for some of the arrows seen on this site (bootstrap)
- `#343a40` was used for some of the arrows seen on this site (bootstrap)
- `#222` was used for the allauth form inner content
- `#dc3545` was used for the custom checkout box
- `#17a2b8` was used for the allauth form inner content (text-info)


## Typography

- [Lato](https://fonts.google.com/) was used for the site text.
- [Font Awesome](https://fontawesome.com/) was used for the icons seen throughout the site.


## User Stories

### Registered users

- As a first time site visitor I want to clearly be able to see the site's purpose to see if I would want to continue browsing the site. `(MUST HAVE)`
- As a user I want to clearly be able to navigate the website so I can find what I am looking for. `(MUST HAVE)`
- As a site user I want to be able to search certain products that I am looking for and to see if they are available on the website. `(SHOULD HAVE)`
- As a site user I want to be able to view all products by clicking the 'All Products ' link. `(MUST HAVE)`
- As a site user I want to be able to click on a certain product and to be brought to it's own individual page and to read the description about the product. `(MUST HAVE)`
- As a site user I want to be able to sort products by category (Home/Away/Accessories) so I can find the right category of what I am looking for. `(SHOULD HAVE)`
- As a site user I want to be able to add products to my shopping basket so that I can procced to the checkout and purchase them. `(MUST HAVE)`
- As a site user I want to be able to see the running total amount in my basket as I am shopping so I know how much I am spending. `(MUST HAVE)`
- As a site user I want to be able to checkout with a card payment so that I can purchase the products I want to buy. `(MUST HAVE)`
- As a site user I want to be able to receive an order confirmation email after I purchase from the shop so that I have a record of what I have purchased from the shop. `(SHOULD HAVE )`
- As a site user I want to be able to create an account so that I can save my billing and shipping details and to keep track of all the purchases I've made. `(MUST HAVE)`
- As a registered user I want to be able to edit my account details so that I can keep my account up to date and make changes if I need to. `(SHOULD HAVE)`
- As a site user I want to be able to add and remove items in my bag. `(MUST HAVE)`
- As a site user I want to be able to sign up to the sites mailing list so that I can stay up to date with the latest offers and promotions. `(SHOULD HAVE)`
- As a site user I want to be able to read the privacy policy so that I can a so I can understand the stores policy. `(SHOULD HAVE)`
- As a site user I want to be able to fill out a contact form so that I can enquire about a certain product or ask about my order. `(SHOULD HAVE)`
- As a site user I want to be able to see the prices of the products so I know weather or not I want to purchase the product. `(MUST HAVE)`


### Site admin

- As a site admin I want to be able to create new products from the front end so that I can easily add new products to the site. `(SHOULD HAVE)`
- As a site admin I want to be able to edit existing products so that I can ensure that all products are up to date and has the correct information. `(SHOULD HAVE)`
- As a site admin I want to be able to delete certain products that I know longer want on the site. `(SHOULD HAVE)`
- As a site admin I want to be able to set appropriate keywords on the site pages so that I can increase the chance of customers finding the site when searching for certain products. `(MUST HAVE)`
- As a site admin I want to be able to view open tickets and also mark as seen and close tickets. `(SHOULD HAVE)`


### Future features

- As a site user I want to be able to apply a discount code to receive a discount on a product. `(WONT HAVE)`
- As a site user I want to be able to read an faq page. `(WONT HAVE)`
- As a site admin I want to be bale to set the stock number on products so that I can let users know if a product is out of stock. `(WONT HAVE)`


## Wireframes

I used [balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.


### Home page wireframes

<details>
<summary>Click to view the home page wireframes</summary>

#### Desktop
![screenshot](docs/wireframes-and-models/wireframe-homepage-desktop.png)

</details>

### Basket page wireframe

<details>
<summary>Click to view the basket page wireframes</summary>

#### Desktop
![screenshot](docs/wireframes-and-models/wireframe-basket.png)

</details>

### Basket page wireframe

<details>
<summary>Click to view the checkout wireframes</summary>

#### Desktop
![screenshot](docs/wireframes-and-models/wireframe-checkout.png)

</details>

### Checkout page wireframe

<details>
<summary>Click to view the checkout wireframes</summary>

#### Tablet
![screenshot](docs/wireframes-and-models/wireframe-checkout-success.png)

</details>

### Contact page wireframe

<details>
<summary>Click to view the contact page wireframes</summary>

#### Mobile
![screenshot](docs/wireframes-and-models/wireframe-contact-us-mobile.png)

</details>

### Privacy page wireframe

<details>
<summary>Click to view the privacy page wireframes</summary>

#### Mobile
![screenshot](docs/wireframes-and-models/Privacy-mobile.png)

</details>

### Product info page wireframe

<details>
<summary>Click to view the product info page wireframes</summary>

#### Mobile
![screenshot](docs/wireframes-and-models/Privacy-mobile.png)

</details>

### Sign up page wireframe

<details>
<summary>Click to view the sign up page wireframes</summary>

#### Tablet
![screenshot](docs/wireframes-and-models/wireframe-signup-tablet.png)

</details>

### Sign up page wireframe

<details>
<summary>Click to view the sign in page wireframes</summary>

#### Desktop
![screenshot](docs/wireframes-and-models/wireframe-sign-in.png)

</details>


## Features

### Existing features

- **Home page**

    - When a user first opens the webpage they are welcome with a message on the screen on the background of the Arsenal FC stadium, there is also a 'Shop now' button that will bring the user to the products page. They will aslo be able to see the navigation bar at the top of the page.

    ![screenshot](docs/features/home-page.png)

- **Home kit page**

    - Once the user clicks on the 'Home Kit' navigation they will be brought to a page that will display only the Home kits.

    ![screenshot](docs/features/home-kit.png)

- **Away kit page**

    - Once the user clicks on the 'Away Kit' navigation they will be brought to a page that will display only the Away kits.

    ![screenshot](docs/features/away-kit.png)

- **Retro kit page**

    - Once the user clicks on the 'Retro Kit' navigation they will be brought to a page that will display only the Retro kits.

    ![screenshot](docs/features/retro-kit.png)

- **Accessories page**

    - Once the user clicks on the 'Accessories' navigation they will be brought to a page that will display only the Accesories.

    ![screenshot](docs/features/accessories-page.png)

- **Sign up page**

    - A user can register an account with is accessible when the click on 'My account' in the navigation bar. Users will be asked to enter their email address, username and password. Users will get a confirmation email once they have registered an account.

    ![screenshot](docs/features/sign-up-page.png)

- **Sign in page**

    - The sign up pages will ask the user to enter their name or email address and their password, if a user forgets their password they can click the 'forgot password' button and a email will be sent to them to reset their password. There is also a 'remember me' button.

    ![screenshot](docs/features/sign-in-page.png)

- **Sign out page**

    - When a user presses the sign out button they will be asked if they are sure they want to sign out.

    ![screenshot](docs/features/sign-out-page.png)

- **Product sorting**

    - There is a 'sory by' drop down which will allow user to sort products by price, category, rating and name.

     ![screenshot](docs/features/sorting-products.png)

- **Product detail**

    - When a user clicks on a product they will be brought to a page which will show the price of the product, the product rating and also a description of the product. It also includes a size selector dropdown, an add to bag option and a 'keep shopping button'.

    ![screenshot](docs/features/product-detail-page.png)

- **Add to bag**

    - When a user adds a product to the bag a success message will appear to notify the user the product was added to their bag and will tell the user how much more theu need to spend to receive free delivery.

    ![screenshot](docs/features/add-to-bag.png)

- **View bag**

    - The view bag page will allow customer to add more of a quantity of a ceratin product or to remove a product. The grand total will appear at the bottom of the page.

    ![screenshot](docs/features/view-bag-page.png)

- **Checkout page**

    - The checkout page will show the user what they are ordering and the user will also be asked to fill in their name, email and home address, a save information button is at the bottom of the page for faster checkout if the user wants to return to the store.

     ![screenshot](docs/features/checkout-page.png)

- **Checkout confirmation page**

    - A checkout confirmation page will be shown once the user has entered their correct card details showing what they have order. A confirmation email will be sent to the user too.

    ![screenshot](docs/features/checkout-confirmation.png)

- **Profile page**

    - The profile page allows users to update their information if needed and the user can also see their order history.

    ![screenshot](docs/features/my-profile-page.png)

- **Admin add product**

    - When the admin is logged in a product management naviagtion will show allowing the admin to add new products to the store.

    ![screenshot](docs/features/admin-add-products.png)
    ![screenshot](docs/features/product-management-1.png)
    ![screenshot](docs/features/product-mangement-2.png)

- **Edit and delete product**

    - When the admin is logged in they can an edit and delete button will show on any product, the admin can edit a certain product and also delete a product from the store.

    ![screenshot](docs/features/edit-delete-admin.png)
    ![screenshot](docs/features/edit-products-1.png)
    ![screenshot](docs/features/edit-products-2.png)

- **Back to top button**

    - A back to top button is displayed on the products page which will bring the user to the top of the page when clicked.

    ![screenshot](docs/features/back-to-top.png)

- **Footer**

    - Social media icons are at the bottom of each page which will bring user to the selected page.

    ![screenshot](docs/features/footer.png)

- **Privacy page** 

    - A privacy button is at the bottom of each page in the footer which will bring the user to the privacy policy page.

    ![screenshot](docs/features/privacy-contact.png)
    ![screenshot](docs/features/privacy-page.png)

- **Contact page** 

    - A contact button is at the bottom of each page in the footer which will bring the user to a conatct page with a detailed map and a contact form that the user can fill out.

    ![screenshot](docs/features/privacy-contact.png)
    ![screenshot](docs/features/contact-page.png)

- **Product review** 

    - A user can leave a review on a product which will have to be approved by the admin.

    ![screenshot](docs/features/review-comment.png)

- **Search bar** 

    - A search bar is in the navigation bar which allows users to search for a product.

    ![screenshot](docs/features/search-bar.png)

- **Nav bar (smaller screen)**

    - When the user is view the site on small screen the nav bar becomes a dropdown.

    ![screenshot](docs/features/dropdown-mobile-view.png)
    ![screenshot](docs/features/nav-mobile-view.png)





