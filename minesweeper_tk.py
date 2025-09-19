"""
Authors: Katie Nordberg, Christina Sorensen, Navya Nittala, Vi Lara, and Kundana Dongala
Program Name: playMinesweeper.py
Description:
    Tkinter UI for a Minesweeper game.

    This file builds a GUI with:
    - A toolbar (mines-remaining label, New…, Reset)
    - A clickable grid of Buttons (one per board cell)
    - Mouse interactions: left-click to uncover, right-click to flag
    - Win/Lose handling and full-board rerendering after each action
Input: None (all parameters hardcoded or via simple dialog)
Output: A playable Minesweeper game window
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
from functools import partial

from Classes.minesweeper import BoardManager

# Window + general colors
BG_COLOR       = "#d182a0"   # soft pink (window / background)
FG_COLOR       = "#eac7a5"   # beige text

# Buttons + entries
BTN_BG         = "#8c5a5a"   # muted brown buttons
BTN_FG         = "#eac7a5"   # beige button text
ENTRY_BG       = "#ffffff"   # white entry background
ENTRY_FG       = "#000000"   # black entry text

# Cell state backgrounds
COVERED_BG     = "#e0a5b0"   # lighter pink for covered cells
FLAG_BG        = "#b37b7b"   # brownish pink for flagged cells
UNCOVERED_BG   = "#f2d2d7"   # pale pink for uncovered cells
MINE_BG        = "#ffebee"   # light red/pink when a mine is revealed
DISABLED_FG    = "#3b2e2e"   # dark text on uncovered cells

# Mapping of number -> text color for uncovered numeric cells
NUMBER_COLORS = {
    0: "#e0a5b0",
    1: "#1976d2",
    2: "#388e3c",
    3: "#d32f2f",
    4: "#7b1fa2",
    5: "#5d4037",
    6: "#00838f",
    7: "#455a64",
    8: "#000000",
}

class MinesweeperApp(tk.Tk):
    """Main application window for Minesweeper.

    Builds the toolbar, grid of buttons, wires up mouse events, and
    syncs the UI with the backend state via update_view().
    """

    def __init__(self, rows=10, cols=10, mines=10):
        super().__init__()
        self.title("Minesweeper")
        self.configure(bg=BG_COLOR)

        # Create the game using BoardManager (backend model)
        self.game = BoardManager(rows, cols, mines)

        #Toolbar (top)
        self.toolbar = tk.Frame(self, padx=8, pady=6, bg=BG_COLOR)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Mines remaining label (derived as total mines - current flag count)
        self.mine_label = tk.Label(
            self.toolbar,
            text=self._mine_label_text(),
            font=("Helvetica", 12, "bold"),
            fg=FG_COLOR,
            bg=BG_COLOR,
        )
        self.mine_label.pack(side=tk.LEFT)

        # Reset button: restart with same rows/cols/mines
        self.reset_btn = tk.Button(
            self.toolbar,
            text="Reset",
            command=self.reset_game,
            bg=BTN_BG, fg=BTN_FG,
            activebackground=BTN_BG, activeforeground=BTN_FG,
        )
        self.reset_btn.pack(side=tk.RIGHT, padx=(4, 0))

        # New… button: open dialog to choose a new mine count (fixed 10x10)
        self.new_btn = tk.Button(
            self.toolbar,
            text="New…",
            command=self.new_game_dialog,
            bg=BTN_BG, fg=BTN_FG,
            activebackground=BTN_BG, activeforeground=BTN_FG,
        )
        self.new_btn.pack(side=tk.RIGHT, padx=(4, 8))

        # Grid container (center) 
        self.grid_frame = tk.Frame(self, padx=10, pady=10, bg=BG_COLOR)
        self.grid_frame.pack()

        # Build 2D list of Buttons mirroring the backend board dimensions
        self.buttons = [
            [self._make_cell_button(r, c) for c in range(self.game.cols)]
            for r in range(self.game.rows)
        ]

        # Add column labels (A–J) to the grid frame
        for c in range(self.game.cols):
            tk.Label(
                self.grid_frame,
                text=chr(65 + c),  # Convert column index to letter (A–J)
                font=("Helvetica", 12, "bold"),
                bg=BG_COLOR,
                fg=FG_COLOR,
            ).grid(row=0, column=c + 1, padx=5, pady=5)

        # Add row labels (1–10) to the grid frame
        for r in range(self.game.rows):
            tk.Label(
                self.grid_frame,
                text=str(r + 1),  # Convert row index to number (1–10)
                font=("Helvetica", 12, "bold"),
                bg=BG_COLOR,
                fg=FG_COLOR,
            ).grid(row=r + 1, column=0, padx=5, pady=5)

        # Initial paint to reflect the fresh backend state
        self.update_view()

    # UI helpers
    def _make_cell_button(self, r, c):
        """Create a single cell Button, place it in the grid, and bind events.

        Left-click uncovers, right-click flags. Styling starts as 'covered'.
        """
        b = tk.Button(
            self.grid_frame,
            width=3, height=1,
            text="",
            relief=tk.RAISED,
            font=("Helvetica", 12, "bold"),
            bg=COVERED_BG, fg=FG_COLOR,
            activebackground=COVERED_BG, activeforeground=FG_COLOR,
        )
        b.grid(row=r+1, column=c+1, padx=1, pady=1, sticky="nsew")

        # Mouse interactions
        b.bind("<Button-1>", partial(self.on_left_click, r, c))   # uncover
        b.bind("<Button-3>", partial(self.on_right_click, r, c))  # flag toggle
        #  macOS: Ctrl+Click as right-click
        # b.bind("<Control-Button-1>", partial(self.on_right_click, r, c))

        return b

    def _mine_label_text(self):
        """Compute the label text for 'mines remaining'.

        Remaining = total mines - number of flagged cells.
        Note: This is a player aid; it can be 'wrong' if flags are misplaced.
        """
        flags = sum(
            1 for r in range(self.game.rows) for c in range(self.game.cols)
            if self.game.boardState[r][c] == 1
        )
        remaining = self.game.mines - flags
        return f"Mines: {remaining} / {self.game.mines}"

    def new_game_dialog(self):
        """Open a simple prompt to choose a new mine count (10–20).

        Rebuilds the backend and the grid while keeping the 10x10 size.
        """
        try:
            mines = simpledialog.askinteger(
                "New Game",
                "Number of mines (10–20):",
                minvalue=10, maxvalue=20, parent=self,
            )
            if mines is None:
                return  # user cancelled
            self.game = BoardManager(10, 10, mines)
            self._rebuild_grid()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def reset_game(self):
        """Reset the game with the SAME rows/cols/mines as current state."""
        self.game = BoardManager(self.game.rows, self.game.cols, self.game.mines)
        self.title("Minesweeper")
        self._rebuild_grid()

    def _rebuild_grid(self):
        """Destroy all cell Buttons and recreate them cleanly.

        This avoids stale button configuration and ensures event bindings and
        visual state start fresh.
        """
        # Remove old buttons from the grid
        for row in self.buttons:
            for b in row:
                b.destroy()

        # Rebuild based on the new backend dimensions
        self.buttons = [
            [self._make_cell_button(r, c) for c in range(self.game.cols)]
            for r in range(self.game.rows)
        ]
        self.update_view()

    # Event handlers
    def on_left_click(self, r, c, event):
        """Handle uncover action.

        - If flagged, ignore.
        - Attempt to uncover the cell via backend.
        - If a mine is uncovered, reveal all, show Game Over, and disable.
        - If the cell is a 0 (empty), attempt flood-fill with expandOpenCells.
        - Repaint and check for win state.

        Button-1 = left mouse click
        Button-3 = right mouse click (on Mac, usually two-finger tap)
        """
        self.title("Playing")

        # Ignore uncover attempts on flagged cells
        if self.game.boardState[r][c] == 1:
            return

        # Ask backend to uncover
        self.game.uncoverCell(r, c)

        # If it’s a mine and not flagged, game over
        if not self.game.isFlagged(r, c) and self.game.isMine(r, c):
            self._reveal_all_mines()
            self.title("Game Over")
            self.update_view()
            messagebox.showinfo("BOOM!", "Game Over.")
            self._disable_all()
            self.reset_game()
            return

        try:
            if self.game.boardContent[r][c] == 0:
                self.game.expandOpenCells(r, c, True)
        except Exception:
            # Guard against incomplete backend flood-fill implementation
            pass

        # Refresh the UI and evaluate win condition
        self.update_view()
        if self._check_win():
            self.title("You Win!")
            messagebox.showinfo("🎉 You Win!", "You cleared all safe cells!")
            self._disable_all()
            self.reset_game()

    def on_right_click(self, r, c, event):
        """Handle flag/unflag action, then repaint."""
        # if self.game.boardState[r][c] == 2:
        #     return
        self.game.flagCell(r, c)
        self.update_view()

    # Rendering / Sync
    def update_view(self):
        """Synchronize the visual grid with the backend's boardState/content."""
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                btn = self.buttons[r][c]
                state = self.game.boardState[r][c]

                if state == 0:  # covered
                    btn.config(
                        text="",
                        relief=tk.RAISED,
                        state=tk.NORMAL,
                        bg=COVERED_BG,
                        fg=FG_COLOR,
                        activebackground=COVERED_BG,
                        activeforeground=FG_COLOR,
                    )
                elif state == 1:  # flagged
                    btn.config(
                        text="F",
                        relief=tk.RAISED,
                        state=tk.NORMAL,
                        bg=FLAG_BG,
                        fg=FG_COLOR,
                        activebackground=FLAG_BG,
                        activeforeground=FG_COLOR,
                    )
                elif state == 2:  # uncovered
                    btn.config(
                        relief=tk.SUNKEN,
                        state=tk.DISABLED,
                        bg=UNCOVERED_BG,
                        fg=DISABLED_FG,
                    )
                    if self.game.isMine(r, c):
                        # Show a mine
                        btn.config(text="X", disabledforeground="#d32f2f", bg=MINE_BG)
                    else:
                        # Show adjacent-mine count if > 0; otherwise leave empty
                        n = self.game.boardContent[r][c]
                        btn.config(
                            text=str(n),
                            disabledforeground=NUMBER_COLORS.get(n, DISABLED_FG),
                        )


        # Update mines-remaining label after any state changes
        self.mine_label.config(text=self._mine_label_text(), fg=FG_COLOR, bg=BG_COLOR)
        self.update_idletasks()

    def _reveal_all_mines(self):
        """Force all mines to appear as uncovered in boardState (for rendering)."""
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                if self.game.isMine(r, c):
                    self.game.boardState[r][c] = 2  # mark as uncovered

    def _disable_all(self):
        """Disable all cell buttons (used after win/lose)."""
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                self.buttons[r][c].config(state=tk.DISABLED)

    def _check_win(self):
        """Return True if all non-mine cells are uncovered, else False."""
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                if not self.game.isMine(r, c) and self.game.boardState[r][c] != 2:
                    return False
        return True


if __name__ == "__main__":

    class MineCountDialog(tk.Tk):
        """Simple one-shot dialog to ask for the number of mines.

        Keeps look & feel consistent with the main app.
        """
        def __init__(self):
            super().__init__()
            self.title("Minesweeper")
            self.configure(bg=BG_COLOR)
            self.resizable(False, False)
            self.geometry("400x400")

            # Centered container
            frame = tk.Frame(self, bg=BG_COLOR)
            frame.place(relx=0.5, rely=0.5, anchor="center")

            # Title label
            tk.Label(
                frame,
                text="MINESWEEPER",
                font=("Helvetica", 24, "bold"),
                fg=FG_COLOR,
                bg=BG_COLOR,
            ).pack(pady=(0, 20))

            # Prompt text
            tk.Label(
                frame,
                text="Enter number of mines (10–20)",
                font=("Helvetica", 12),
                fg=FG_COLOR,
                bg=BG_COLOR,
            ).pack(pady=(0, 10))

            # Numeric entry field
            self.entry = tk.Entry(
                frame,
                font=("Helvetica", 14),
                justify="center",
                bg=ENTRY_BG,
                fg=ENTRY_FG,
                width=10,
            )
            self.entry.pack(pady=10)
            self.entry.focus_set()

            # Submit button
            tk.Button(
                frame,
                text="PLAY",
                font=("Helvetica", 12, "bold"),
                bg=BTN_BG,
                fg=BTN_FG,
                activebackground=BTN_BG,
                activeforeground=BTN_FG,
                command=self.submit,
            ).pack(pady=20)

            self.result = None  # will hold the validated int or remain None

        def submit(self):
            """Validate integer in [10, 20]; store in self.result or show error."""
            try:
                val = int(self.entry.get())
                if 10 <= val <= 20:
                    self.result = val
                    self.destroy()
                else:
                    messagebox.showerror("Invalid", "Enter a number 10-20")
            except ValueError:
                messagebox.showerror("Invalid", "Please enter a valid integer")

    # Launch the dialog to collect a mine count
    dialog = MineCountDialog()
    dialog.mainloop()

    # Use dialog result if provided; default to 10 if user closes/cancels
    mines = dialog.result if dialog.result else 10

    # Create and run the main game window
    app = MinesweeperApp(rows=10, cols=10, mines=mines)
    app.mainloop()
