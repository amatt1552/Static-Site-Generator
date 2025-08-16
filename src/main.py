from textnode import TextNode, TextType
def main():
    text_node = TextNode("heheheha!", TextType.LINK, "https://supercell.com/en/games/clashroyale/")
    print(text_node)

if __name__ == "__main__":
    main()