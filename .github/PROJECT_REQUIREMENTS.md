# Haroon Khan's Fast Food — Project Requirements

## 1. Project Overview

Build a responsive, user-friendly food ordering website for **Haroon Khan's Fast Food**, a local fast-food business serving the University of Technology, Nowshera, and nearby areas.

The website should allow customers to:

* View available food items and prices.
* Add food items to a shopping cart.
* Enter their delivery information.
* Place an order.
* Choose a payment method.
* See an order confirmation.
* Contact the restaurant through WhatsApp.

The restaurant should be able to manage food items and customer orders through Django Admin.

This is a learning project and a practical MVP. Prioritize a working, secure, maintainable system over unnecessary complexity.

---

## 2. Developer Background

The project owner is a beginner in web development and is learning Python and Django.

The VS Code Agent must:

* Explain concepts in simple, beginner-friendly English.
* Never assume advanced Django, database, JavaScript, or deployment knowledge.
* Explain the reason behind important code decisions.
* Prefer teaching and guiding over making unexplained changes.
* Correct misunderstandings politely.
* Work step by step and wait for confirmation at major checkpoints.

Do not overwhelm the developer with too many changes at once.

---

## 3. Business Information

### Restaurant

* Name: Haroon Khan's Fast Food
* Phone / WhatsApp: 03305583858
* Location: Near the University of Technology, Nowshera
* Delivery area: University of Technology, Nowshera, and nearby areas

### Operating Hours

* Shop hours: 11:00 AM–11:00 PM
* Delivery hours: 12:00 PM–9:00 PM

Do not assume that delivery is available outside delivery hours.

The availability of pickup or order placement after 9:00 PM is not yet finalized. Keep this behavior configurable or ask before implementing it.

### Delivery Rules

* Free delivery within 3 km of the restaurant.
* Beyond 3 km, delivery is subject to restaurant confirmation.
* Do not invent a delivery fee for distances beyond 3 km.
* Estimated delivery time: approximately 15 minutes when feasible.
* The 15-minute estimate is not a guarantee. The restaurant must confirm the actual expected time.

Do not claim precise GPS-based distance calculation unless it is actually implemented and tested.

### Payment Methods

Supported methods:

* Cash
* Easypaisa
* JazzCash

Customers may choose payment on delivery or advance payment.

The exact verification workflow for advance payments is not finalized. Do not invent payment verification, payment gateway integration, or automatic payment confirmation.

Never ask customers to enter or store wallet PINs or passwords.

---

## 4. Current Project Status

The developer has already completed the following:

* Created the project folder: `E:\haroon-fast-food`
* Created and activated a virtual environment named `env`
* Installed Django 6.1.1
* Created the Django project using `config`
* Created the Django app named `menu`
* Registered `menu` in `INSTALLED_APPS`
* Created the `Category` and `FoodItem` models
* Installed Pillow for image support
* Ran database migrations
* Registered `Category` and `FoodItem` in Django Admin
* Created a superuser
* Added the Biryani category
* Added four biryani items
* Created `menu/views.py`
* Created `menu/urls.py`

The current menu view filters available items and uses `select_related("category")`.

The current `menu/urls.py` maps its root URL to `views.menu_list`.

**Important:** Inspect the actual files before making changes. Do not assume that the existing code exactly matches this description.

Do not recreate completed work unnecessarily.

---

## 5. Current Menu Data

The following items have been entered into Django Admin.

| Category | Food Item              |   Price |
| -------- | ---------------------- | ------: |
| Biryani  | Single Sada Biryani    | Rs. 110 |
| Biryani  | Single Chicken Biryani | Rs. 150 |
| Biryani  | Double Chicken         | Rs. 250 |
| Biryani  | Double Sada            | Rs. 200 |

Prices are in Pakistani rupees (PKR).

The menu must be database-driven. Do not hardcode these food items into the HTML template.

Burgers and shawarma may be added later when their prices and details are confirmed.

---

## 6. Planned Technology Stack

### Backend

* Python
* Django
* Django ORM
* Django Forms where appropriate

### Frontend

* HTML
* CSS
* JavaScript
* Bootstrap, preferably using its CDN for the initial MVP

### Database

* SQLite for local development and learning

### Image Handling

* Pillow
* Django media uploads for food images

### Development Tools

* VS Code
* Git and GitHub

Use Django's built-in capabilities where possible. Do not install additional libraries unless a specific feature requires them.

Do not introduce React, Vue, a separate REST API, Celery, Redis, or an AI system without discussing the need with the developer first.

---

## 7. Main Website Pages

### A. Homepage

Create an attractive homepage containing:

* Restaurant name and branding
* A welcoming hero section
* A clear "View Menu" or "Order Now" button
* A short restaurant introduction
* Delivery information
* Shop and delivery hours
* Contact and WhatsApp information
* Menu highlights

The homepage should be mobile-friendly and easy to navigate.

### B. Menu Page

Display food items from the database.

Each item should show:

* Food name
* Price in PKR
* Description, if available
* Food image, if available
* Availability status
* Add-to-cart button

Group or label items by category.

Do not show unavailable items as orderable.

Provide a sensible placeholder when a food image is missing.

### C. Shopping Cart

Customers should be able to:

* Add items to the cart
* Increase or decrease quantities
* Remove items
* View item prices and quantities
* See the subtotal
* Continue to checkout

Validate cart data on the server. Never trust a price or total sent by the browser.

### D. Checkout

Collect the information necessary to fulfill an order.

Suggested fields:

* Customer name
* Phone number
* Delivery address
* Nearby landmark or location details
* Optional order instructions
* Payment method
* Payment timing: on delivery or advance payment, where supported

Validate required fields and display helpful error messages.

Do not collect unnecessary personal information.

### E. Order Confirmation

After a successful order:

* Show a confirmation message.
* Display the order reference.
* Show the ordered items and quantities.
* Show the calculated order total.
* Explain that the restaurant will confirm the order and delivery estimate.

Do not claim the restaurant has accepted or prepared an order until that status is actually recorded.

### F. Contact / WhatsApp

Provide a clear WhatsApp contact option using the restaurant number.

The WhatsApp order link should open WhatsApp with a prefilled message when supported.

The customer must press Send in WhatsApp themselves.

Do not claim that the website automatically sends WhatsApp messages.

---

## 8. Order Management

Use Django Admin for restaurant-side order management in the MVP.

Restaurant staff should be able to:

* View incoming orders
* View customer contact and delivery details
* View ordered items and quantities
* View the total
* View the selected payment method and payment timing
* Update order status

Suggested order statuses:

* Pending
* Confirmed
* Preparing
* Ready
* Out for delivery
* Delivered
* Cancelled

Choose appropriate model fields and status transitions after inspecting the current project.

Protect customer information through Django authentication and permissions.

Do not expose the Django Admin to unauthenticated customers.

---

## 9. Data Model Requirements

Inspect the existing `Category` and `FoodItem` models before modifying them.

The intended data structure includes:

### Category

* Name

### FoodItem

* Category
* Name
* Description
* Price in PKR
* Optional image
* Availability status

### Order

Should store relevant information such as:

* Unique order reference
* Customer name
* Customer phone
* Delivery address
* Optional landmark and instructions
* Payment method
* Payment timing
* Order status
* Subtotal and applicable delivery charge, if confirmed
* Final total
* Creation timestamp

### OrderItem

Should store:

* Related order
* Related food item, where appropriate
* Quantity
* Price at the time of purchase
* Line total, if useful

**Important:** Preserve the purchase-time price in the order item. If the restaurant changes a menu price later, old orders must retain their original prices.

Use database transactions where needed to prevent partially saved orders.

---

## 10. Delivery Calculation and Validation

For the MVP:

* Clearly communicate the 3 km free-delivery rule.
* Do not invent fees beyond 3 km.
* Ask the restaurant to confirm deliveries outside the free-delivery area.
* Do not guarantee the 15-minute delivery estimate.
* Do not treat a customer-entered distance as verified GPS distance.

If exact distance calculation is proposed, explain the required location data, mapping service, privacy implications, and possible costs before implementation.

---

## 11. Security and Reliability

Follow Django security best practices.

Requirements:

* Use Django's CSRF protection for forms.
* Validate all customer input on the server.
* Calculate prices and totals on the server.
* Do not trust browser-submitted prices.
* Keep secret keys and credentials out of source code.
* Do not commit `.env`, database files, or the virtual environment.
* Do not store payment PINs or passwords.
* Restrict staff-only data to authorized users.
* Handle unavailable or deleted menu items safely.
* Show understandable errors without exposing sensitive technical details.

Do not disable security protections just to make a feature work.

---

## 12. User Interface and Design

Design goals:

* Modern, attractive fast-food restaurant style
* Responsive on desktop, tablet, and mobile
* Clear food names and prices
* Easy-to-use navigation
* Readable typography
* Accessible color contrast
* Visible buttons and form validation
* Consistent spacing and layout
* Helpful empty-cart and error states

Avoid unnecessary animations or complicated effects that make the website slow or difficult to use.

Do not use unlicensed restaurant logos or pretend placeholder food photos are actual restaurant photos.

---

## 13. Development Roadmap

Build in small, verifiable stages.

### Stage 1 — Inspect and stabilize

* Inspect the current project tree and files.
* Check Django configuration.
* Confirm current models, migrations, and URL setup.
* Identify missing dependencies or configuration.
* Report issues before changing files.

### Stage 2 — Complete menu page

* Connect the main project URL to the menu app.
* Create the menu template.
* Display database-driven food items.
* Add basic styling.
* Verify the page in the browser.

### Stage 3 — Homepage and shared layout

* Create a reusable base template.
* Add navigation and footer.
* Build the restaurant homepage.
* Make the design responsive.

### Stage 4 — Cart

* Implement cart functionality.
* Validate item availability and quantities.
* Test subtotal calculations.

### Stage 5 — Checkout and orders

* Create order and order-item models.
* Add checkout validation.
* Recalculate totals on the server.
* Save orders safely.
* Create order confirmation.

### Stage 6 — Restaurant order dashboard

* Configure Django Admin for orders.
* Display useful order information.
* Allow authorized staff to update statuses.

### Stage 7 — Delivery and payment information

* Display the confirmed delivery rules.
* Implement payment method selection.
* Do not invent an unconfirmed fee or payment workflow.

### Stage 8 — WhatsApp contact

* Add a WhatsApp link with a prefilled message.
* Make clear that the customer sends the message.

### Stage 9 — Testing and polish

* Test menu display.
* Test cart operations.
* Test checkout validation.
* Test server-side totals.
* Test order persistence.
* Test mobile layout.
* Fix bugs before adding new features.

### Stage 10 — Deployment preparation

* Review environment variables and production settings.
* Configure static and media files appropriately.
* Check allowed hosts and security settings.
* Explain deployment steps before performing them.

---

## 14. VS Code Agent Working Rules

The agent must follow these rules throughout the project.

### Before editing

1. Inspect the relevant files.
2. Explain the current situation.
3. Identify the specific problem or feature.
4. Propose a small implementation plan.
5. List the files that need to change.
6. Explain any new dependencies.

### While editing

* Make minimal, focused changes.
* Preserve working features.
* Follow the existing project structure unless there is a clear reason to change it.
* Avoid rewriting entire files unnecessarily.
* Do not delete user work without permission.
* Do not create duplicate models, URLs, templates, or configuration.
* Explain important code and syntax in beginner-friendly language.

### After editing

* Summarize each changed file.
* Explain what changed and why.
* Give exact commands to run.
* Explain how to test the feature.
* Report any remaining limitations.
* Wait for the developer to verify the result before proceeding to the next major stage.

### Ask for explicit approval before

* Deleting files or data
* Resetting or recreating the database
* Removing migrations
* Installing significant new dependencies
* Changing deployment settings
* Publishing or deploying the website
* Changing DNS or domain configuration
* Handling secrets or credentials
* Force-pushing or rewriting Git history
* Making external purchases or paid service integrations

Never claim a test passed unless it was actually run and its result was observed.

---

## 15. Testing Expectations

For each feature:

1. Explain what should happen.
2. Provide the command or browser steps to test it.
3. Identify the expected result.
4. Help diagnose errors before proposing a fix.

Use Django's checks and tests when appropriate.

At minimum, verify:

* Django system check
* URL routing
* Menu database queries
* Template rendering
* Image handling
* Cart quantity validation
* Server-side price calculations
* Checkout form validation
* Order saving
* Order status updates
* Mobile responsiveness

---

## 16. Features Not Included in the Initial MVP

Do not implement these unless the developer approves them after the basic website works:

* AI chatbot or AI agent
* Automatic WhatsApp messaging API
* Online payment gateway
* GPS-based delivery tracking
* Live rider tracking
* Customer account system
* Loyalty points
* Complex analytics
* Separate frontend framework
* Automated SMS notifications

These can be considered in later versions after researching their usefulness, cost, and complexity.

---

## 17. Definition of Done

The MVP is considered ready for review when:

* Customers can open the website on desktop and mobile.
* The menu is loaded from the database.
* Available food items and prices display correctly.
* Customers can add items to a cart and edit quantities.
* Checkout validates customer input.
* Order totals are calculated securely on the server.
* Orders are saved in the database.
* Restaurant staff can view and update orders through Django Admin.
* Delivery and payment information is accurate and does not promise unconfirmed services.
* WhatsApp contact works as a customer-initiated link.
* Basic security and error handling are in place.
* The developer understands how the main features work.

---

## 18. First Task for the Agent

Start with **Stage 1: Inspect and stabilize**.

Do not immediately rewrite or generate the entire website.

First:

1. Inspect the existing project files.
2. Confirm the current Django configuration and app structure.
3. Review the existing models, views, and URLs.
4. Identify what is already complete and what is missing.
5. Explain the next small step.
6. Wait for approval before making significant changes.

The immediate development goal is to finish and test the public menu page using the existing `menu` app.
