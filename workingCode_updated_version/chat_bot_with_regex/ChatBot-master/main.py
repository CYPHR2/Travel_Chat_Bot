import webScrapper as wb
import parser as p


def main():
	# First start the webScrapper which will generate the HTML Files
	wb.webScrapper()
	 
	# run the parser to generate JSON Files
	p.parse_function()


if __name__ == "__main__":
	main()
