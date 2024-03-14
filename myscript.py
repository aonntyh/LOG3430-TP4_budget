import os
os.system("git bisect start 6cc5ae52e512d29c44004c4803f1316b1fb0f916 c1a4be04b972b6c17db242fc37752ad517c29402")
os.system("git bisect run python3 manage.py test")
os.system("git bisect reset")