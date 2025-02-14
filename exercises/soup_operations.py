import exercises.element_paths as element_paths

def remove_with_selector_if_exists(soup, css_selector):
    elements = soup.css.select(css_selector)
    if len(elements) != 0: elements[0].decompose()
    return soup

def remove_unnecessary_elements(soup):
    # Remove Results Bar if exists
    remove_with_selector_if_exists(soup, element_paths.exercise_results_row_1)
    remove_with_selector_if_exists(soup, element_paths.exercise_results_row_2)
    remove_with_selector_if_exists(soup, element_paths.exercise_results_row_3)

    # Remove Header (ganz oben mit Artemis Zeichen und navbar)
    soup.css.select(element_paths.exercise_navbar_and_upper_stuff)[0].decompose()     

    # remove 'Tasks' part, if exists
    remove_with_selector_if_exists(soup, element_paths.exercise_tasks_row)

    # remove Community Field if exists
    remove_with_selector_if_exists(soup, element_paths.exercise_community_field)

    soup.find('jhi-footer').decompose()# Footer (About, Privacy und so ganz unten)
    
    return soup

def remove_test_icons(soup):
    for fa_icon in soup.find_all("fa-icon", class_="test-icon"):
        fa_icon.decompose()