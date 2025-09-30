from flask import Flask, request

app = Flask(__name__)


header = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Swayam Waghmare | Portfolio</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        body {
            font-family: 'Roboto', sans-serif;
            margin:0; padding:0;
            background: linear-gradient(to right, #fdfbfb, #ebedee);
            color: #333;
        }
        header {
            background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
            color:#fff; padding:20px; display:flex; justify-content:space-between; align-items:center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        header h1 { margin:0; font-size:24px; }
        nav a {
            color:#fff; margin:0 15px; text-decoration:none; font-weight:500; transition: 0.3s;
        }
        nav a:hover { color: #ffe600; transform: scale(1.1); }
        main { padding:30px; max-width:1000px; margin:auto; }
        footer { text-align:center; padding:15px; background:#6a11cb; color:#fff; margin-top:40px; border-top:2px solid #2575fc;}
        h2 { color:#2575fc; margin-bottom:15px; }
        p { line-height:1.6; }
        ul { list-style:none; padding:0; }
        li { background:#fff; margin:10px 0; padding:15px; border-radius:10px; box-shadow: 0 3px 6px rgba(0,0,0,0.1); }
        form input, form textarea {
            width:100%; padding:10px; margin:5px 0; border-radius:8px; border:1px solid #ccc; font-size:16px;
        }
        button {
            padding:12px 20px;
            background:#2575fc; color:#fff; border:none; border-radius:8px;
            cursor:pointer; font-size:16px; transition:0.3s;
        }
        button:hover { background:#6a11cb; transform: scale(1.05); }
    </style>
</head>
<body>
    <header>
        <h1>Swayam Waghmare</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/projects">Projects</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>
    <main>
"""

footer = """
    </main>
    <footer>
        <p>&copy; 2025 Swayam Waghmare | Built with Python & Flask</p>
    </footer>
</body>
</html>
"""

@app.route("/")
@app.route("/")
def home():
    return header + """
    <section style="text-align:center; padding:50px 20px; background: linear-gradient(to right, #f0f4f8, #d9e2ef); border-radius:15px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); margin-bottom:30px;">
        <h1 style="font-size:36px; color:#2575fc; margin-bottom:15px;">Hi, I’m <span style="color:#6a11cb;">Swayam Waghmare</span></h1>
        <p style="font-size:20px; line-height:1.6; color:#333; max-width:800px; margin:auto;">
            I am a <b>BTech AI student</b> at JD College of Engineering & Management, Nagpur, passionate about 
            <span style="color:#6a11cb; font-weight:bold;">Generative AI</span>, 
            <span style="color:#2575fc; font-weight:bold;">Computer Vision</span>, 
            and building <span style="color:#ff6f61; font-weight:bold;">intelligent, real-world solutions</span>.
        </p>
        <p style="font-size:18px; color:#555; max-width:800px; margin:auto; margin-top:20px;">
            Through my projects, I combine creativity with technical expertise, delivering innovative AI solutions that inspire and make an impact. 
            Explore my portfolio to see my work, learnings, and contributions.
        </p>
        <a href="/projects" style="display:inline-block; margin-top:25px; padding:12px 25px; background:#2575fc; color:#fff; text-decoration:none; font-size:18px; border-radius:10px; transition:0.3s;">
            View My Projects
        </a>
    </section>
    """ + footer

@app.route("/about")
def about():
    return header + """
        <h2>Welcome</h2>
<p>Hello 👋 I’m <b>Swayam Waghmare</b>, a BTech student specializing in <span style="color:#6a11cb;">Artificial Intelligence</span> at JD College of Engineering & Management, Nagpur.</p>

<p>I’m passionate about exploring cutting-edge technologies like <span style="color:#2575fc;">Generative AI</span>, <span style="color:#ff6f61;">Computer Vision</span>, and building intelligent systems that solve real-world problems.</p>

<p>Through my projects and experiments, I aim to combine creativity with technical expertise, delivering innovative solutions and sharing knowledge with the community. Dive into my portfolio to see my work, learnings, and contributions.</p>

        <ul>
            <li>10th – Prashant High School</li>
            <li>12th – Rajendra Junior College</li>
            <li>BTech AI – JDCOEM</li>
        </ul>
        <p>I enjoy exploring <span style="color:#6a11cb;">Generative AI</span>, 
        <span style="color:#2575fc;">Computer Vision</span>, and building innovative AI projects.</p>
    """ + footer

@app.route("/projects")
def projects():
    projects_list = [
        "Generative Adversarial Network (GAN) Case Study",
        "AI Image Processing Application",
        "Flask REST API Development",
        "Cybersecurity Internship Report",
        "sack detection using ml and DIP"
    ]
    items = "".join([f"<li>{p}</li>" for p in projects_list])
    return header + f"""
        <h2>Projects</h2>
        <ul>{items}</ul>
    """ + footer

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        user_name = request.form.get("name")
        message = request.form.get("message")
        return header + f"""
            <h2>Contact Me</h2>
            <p>✅ Thanks, <b>{user_name}</b>! Your message has been received.</p>
        """ + footer

    return header + """
        <h2>Contact Me</h2>
        <form method="POST">
            <label>Name:</label><br>
            <input type="text" name="name" required><br><br>

            <label>Message:</label><br>
            <textarea name="message" required></textarea><br><br>

            <button type="submit">Send</button>
        </form>
    """ + footer

if __name__ == "__main__":
    app.run(debug=True)
