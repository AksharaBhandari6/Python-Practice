# sudoku-solver
my dear sudoku solver :D #project2


-----------INSPO----------------
🔍 “Sudoku Solver – Because Solving by Hand is Overrated”

Recently, I challenged myself with something… unnecessary, overkill, and extremely fun:
Building a real-time Sudoku solver using just my webcam, deep learning, and a lot of CPU patience.
 (Yep, no GPU. Just me, my overworked CPU, and a very forgiving fan. 🔥💻)

😅 Why I did this:

I could’ve just picked up a pen and solved the puzzle like a normal human.
 But where’s the fun in that?
Instead, I built a system that:
🔹 Captures a Sudoku puzzle live from my webcam
🔹 Detects and straightens the grid using OpenCV (after hours of trial and error)
🔹 Recognizes digits using a CNN trained on MNIST
🔹 Solves the puzzle using a custom Python backtracking algorithm
🔹 Overlays the solution onto the original video feed — in real time

🧠 Tech Stack I used:

⚙️ Python – the hero of all things automation
⚙️ OpenCV – for contour detection, image processing, and camera control
⚙️ TensorFlow + Keras – to train and load the digit recognizer (on CPU, painfully slow)
⚙️ NumPy – to juggle arrays and logic
⚙️ cv2.VideoWriter – to record the chaos as proof

😂 Things that broke (and made me stronger):

💥 My CPU (almost filed for burnout)
💥 Lighting — apparently the mortal enemy of consistent grid detection
💥 The model mistaking blank cells for digits (and vice versa, of course)
💥 Perspective warping — the true boss level of this entire project

💡 What I learned:

📘 Real-time computer vision + ML is doable on CPU — just keep snacks nearby
📘 Combining CNNs, classic backtracking, and OpenCV is incredibly satisfying
📘 Debugging transforms will test your patience, but build your character

Honestly, building this was both chaotic and fulfilling.
 It reminded me that even without the latest hardware, you can still build cool, smart stuff — if you’re stubborn enough 😎

