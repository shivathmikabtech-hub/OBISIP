<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shivathmika's Portfolio</title>
  <link rel="stylesheet" href="port.css">
</head>
<body>
  <header>
    <h1>Shivathmika Inaganti</h1>
    <p>Web Developer</p>
    <nav>
      <ul>
        <li><a href="#about">About</a></li>
        <li><a href="#projects">Projects</a></li>
        <li><a href="#resume">Resume</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <section id="about">
      <h2>About Me</h2>
      <p>I am a passionate web developer with experience in HTML, CSS, and JavaScript. I love creating beautiful and functional websites.</p>
    </section>

    <section id="projects">
      <h2>My Projects</h2>
       <div class="side2">
            <img src="C:\Users\AKSHAY\OneDrive\Desktop\web.png" alt="image" align="right" width="500"height="345">
        </div>
      <ol>
        <li>
          <h3>Landing page </h3>
          <p>It is a landing page of magic brick company who sales properties</p>
          <a href="">Live Demo</a>
        </li>
         <li>
          <h3>Portfolio</h3>
          <p>It is portfolio of a web developer</p>
          <a href="">Live Demo</a>
        </li>
         <li>
          <h3>Temperature converter</h3>
          <p>It is used to convert the temperature into different units</p>
          <a href="">Live Demo</a>
        </li>
        
        <!-- Add more project items here -->
      </ol>
    </section>

    <section id="resume">
      <h2>Resume</h2>
      <a href="resume.pdf" download>Download Resume</a>
    </section>

    <section id="contact">
      <h2>Contact Me</h2>
      <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Send Message</button>
      </form>
    </section>
  </main>

  <footer>
    <p>&copy; 2024 Shivathmika Inaganti. All rights reserved.</p>
  </footer>
</body>
</html>