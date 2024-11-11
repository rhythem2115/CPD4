import csv
import os

# Define paths
meets_folder = "meets"
output_html_path = "index.html"

def generate_meet_links():
    """Generate HTML links for each meet CSV file found in the meets folder."""
    html_links = ""
    for filename in os.listdir(meets_folder):
        if filename.endswith(".csv"):
            meet_name = filename.replace("_", " ").replace(".csv", "")
            html_file = filename.replace(".csv", ".html")
            link = f'<li><a href="{meets_folder}/{html_file}">{meet_name}</a></li>\n'
            html_links += link
    return html_links

def create_index_html():
    """Generate the main index.html file with links to each meet."""
    with open(output_html_path, "w") as file:
        file.write(
            "<!DOCTYPE html>\n"
            "<html lang='en'>\n"
            "<head>\n"
            "<meta charset='UTF-8'>\n"
            "<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
            "<title>Skyline High School Cross Country Meet Results</title>\n"
            "<link rel='stylesheet' href='css/reset.css'>\n"
            "<link rel='stylesheet' href='css/style.css'>\n"
            "<link rel='stylesheet' href='css/homepage.css'>\n"
            "</head>\n"
            "<body>\n"
            "<a class='skip-link' href='#main-content'>Skip to Main Content</a>\n"
            "<header>\n"
            "<h1>Skyline High School Cross Country Meet Results</h1>\n"
            "</header>\n"
            "<nav>\n"
            "<ul>\n"
            f"{generate_meet_links()}"
            "</ul>\n"
            "</nav>\n"
            "<footer>\n"
            "<p>&copy; 2024 Skyline High School Cross Country</p>\n"
            "</footer>\n"
            "</body>\n"
            "</html>"
        )

def create_meet_html(meet_csv_path, meet_html_path, meet_name):
    """Generate an HTML file for a specific meet from its CSV file."""
    with open(meet_csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Assume the first row is headers

        with open(meet_html_path, "w") as htmlfile:
            htmlfile.write(
                "<!DOCTYPE html>\n"
                "<html lang='en'>\n"
                "<head>\n"
                "<meta charset='UTF-8'>\n"
                "<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
                f"<title>{meet_name} Results</title>\n"
                "<link rel='stylesheet' href='../css/reset.css'>\n"
                "<link rel='stylesheet' href='../css/style.css'>\n"
                "</head>\n"
                "<body>\n"
                "<header>\n"
                "<nav>\n"
                "<a href='../index.html' class='button'>Home Page</a>\n"  # Updated link
                "<a href='#summary' class='button'>Summary</a>\n"
                "<a href='#team-results' class='button'>Team Results</a>\n"
                "<a href='#individual-results' class='button'>Individual Results</a>\n"
                "<a href='#gallery' class='button'>Gallery</a>\n"
                "</nav>\n"
                f"<h1>{meet_name}</h1>\n"
                "<p>Thu Aug 29 2024</p>\n"
                "</header>\n"
                "<main>\n"
                "<section id='summary'>\n"
                "<h2 class='section-title'>Race Summary</h2>\n"
                "<p>The Skyline team performed admirably at the {meet_name}. Additional race summary content can go here.</p>\n"
                "</section>\n"
                "<section id='team-results'>\n"
                "<h2 class='section-title'>Team Results</h2>\n"
                "<table>\n"
                "<thead>\n"
                "<tr>\n"
            )

            # Write headers
            for header in headers:
                htmlfile.write(f"<th>{header}</th>")
            htmlfile.write("</tr>\n</thead>\n<tbody>\n")

            # Write data rows
            for row in reader:
                htmlfile.write("<tr>\n")
                for cell in row:
                    htmlfile.write(f"<td>{cell}</td>")
                htmlfile.write("</tr>\n")

            htmlfile.write("</tbody>\n</table>\n</section>\n")

            # Individual Results Section
            htmlfile.write(
                "<section id='individual-results'>\n"
                "<h2 class='section-title'>Individual Results</h2>\n"
                "<div class='individual-results'>\n"
            )

            # Reset CSV reader and skip header row again for individual results
            csvfile.seek(0)
            next(reader)

            for row in reader:
                name, place, time, grade = row  # Adjust based on actual CSV structure
                htmlfile.write(
                    "<div class='individual-result'>\n"
                    f"<img src='../images/profiles/{name.replace(' ', '_')}.jpg' alt='{name}'>\n"
                    "<div>\n"
                    f"<p><strong>Name:</strong> {name}</p>\n"
                    f"<p><strong>Place:</strong> {place}</p>\n"
                    f"<p><strong>Time:</strong> {time}</p>\n"
                    f"<p><strong>Grade:</strong> {grade}</p>\n"
                    "</div>\n"
                    "</div>\n"
                )

            htmlfile.write("</div>\n</section>\n</main>\n<footer>\n"
                           "<p>&copy; 2024 Skyline High School Cross Country</p>\n"
                           "</footer>\n</body>\n</html>")

def generate_all_meets():
    """Generate HTML files for all meets and create the main index.html."""
    if not os.path.exists(meets_folder):
        os.makedirs(meets_folder)

    # Generate each meet HTML page
    for filename in os.listdir(meets_folder):
        if filename.endswith(".csv"):
            meet_name = filename.replace("_", " ").replace(".csv", "")
            meet_csv_path = os.path.join(meets_folder, filename)
            meet_html_path = os.path.join(meets_folder, filename.replace(".csv", ".html"))
            create_meet_html(meet_csv_path, meet_html_path, meet_name)
   
    # Generate the main index HTML with links to each meet
    create_index_html()

if __name__ == "__main__":
    generate_all_meets()