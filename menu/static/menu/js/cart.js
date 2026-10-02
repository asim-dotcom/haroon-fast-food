(function () {
    "use strict";

    const storageKey = "haroon-fast-food-cart";
    const cartContent = document.querySelector("#cart-content");
    const addButtons = document.querySelectorAll(".add-to-cart");
    const checkoutForm = document.querySelector("#checkout-form");
    const cartDataInput = document.querySelector("#id_cart_data");
    let cart = loadCart();

    function loadCart() {
        try {
            const storedCart = JSON.parse(localStorage.getItem(storageKey));

            if (!Array.isArray(storedCart)) {
                return [];
            }

            return storedCart.filter(function (item) {
                return (
                    item &&
                    Number.isInteger(item.id) &&
                    typeof item.name === "string" &&
                    Number.isFinite(item.price) &&
                    Number.isInteger(item.quantity) &&
                    item.quantity > 0
                );
            });
        } catch (error) {
            return [];
        }
    }

    function saveCart() {
        try {
            localStorage.setItem(storageKey, JSON.stringify(cart));
        } catch (error) {
            // The cart still works for the current page if browser storage is unavailable.
        }
    }

    function findCartItem(itemId) {
        return cart.find(function (item) {
            return item.id === itemId;
        });
    }

    function addToCart(card) {
        const itemId = Number(card.dataset.itemId);
        const itemName = card.dataset.itemName;
        const itemPrice = Number(card.dataset.itemPrice);
        const existingItem = findCartItem(itemId);

        if (!Number.isInteger(itemId) || !itemName || !Number.isFinite(itemPrice)) {
            return;
        }

        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cart.push({
                id: itemId,
                name: itemName,
                price: itemPrice,
                quantity: 1
            });
        }

        saveCart();
        renderCart();
    }

    function changeQuantity(itemId, amount) {
        const item = findCartItem(itemId);

        if (!item) {
            return;
        }

        item.quantity += amount;

        if (item.quantity <= 0) {
            removeFromCart(itemId);
        } else {
            saveCart();
            renderCart();
        }
    }

    function removeFromCart(itemId) {
        cart = cart.filter(function (item) {
            return item.id !== itemId;
        });
        saveCart();
        renderCart();
    }

    function formatPrice(amount) {
        return "Rs. " + amount.toLocaleString("en-PK");
    }

    function createCartItem(item) {
        const row = document.createElement("article");
        const details = document.createElement("div");
        const name = document.createElement("h3");
        const unitPrice = document.createElement("p");
        const controls = document.createElement("div");
        const decreaseButton = document.createElement("button");
        const quantity = document.createElement("span");
        const increaseButton = document.createElement("button");
        const lineTotal = document.createElement("p");
        const removeButton = document.createElement("button");

        row.className = "cart-item";
        details.className = "cart-item-details";
        name.className = "cart-item-name";
        unitPrice.className = "cart-item-unit-price";
        controls.className = "quantity-controls";
        decreaseButton.className = "quantity-button";
        quantity.className = "quantity";
        increaseButton.className = "quantity-button";
        lineTotal.className = "cart-line-total";
        removeButton.className = "remove-item";

        name.textContent = item.name;
        unitPrice.textContent = formatPrice(item.price) + " each";
        decreaseButton.type = "button";
        decreaseButton.textContent = "−";
        decreaseButton.setAttribute("aria-label", "Decrease quantity of " + item.name);
        quantity.textContent = item.quantity;
        increaseButton.type = "button";
        increaseButton.textContent = "+";
        increaseButton.setAttribute("aria-label", "Increase quantity of " + item.name);
        lineTotal.textContent = formatPrice(item.price * item.quantity);
        removeButton.type = "button";
        removeButton.textContent = "Remove";

        decreaseButton.addEventListener("click", function () {
            changeQuantity(item.id, -1);
        });
        increaseButton.addEventListener("click", function () {
            changeQuantity(item.id, 1);
        });
        removeButton.addEventListener("click", function () {
            removeFromCart(item.id);
        });

        details.append(name, unitPrice);
        controls.append(decreaseButton, quantity, increaseButton);
        row.append(details, controls, lineTotal, removeButton);

        return row;
    }

    function renderCart() {
        cartContent.replaceChildren();

        if (cart.length === 0) {
            const emptyMessage = document.createElement("p");
            emptyMessage.className = "cart-empty";
            emptyMessage.textContent = "Your cart is empty. Add something delicious from the menu.";
            cartContent.append(emptyMessage);
            return;
        }

        const cartList = document.createElement("div");
        const summary = document.createElement("div");
        const summaryLabel = document.createElement("strong");
        const subtotal = document.createElement("strong");
        const total = cart.reduce(function (sum, item) {
            return sum + item.price * item.quantity;
        }, 0);

        cartList.className = "cart-list";
        summary.className = "cart-summary";
        summaryLabel.textContent = "Subtotal";
        subtotal.textContent = formatPrice(total);

        cart.forEach(function (item) {
            cartList.append(createCartItem(item));
        });

        summary.append(summaryLabel, subtotal);
        cartContent.append(cartList, summary);
    }

    addButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            addToCart(button.closest(".menu-card"));
        });
    });

    checkoutForm.addEventListener("submit", function () {
        cartDataInput.value = JSON.stringify(
            cart.map(function (item) {
                return {
                    id: item.id,
                    quantity: item.quantity
                };
            })
        );
    });

    renderCart();
})();
