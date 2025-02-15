import turtle
import pandas as pd

#screen setup
screen = turtle.Screen()
screen.title("India State Guessing Game")
image = "India_map.gif"
screen.addshape(image)
turtle.shape(image)

# Turtle for writing on the map
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# Read CSV data
data = pd.read_csv("28_states.csv")
us_states = data["state"].str.title()  # Standardize state names
guessed_states = []
not_guessed_states = set(us_states)


# Game loop
while len(guessed_states) < 28:
    ans = screen.textinput(title=f"{len(guessed_states)}/28 States Correct",
                           prompt="What's the state's name?").strip().title()

    if ans == "Exit":
        # Mark all unguessed states in red
        for state in not_guessed_states:
            state_data = data[data["state"].str.title() == state]
            x, y = state_data["x"].iloc[0], state_data["y"].iloc[0]
            pen.goto(x, y)
            pen.pencolor("red")
            pen.write(arg=state, align="center")
        # Save remaining states to CSV
        pd.DataFrame(not_guessed_states, columns=["state"]).to_csv("Not_guessed_US_state.csv", index=False)
        break

    if ans in not_guessed_states:
        guessed_states.append(ans)
        not_guessed_states.remove(ans)
        state_data = data[data["state"].str.title() == ans]
        x, y = state_data["x"].iloc[0], state_data["y"].iloc[0]
        pen.goto(x, y)
        pen.pencolor("black")
        pen.write(arg=ans, align="center")


screen.exitonclick()

