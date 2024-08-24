from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get():
    return Title("Alay Shah", 
                 Meta(name="viewport", content="width=device-width, initial-scale=1.0")), Main(
        Div(
            Div(
                Div(
                    Img(src="static/profile.jpg", alt="Profile Picture", 
                        style="border-radius: 50%; width: 150px; height: 150px; object-fit: cover;"),
                    style="display: inline-block; vertical-align: middle; margin-right: 20px;"
                ),
                Div(
                    H1("Alay Shah", style="font-size: 2.2em; color: black; font-weight: bold; margin-bottom: 5px;"),
                    P("Healthtech founder in Boston, MA", style="font-size: 1.1em; color: black; margin-bottom: 15px; font-weight: 300;"),
                    Div(
                        A(Img(src="static/linkedinicon.jpg", alt="LinkedIn", style="width: 20px; height: 20px;"), 
                          href="https://linkedin.com/in/alayrshah", target="_blank",
                          style="background-color: #0077B5; width: 40px; height: 40px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-right: 10px; text-decoration: none;"),
                        A(Img(src="static/xicon.png", alt="X (Twitter)", style="width: 20px; height: 20px;"), 
                          href="https://twitter.com/alay0shah", target="_blank",
                          style="background-color: #333333; width: 40px; height: 40px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; text-decoration: none;"),
                        style="margin-top: 10px;"
                    ),
                    style="display: inline-block; vertical-align: middle; text-align: left;"
                ),
                style="display: flex; align-items: center; justify-content: center; text-align: center; margin-bottom: 40px;"
            ),
            Div(
                P("Founder @ ", A("Stellar,", href="https://stellarheal.com", target="_blank", style="color: #0077B5; text-decoration: none;"), " building an AI care system that helps therapists learn more about how to help their patients. Came from a long history of computational neuroscience research, primarily in building biomarkers for neurological disorders.", style="color: black; font-weight: 300; margin-bottom: 8px; line-height: 1.5;"),
                P("Generally interested in topics in neuroscience including human behavior, developmental neuroscience, and health optimization. Been building in AI for the last 6 years, but mainly at the application research layer.", style="color: black; font-weight: 300; margin-bottom: 8px; line-height: 1.5;"),
                P("CS & Neuroscience @ ", A("MIT", href="https://bcs.mit.edu/", target="_blank", style="color: #0077B5; text-decoration: none;"), " | ",
                  "Prev. Founder @ Oculo App (Open Sourcing)", 
                  style="color: black; font-weight: 300; line-height: 1.5;"),
                style="margin-bottom: 30px;"
            ),
            Div(
                H2("Contact", style="font-size: 1.5em; color: black; font-weight: 600; margin-bottom: 10px;"),
                P("Email: ", A("alay[at]stellarheal[dot]com", href="mailto:alay@stellarheal.com", target="_blank", style="color: #0077B5; text-decoration: none;"), style="color: black; font-weight: 300; margin-bottom: 8px; line-height: 1.5;"),
                P("Twitter: ", A("twitter.com/alay0shah", href="https://twitter.com/alay0shah", target="_blank", style="color: #0077B5; text-decoration: none;"), style="color: black; font-weight: 300; line-height: 1.5;"),
                style="margin-bottom: 30px;"
            ),
            Div(
                H2("Research", style="font-size: 1.5em; color: black; font-weight: 600; margin-bottom: 10px;"),
                P(A("Research Paper Title 1", href="#", target="_blank", style="color: #0077B5; text-decoration: none;"), " - Publication Date", style="color: black; font-weight: 300; margin-bottom: 8px; line-height: 1.5;"),
                P(A("Research Paper Title 2", href="#", target="_blank", style="color: #0077B5; text-decoration: none;"), " - Publication Date", style="color: black; font-weight: 300; margin-bottom: 8px; line-height: 1.5;"),
                style="margin-bottom: 30px;"
            ),
            Div(
                H2("Links & Resources", style="font-size: 1.5em; color: black; font-weight: 600; margin-bottom: 10px;"),
                P(A("Why we're building Stellar", href="https://www.google.com/search?client=safari&rls=en&q=why+we%27re+building+Stellar&ie=UTF-8&oe=UTF-8", target="_blank", style="color: #0077B5; text-decoration: none;"), " - July 2024", style="color: black; font-weight: 300; margin-bottom: 8px; line-height: 1.5;"),
                P(A("TEDxMIT: Building a better brain", href="https://www.youtube.com/watch?v=cG6sM8z9Umc", target="_blank", style="color: #0077B5; text-decoration: none;"), " - December 2022", style="color: black; font-weight: 300; margin-bottom: 8px; line-height: 1.5;"),
                P(A("Why we're starting Oculo", href="https://medium.com/@oculohealth/why-were-starting-oculo-c840a8cd714", target="_blank", style="color: #0077B5; text-decoration: none;"), " - November 2022", style="color: black; font-weight: 300; margin-bottom: 8px; line-height: 1.5;"),
                P(A("Forbes: This High School Student Invented An Eye-Tracking Test To Detect Brain Disorders", href="https://www.forbes.com/sites/carolineseydel/2021/03/23/this-high-school-student-invented-an-eye-tracking-test-to-detect-brain-disorders/", target="_blank", style="color: #0077B5; text-decoration: none;"), " - March 2021", style="color: black; font-weight: 300; margin-bottom: 8px; line-height: 1.5;"),
                P(A("Plano teen wins $70,000 and national acclaim for eye-opening research", href="https://dallas.culturemap.com/news/innovation/03-24-21-plano-teen-alay-shah-regeneron-science-talent-search-win/", target="_blank", style="color: #0077B5; text-decoration: none;"), " - March 2021", style="color: black; font-weight: 300; line-height: 1.5;"),
                style="margin-bottom: 30px;"
            ),
            cls="container",
            style="max-width: 600px; margin: 0 auto; padding: 40px 20px 20px; font-family: 'DM Sans', sans-serif;"
        ),
        style="background-color: white; color: black; min-height: 100vh; font-family: 'DM Sans', sans-serif;"
    )
                 
serve()
