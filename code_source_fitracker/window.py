import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import random
from PIL import Image, ImageTk
def return_to_menu():
    food_frame.pack_forget()
    activity_frame.pack_forget()
    button_frame.pack(expand=True, fill=tk.BOTH)

CALORIE_GOAL_LIMIT = 4000  # Default value
PROTEIN_GOAL = 180  # Default value
FAT_GOAL = 80  # Default value
CARBS_GOAL = 300  # Default value

today = []

def add_food():
    name = name_entry.get()
    calories = int(calories_entry.get())
    protein = int(protein_entry.get())
    fat = int(fat_entry.get())
    carbs = int(carbs_entry.get())


    food = {'name': name, 'calories': calories, 'protein': protein, 'fat': fat, 'carbs': carbs}
    today.append(food)

    messagebox.showinfo("Food Added", "Food successfully added to today's list.")

def visualize_progress():
    if not today:
        messagebox.showwarning("No Data", "No data available to visualize.")
        return

    fig, axs = plt.subplots(2, 2)

    # Plot 1: Nutrients Distribution
    nutrients_labels = ['Proteins', 'Fats', 'Carbs']
    nutrients_values = [sum(food['protein'] for food in today),
                        sum(food['fat'] for food in today),
                        sum(food['carbs'] for food in today)]
    explode = (0.1, 0.1, 0.1) 
    axs[0, 0].pie(nutrients_values, labels=nutrients_labels, autopct='%1.1f%%',explode=explode,shadow=True)
    axs[0, 0].set_title('Nutrients Distribution')

    # Plot 2: Nutrients Goal Progress
    goal_values = [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL]
    axs[0, 1].bar(nutrients_labels, nutrients_values, label='Consumed')
    axs[0, 1].bar(nutrients_labels, goal_values, label='Goal')
    axs[0, 1].legend()
    axs[0, 1].set_title('Nutrients Goal Progress')

    # Plot 3: Calories Goal Remaining
    calories_consumed = sum(food['calories'] for food in today)
    calories_goal_remaining = max(0, CALORIE_GOAL_LIMIT - calories_consumed)
    axs[1, 0].pie([calories_consumed, calories_goal_remaining],
                  labels=['Calories', 'Remaining'], autopct='%1.1f%%')
    axs[1, 0].set_title('Calories Goal Remaining')

    # Plot 4: Calories vs Weight
    fig.tight_layout()

    # Create a new window for visualization
    visualization_window = tk.Toplevel()
    visualization_window.title("Visualization")

    # Embed the matplotlib plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=visualization_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def edit_goals():
    edit_goals_window = tk.Toplevel()
    edit_goals_window.title("Edit Goals")
    edit_goals_window.geometry("400x300")

    # Labels
    tk.Label(edit_goals_window, text="Calorie Goal Limit:",font=('Arial', 14, 'bold')).grid(row=0, column=0)
    tk.Label(edit_goals_window, text="Protein Goal:",font=('Arial', 14, 'bold')).grid(row=1, column=0)
    tk.Label(edit_goals_window, text="Fat Goal:",font=('Arial', 14, 'bold')).grid(row=2, column=0)
    tk.Label(edit_goals_window, text="Carbs Goal:",font=('Arial', 14, 'bold')).grid(row=3, column=0)

    # Entries
    calorie_goal_entry = tk.Entry(edit_goals_window,font=('Arial', 12))
    calorie_goal_entry.grid(row=0, column=1)
    calorie_goal_entry.insert(0, str(CALORIE_GOAL_LIMIT))

    protein_goal_entry = tk.Entry(edit_goals_window,font=('Arial', 12))
    protein_goal_entry.grid(row=1, column=1)
    protein_goal_entry.insert(0, str(PROTEIN_GOAL))

    fat_goal_entry = tk.Entry(edit_goals_window,font=('Arial', 12))
    fat_goal_entry.grid(row=2, column=1)
    fat_goal_entry.insert(0, str(FAT_GOAL))

    carbs_goal_entry = tk.Entry(edit_goals_window,font=('Arial', 12))
    carbs_goal_entry.grid(row=3, column=1)
    carbs_goal_entry.insert(0, str(CARBS_GOAL))

    # Button
    save_button = tk.Button(edit_goals_window, text="Save Goals",font=("Helvetica", 14),
                            command=lambda: save_goals(calorie_goal_entry, protein_goal_entry,
                                                        fat_goal_entry, carbs_goal_entry))
    save_button.grid(row=4, column=0, columnspan=2)

def save_goals(calorie_goal_entry, protein_goal_entry, fat_goal_entry, carbs_goal_entry):
    global CALORIE_GOAL_LIMIT, PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL
    CALORIE_GOAL_LIMIT = int(calorie_goal_entry.get())
    PROTEIN_GOAL = int(protein_goal_entry.get())
    FAT_GOAL = int(fat_goal_entry.get())
    CARBS_GOAL = int(carbs_goal_entry.get())

    messagebox.showinfo("Goals Saved", "Goals successfully updated.")






app = tk.Tk()
food_frame=tk.Frame(app,bg="#539afc")
image_food_frame=tk.Frame(food_frame,width=800 ,height=650)
image_food_frame.place(x=400,y=0)

food_frame_image = Image.open("delicious-cartoon-style-fast-food.jpg")  
food_frame_image_resized = food_frame_image.resize((800,650))
food_frame_image = ImageTk.PhotoImage(food_frame_image_resized)

back_food_image= tk.Label(image_food_frame, image=food_frame_image)
back_food_image.place(x=0, y=0, relwidth=1, relheight=1)




app.title("Calorie Tracker App")
app.geometry("1200x650")




# Food Tracker Tab
food_tracker_frame = tk.Frame(food_frame,width=200,height=200,bg="#539afc")
food_tracker_frame.place(x=20,y=150)


# Labels
tk.Label(food_tracker_frame, text="Name",bg="#539afc",font=('Arial', 14, 'bold')).grid(row=0, column=0)
tk.Label(food_tracker_frame, text="Calories",bg="#539afc",font=('Arial', 14, 'bold')).grid(row=1, column=0)
tk.Label(food_tracker_frame, text="Protein",bg="#539afc",font=('Arial', 14, 'bold')).grid(row=2, column=0)
tk.Label(food_tracker_frame, text="Fat",bg="#539afc",font=('Arial', 14, 'bold')).grid(row=3, column=0)
tk.Label(food_tracker_frame, text="Carbs",bg="#539afc",font=('Arial', 14, 'bold')).grid(row=4, column=0)

# Entries
name_entry = tk.Entry(food_tracker_frame, font=('Arial', 14))

name_entry.grid(row=0, column=1)

calories_entry = tk.Entry(food_tracker_frame,font=('Arial', 14))
calories_entry.grid(row=1, column=1)

protein_entry = tk.Entry(food_tracker_frame,font=('Arial', 14))
protein_entry.grid(row=2, column=1)

fat_entry = tk.Entry(food_tracker_frame,font=('Arial', 14))
fat_entry.grid(row=3, column=1)

carbs_entry = tk.Entry(food_tracker_frame,font=('Arial', 14))
carbs_entry.grid(row=4, column=1)

# Button
add_food_button = tk.Button(food_tracker_frame, text="Add Food",bg="#1275b3",font=("Helvetica", 14) ,command=add_food)
add_food_button.grid(row=6, column=0, columnspan=2)

# Buttons
goal_image = Image.open("objectifs.png")  
goal_image_resized = goal_image.resize((24, 24))
goal_icon_image = ImageTk.PhotoImage(goal_image_resized)

analyse_image = Image.open("une-analyse.png")  
analyse_image_resized = analyse_image.resize((24, 24))
analyse_icon_image = ImageTk.PhotoImage(analyse_image_resized)



menu_image = Image.open("menu.png")  # Replace "fast-food.png" with the path to your image file
menu_image_resized = menu_image.resize((20, 20))
menu_icon_image = ImageTk.PhotoImage(menu_image_resized)


visualize_button = tk.Button(food_frame, text="  Visualize Progress",bg="#1275b3",font=("Helvetica", 14) ,height=40,image=analyse_icon_image, compound=tk.LEFT , command=visualize_progress)
visualize_button.place(x=10,y=400)

edit_goals_button = tk.Button(food_frame, text="  Edit Goals",bg="#1275b3",font=("Helvetica", 14) ,height=40,image=goal_icon_image, compound=tk.LEFT , command=edit_goals)
edit_goals_button.place(x=230,y=400)

food_btn_return_menu=tk.Button(food_frame,text="  Return to Menu", bg="#7df5e5",font=("Helvetica", 16) ,image=menu_icon_image, compound=tk.LEFT ,command=return_to_menu)
food_btn_return_menu.place(x=0, y=0)




###########################################################################################""""

# Load the dataset
df = pd.read_csv("exercise_dataset.csv")

# Function to convert weight from kg to lb
def kg_to_lb(weight_kg):
    return weight_kg * 2.20462

# Function to find the nearest weight
def find_nearest_weight(weight):
    weights = [130, 155, 180, 205]  # Possible weight values in the dataset
    return min(weights, key=lambda x: abs(x - weight))

# Function to handle button click event
def on_button_click():
    try:
        # Get the weight entered by the user in kg
        weight_kg = float(entry.get())
        # Convert weight to pounds
        weight_lb = kg_to_lb(weight_kg)
        # Find the nearest weight in the dataset
        nearest_weight = find_nearest_weight(weight_lb)
        # Plot both graphs
        plot_both_graphs(nearest_weight)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Function to plot both graphs
def plot_both_graphs(weight):
    # Select a random subset of 50 activities
    random_activities = random.sample(df['Activity, Exercise or Sport (1 hour)'].tolist(), 50)
    # Filter the dataset to include only the selected activities
    filtered_df = df[df['Activity, Exercise or Sport (1 hour)'].isin(random_activities)]

    # Create a new window for the graphs
    graph_window = tk.Toplevel(app)
    graph_window.title("Calories Burned Graphs")

    # Plot the first graph (larger)
    fig1, ax1 = plt.subplots(figsize=(10, 8))
    ax1.bar(filtered_df['Activity, Exercise or Sport (1 hour)'], filtered_df[str(weight) + ' lb'], color='skyblue')
    ax1.set_xlabel('Activity')
    ax1.set_ylabel('Calories Burned')
    ax1.set_title('Calories Burned for Weight ' + str(entry.get()) + ' KG (Random Subset of 50 Activities)')
    ax1.tick_params(axis='x', rotation=90,labelsize=12)
    plt.tight_layout()

    # Plot the second graph (smaller)
    weight_df = df[['Activity, Exercise or Sport (1 hour)', str(weight) + ' lb']]
    sorted_df = weight_df.sort_values(by=str(weight) + ' lb', ascending=False)
    top_10_activities = sorted_df.head(10)
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    ax2.barh(top_10_activities['Activity, Exercise or Sport (1 hour)'],
             top_10_activities[str(weight) + ' lb'], color='skyblue')
    ax2.set_xlabel('Calories Burned')
    ax2.set_ylabel('Activity')
    ax2.set_title(f'Top 10 Activities for Burned Calories (Weight: {entry.get()} KG)', fontsize=8)
    ax2.invert_yaxis()  # Invert y-axis to display the highest calories burned at the top
    ax2.tick_params(axis='y', labelsize=7)  # Adjust font size of y-axis labels
    plt.tight_layout()

    # Create canvas for the first graph
    canvas1 = FigureCanvasTkAgg(fig1, master=graph_window)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    # Create canvas for the second graph
    canvas2 = FigureCanvasTkAgg(fig2, master=graph_window)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)


# Create a frame for weight input and button
activity_frame = tk.Frame(app)
ifos_activity_frame=tk.Frame(activity_frame,width=300,height=650,bg="#53cafc")
ifos_activity_frame.place(x=0,y=0)
image_frame_activity=tk.Frame(activity_frame,width=900,height=650)
image_frame_activity.place(x=300,y=0)

activity_image_frame= Image.open("20944529.jpg")  
activity_image_frame_resized = activity_image_frame.resize((900, 650))
activity_image_frame = ImageTk.PhotoImage(activity_image_frame_resized)
back_activity_image= tk.Label(image_frame_activity, image=activity_image_frame)
back_activity_image.place(x=0, y=0, relwidth=1, relheight=1)


kg_image_icon = Image.open("cuisine.png")  
kg_image_icon_resized = kg_image_icon.resize((40, 40))
kg_image_icon = ImageTk.PhotoImage(kg_image_icon_resized)


label = tk.Label(ifos_activity_frame, text="Enter your weight (in kg):",font=('Arial', 14, 'bold'),image=kg_image_icon,compound=tk.RIGHT,bg="#53cafc")
label.place(x=10, y=70)
entry = tk.Entry(ifos_activity_frame,font=('Arial', 16),bg="#3d9cc4")
entry.place(x=10,y=130)


button = tk.Button(ifos_activity_frame, text=" Generate Graphs",bg="#3d9cc4",font=("Helvetica", 16),image=analyse_icon_image, compound=tk.LEFT , command=on_button_click)
button.place(x=10,y=200)

activity_btn_return_menu=tk.Button(ifos_activity_frame,text="Return to Menu", bg="#7df5e5",font=("Helvetica", 16) ,image=menu_icon_image, compound=tk.LEFT ,command=return_to_menu)
activity_btn_return_menu.place(x=0,y=0)






def open_food_tracker():
  
    button_frame.pack_forget()
    food_frame.pack(expand=True, fill=tk.BOTH)

def open_activity_tracker():
   
    button_frame.pack_forget()
    activity_frame.pack(expand=True, fill=tk.BOTH)
def return_to_menu():
    food_frame.pack_forget()
    activity_frame.pack_forget()
    button_frame.pack(expand=True, fill=tk.BOTH)


# Create the main window

button_frame=tk.Frame(app,bg="#119189")
button_frame.pack(expand=True, fill=tk.BOTH)
image_frame=tk.Frame(button_frame,width=800,height=650)
image_frame.place(x=400,y=0)
image = Image.open("3864158.jpg")  
photo = ImageTk.PhotoImage(image)
resized_image = image.resize((800, 650))
photo = ImageTk.PhotoImage(resized_image)
background_label = tk.Label(image_frame, image=photo)

background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Create buttons for food and activity trackers
food_image = Image.open("fast-food.png") 
food_image_resized = food_image.resize((30, 30))
food_icon_image = ImageTk.PhotoImage(food_image_resized)

activity_image = Image.open("sport.png")  
activity_image_resized = activity_image.resize((30, 30))
activity_icon_image = ImageTk.PhotoImage(activity_image_resized)

food_button = tk.Button(button_frame, text=" Food Tracker ",width=350,bg="#7df5e5",font=("Helvetica", 30),image=food_icon_image, compound=tk.LEFT ,command=open_food_tracker)
food_button.place(x=20,y=150)

activity_button = tk.Button(button_frame, text=" Activity Tracker ",width=350,bg="#7df5e5",font=("Helvetica", 30),image=activity_icon_image, compound=tk.LEFT ,command=open_activity_tracker)
activity_button.place(x=20,y=300)



app.mainloop()
