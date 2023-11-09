from fpdf import FPDF
# import fpdf

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        img_width = 190  # Width of the image
        img_height = 220  # Height of the image
        page_width = self.w
        page_height = self.h
        x = (page_width - img_width) / 2  # Calculate the horizontal position
        y = (page_height - img_height) / 2  # Calculate the vertical position
        self.image("shirtificate.png", x, y, img_width, img_height)
        
        # Setting font: helvetica 35
        self.set_font("helvetica", "", 35)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        # self.ln(20)

    def footer(self):
        ...
        # Position cursor at 1.5 cm from bottom:
        # self.set_y(-15)
        # Setting font: helvetica italic 8
        # self.set_font("helvetica", "I", 8)
        # Printing page number:
        # self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

def main():

    name = input("Name: ")

    # Instantiation of inherited class
    pdf = PDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font("Times", size=20)

    # Set automatic page break
    pdf.set_auto_page_break(auto=True, margin=15)
    # white text
    pdf.set_text_color(255, 255, 255)

    # Calculate the horizontal and vertical positions to center the text
    page_width = pdf.w
    page_height = pdf.h
    text = name
    text_width = pdf.get_string_width(text)
    x = (page_width - text_width) / 2  # Calculate the horizontal position
    y = (page_height - pdf.font_size) / 2.5  # Calculate the vertical position

    # Add the centered white text
    pdf.text(x, y , text)


    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()