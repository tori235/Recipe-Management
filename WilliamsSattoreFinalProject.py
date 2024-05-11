import tkinter as tk
from tkinter import messagebox

class RecipeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Recipe Management Application")
        self.geometry("400x300")

        self.current_window = None

        self.main_menu()

    def main_menu(self):
        if self.current_window:
            self.current_window.destroy()

        self.current_window = tk.Frame(self)
        self.current_window.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(self.current_window, text="Recipe Management Application")
        label.pack(pady=10)

        button_create_recipe = tk.Button(self.current_window, text="Create Recipe", command=self.create_recipe)
        button_create_recipe.pack()

        button_view_recipes = tk.Button(self.current_window, text="View Recipes", command=self.view_recipes)
        button_view_recipes.pack()

        button_exit = tk.Button(self.current_window, text="Exit", command=self.exit_app)
        button_exit.pack()

    def create_recipe(self):
        if self.current_window:
            self.current_window.destroy()

        self.current_window = tk.Frame(self)
        self.current_window.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(self.current_window, text="Create Recipe")
        label.pack(pady=10)

        entry_name = tk.Entry(self.current_window)
        entry_name.pack()

        def save_recipe():
            recipe_name = entry_name.get()
            if not recipe_name:
                messagebox.showerror("Error", "Recipe name cannot be empty")
            else:
                messagebox.showinfo("Success", f"Recipe '{recipe_name}' created successfully")

        button_save = tk.Button(self.current_window, text="Save Recipe", command=save_recipe)
        button_save.pack()

        button_back = tk.Button(self.current_window, text="Back", command=self.main_menu)
        button_back.pack()

    def view_recipes(self):
        if self.current_window:
            self.current_window.destroy()

        self.current_window = tk.Frame(self)
        self.current_window.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(self.current_window, text="View Recipes")
        label.pack(pady=10)

        # Placeholder for viewing recipes
        label_placeholder = tk.Label(self.current_window, text="No recipes available")
        label_placeholder.pack()

        button_back = tk.Button(self.current_window, text="Back", command=self.main_menu)
        button_back.pack()

    def exit_app(self):
        self.destroy()

if __name__ == "__main__":
    app = RecipeApp()
    app.mainloop()
