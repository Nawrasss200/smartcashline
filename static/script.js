document.addEventListener("DOMContentLoaded", () => {

    const contactForm = document.getElementById("contactForm");
    const formMessage = document.getElementById("formMessage");

    if (contactForm) {

        contactForm.addEventListener("submit", (event) => {

            event.preventDefault();

            const name = document.getElementById("name").value.trim();
            const email = document.getElementById("email").value.trim();
            const message = document.getElementById("message").value.trim();

            if (!name || !email || !message) {

                formMessage.textContent =
                    "يرجى تعبئة جميع الحقول.";

                formMessage.style.color = "#ff8f8f";

                return;
            }

            const subject =
                encodeURIComponent(
                    "استفسار جديد من موقع Smart CashLine"
                );

            const body =
                encodeURIComponent(
                    `الاسم: ${name}\n` +
                    `البريد الإلكتروني: ${email}\n\n` +
                    `الرسالة:\n${message}`
                );

            const mailto =
                `mailto:smartcashline@gmail.com?subject=${subject}&body=${body}`;

            formMessage.textContent =
                "سيتم فتح تطبيق البريد لإرسال رسالتك...";

            formMessage.style.color = "#56f0bd";

            setTimeout(() => {
                window.location.href = mailto;
            }, 500);
        });
    }


    /* ================= NAVBAR SCROLL ================= */

    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", () => {

        if (!navbar) return;

        if (window.scrollY > 30) {

            navbar.style.background =
                "rgba(5, 8, 15, 0.90)";

        } else {

            navbar.style.background =
                "rgba(5, 8, 15, 0.72)";
        }
    });


    /* ================= REVEAL ANIMATION ================= */

    const revealElements =
        document.querySelectorAll(
            ".service-card, .about-card, .contact-box, .cta-box"
        );

    const observer =
        new IntersectionObserver(
            (entries) => {

                entries.forEach((entry) => {

                    if (entry.isIntersecting) {

                        entry.target.style.opacity = "1";
                        entry.target.style.transform =
                            "translateY(0)";

                        observer.unobserve(entry.target);
                    }
                });

            },
            {
                threshold: 0.12
            }
        );


    revealElements.forEach((element) => {

        element.style.opacity = "0";
        element.style.transform =
            "translateY(25px)";

        element.style.transition =
            "opacity .7s ease, transform .7s ease";

        observer.observe(element);
    });


    /* ================= CURRENT YEAR ================= */

    const yearElements =
        document.querySelectorAll(".current-year");

    yearElements.forEach((element) => {
        element.textContent =
            new Date().getFullYear();
    });

});