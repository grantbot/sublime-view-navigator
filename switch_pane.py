import sublime
import sublime_plugin


class NavigatePaneCommand(sublime_plugin.TextCommand):
    """Navigates panes within window"""
    def run(self, edit, direction):
        current_window, current_view = get_current_window_and_view(self)
        group_index, _ = current_window.get_view_index(current_view)
        current_window.focus_group(group_index + direction)


class NavigateViewCommand(sublime_plugin.TextCommand):
    """Navigates views within active pane"""
    def run(self, edit, direction):
        current_window, current_view = get_current_window_and_view(self)
        group_index, view_index = current_window.get_view_index(current_view)
        views_in_group = current_window.views_in_group(group_index)
        current_window.focus_view(views_in_group[(view_index + direction)
                                  % len(views_in_group)])

def get_current_window_and_view(self):
    current_window = self.view.window()
    current_view = current_window.active_view()
    return (current_window, current_view)


