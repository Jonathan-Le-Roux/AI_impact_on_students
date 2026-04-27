import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib.cm as cm

def plot_by_category(data, category, ax=None):
    if ax is None:
        ax = plt.gca()

    cat_counts = data[category].value_counts()
    clean_category = category.replace('_', ' ')
    ax.bar(cat_counts.index.astype(str), cat_counts.values,color = 'skyblue')
    ax.set_xlabel(clean_category)
    ax.set_ylabel('Number of Students')
    ax.set_title(f'Distribution of Students by {clean_category}')
    ax.tick_params(axis='x', rotation=45)


def interactive_category_viewer(data, categories):
    current = [0]

    fig, ax = plt.subplots(figsize=(10, 7))
    plt.subplots_adjust(bottom=0.22)

    def show_plot():
        ax.clear()
        plot_by_category(data, categories[current[0]], ax=ax)
        fig.canvas.draw_idle()

    def next_plot(event):
        current[0] = (current[0] + 1) % len(categories)
        show_plot()

    def prev_plot(event):
        current[0] = (current[0] - 1) % len(categories)
        show_plot()

    ax_prev = plt.axes([0.05, 0, 0.1, 0.05])
    ax_next = plt.axes([0.85, 0, 0.1, 0.05])

    btn_prev = Button(ax_prev, 'Previous')
    btn_next = Button(ax_next, 'Next')

    btn_prev.on_clicked(prev_plot)
    btn_next.on_clicked(next_plot)

    fig._btn_prev = btn_prev
    fig._btn_next = btn_next
    fig._show_plot = show_plot

    show_plot()
    plt.show()