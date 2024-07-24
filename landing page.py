<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content=
        "width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="index.css" >
    <title> shivathmika Landing Page</title>
</head>

<body>
    <nav>
        <div class="heading">OASIS INTERNSHIP</div>
        <span class="sideMenuButton" 
            onclick="openNavbar()">
            &#9776
        </span>

        <div class="navbar">
            <ul>
                <li><a href="#Home">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Sign Up</a></li>
            </ul>
        </div>
    </nav>

    <!-- Side navigation bar for 
        responsive website -->
    <div class="sideNavigationBar" 
        id="sideNavigationBar">
        <a href="#" class="closeButton" 
            onclick="closeNavbar()">
            &#x274C
        </a>
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Sign Up</a>
    </div>

    <!-- Content -->
    <div class="line" id="Home">
        <div class="side1">
            <h1>MAGIC BRICKS.com</h1>
            <button>
                <a href=https://www.magicbricks.com/>
>
                    Explore More
                </a>
            </button>
        </div>
        <div class="side2">
            <img src=
"C:\Users\AKSHAY\OneDrive\Desktop\Magicbricks.jpg" alt="image" width="500"
 height="345">
        </div>
    </div>

    <section class="about" id="My Projects">
        <div class="content">
              <i class="fa fa-home" aria-hidden="true"></i>
            <div class="title">
                <span>HOUSE MODELS</span>
            </div>
            <div class="boxes">
                <div class="box">
                    <div class="topic">
                        <a href="" target="_blank">
                           BUNGALOW
                        </a>
                    </div>
                    <p>
                        A bungalow is a luxurious, modern, and mostly a single-storied building. There may be upliftment in the floor crafted into a sloped roof in some cases.
                    </p>
                </div>
                <div class="box">

                    <div class="topic">
                        <a href="" target="_blank">
                          COTTAGE
                        </a>
                    </div>
                    <p>
                       Modest cottage-style homes originated in Europe in small towns and villages.
                    </p>
                </div>

                <div class="box">
                    <div class="topic">
                        <a href="" target="_blank">
                         COLONIAL
                        </a>
                    </div>
                    <p>Colonial houses are built in a traditional style of architecture that dates back to the U.S. Colonial era. They are designed to comfortably serve as a family home, 
                      and typically feature a rectangular shape with gabled roofs, symmetrical windows, neutral color schemes, and flat exterior walls.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <section class="contact" id="contact">
        <div class="content">
            <div class="title"><span>Sign Up</span></div>
            <div class="contactMenu">
                <div class="input1">
                    <div class="label1">Your Name</div>
                    <div class="input2">
                        <input type="text" 
                            placeholder="Enter your Name here">
                    </div>
                    <div class="label1">
                        <label>Your Email</label>
                    </div>
                    <div class="input2">
                        <input type="text" 
                            placeholder="Enter your Email here">
                    </div>
                    <div class="label1">
                        <label>Your Password</label>
                    </div>
                    <div class="input2">
                        <input type="text" 
                            placeholder="Enter your Password here">
                    </div>
                    <div class="button">
                        <button>Sign Up</button>
                    </div>
                </div>
                <div class="input3">
                    <div class="rightside1">
                        <div class="title1">
                            <span>
                                Contact Us
                            </span>
                        </div>
                        <div class="content1">
                            Magicbricks Realty Services Ltd
                         Bengaluru, Karnataka.
                        </div>
                        <div class="title1">
                            <span>More Information</span>
                        </div>
                        <div class="content1">
                            Greetings to all the house buyers out there!
                            We welcome you to the platform where we
                            consistently strive to offer the best 
                            of houses.Thank you for choosing 
                            and supporting us!
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Footer section -->
    <footer>
        <div class="footer">
            <span>
                Created By
                <a href="https://www.magicbricks.com/" 
                    target="_blank">
                   shivathmika Inaganthi
                </a>
            </span>
        </div>
    </footer>
    <script src="index.js"></script>
</body>

</html>
