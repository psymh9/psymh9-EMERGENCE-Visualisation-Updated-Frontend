from constantly import ValueConstant, Values
from textwrap3 import wrap
from git import Repo
from netgraph import Graph
import gravis as gv, igraph as ig, networkx as nx , matplotlib.pyplot as plt, openpyxl, random, pandas as pd, sys
import os

print(os.getcwd())
class Discipline(Values):
   """
   Constants representing various specialties across the EMERGENCE network. 
   """
   COMPUTER_SCIENCE = ValueConstant("Computer Science")
   COMPUTER_SCIENCE_SHORTHAND = ValueConstant("CS")
   ROBOTICS = ValueConstant("Robotics")
   HEALTHCARE = ValueConstant("Healthcare")
   DESIGN_ENGINEERING_INNOVATION = ValueConstant("Design Engineering and Innovation")
   DESIGN_ENGINEERING_INNOVATION_SHORTHAND = ValueConstant("DEAI")
   ELECTRONIC_ENGINEERING = ValueConstant("Electronic Engineering")
   ELECTRONIC_ENGINEERING_SHORTHAND = ValueConstant("EE")
   SOCIAL_CARE = ValueConstant("Social Care")
   SOCIAL_CARE_SHORTHAND = ValueConstant("SC")
   PHYSIOTHERAPY = ValueConstant("Physiotherapy")
   INCLUDE_CENTRAL_NODE = ValueConstant("include-central-node")
   INCLUDE_LEGEND_NODES = ValueConstant("include-legend-nodes")

class Institution(Values):
    """
    Constants representing the Institutions within the network 
    """
    UNIVERSITY_OF_NOTTINGHAM = ValueConstant("University of Nottingham")
    UNIVERSITY_OF_NOTTINGHAM_SHORTHAND = ValueConstant("UoN")


class Colour(Values):
   """
   Constants representing the various colours of the nodes within the network visualisation
   """
   RED = ValueConstant("red")
   BLUE = ValueConstant("blue")
   GREEN = ValueConstant("green")
   YELLOW = ValueConstant("yellow")
   ORANGE = ValueConstant("orange")
   MAGENTA = ValueConstant("magenta")
   PURPLE = ValueConstant("purple")

class Misc(Values):
   """
   Constants representing miscellaneous values used within the program.  
   """
   ORIGIN = ValueConstant('origin')
   REMOTE = ValueConstant('remote')
   ERROR_MESSAGE = ValueConstant('Some error occured while pushing the code')
   PATH_OF_GIT_REPO = ValueConstant(r'')
   COMMIT_MESSAGE = ValueConstant('New members added to the dataset')
   EXCEL_FILE = ValueConstant("NetworkVisualisationToolWebsite/templates/NetworkVisualisationToolWebsite/NetworkVisualisationData/EMERGENCECollatedData.xlsx")
   ZERO = ValueConstant(0)
   ONE = ValueConstant(1)
   TWO = ValueConstant(2)
   FIVE = ValueConstant(5)
   SIX = ValueConstant(6)
   SEVEN = ValueConstant(7)
   EIGHT = ValueConstant(8)
   NINE = ValueConstant(9)
   TEN = ValueConstant(10)
   ELEVEN = ValueConstant(11)
   TWELVE = ValueConstant(12)
   THIRTEEN = ValueConstant(13)
   WIDTH_RESOLUTION_VISUALISATION = ValueConstant(1000)
   HEIGHT_RESOLUTION_VISUALISATION = ValueConstant(1000) 
   STREAMLIT_TITLE = ValueConstant("EMERGENCE Network Visualisation Tool")
   STREAMLIT_TEXT = ValueConstant("Refer to the EMERGENCE website for instructions on how to use")
   LEGEND_TITLE = ValueConstant("Legend Node: ")
   ONE_HUNDRED = ValueConstant(100)
   LEGEND_X_VALUE = ValueConstant(-1500)
   LEGEND_Y_VALUE = ValueConstant(-1250)
   LEGEND_NODE_SIZE = ValueConstant(75)
   LEGEND_SHAPE = ValueConstant("box")
   LEGEND_WIDTH_CONSTRAINT = ValueConstant(150)
   LEGEND_FONT_SIZE = ValueConstant(20)
   CENTRAL_NODE_ID = ValueConstant("Central Node")
   CENTRAL_NODE_LABEL = ValueConstant("Emergence Network")
   CENRAL_NODE_COLOUR = ValueConstant("black")
   READ_MODE = ValueConstant("r")
   ENCODING = ValueConstant("utf-8")
   HTML_FILE_NAME = ValueConstant("network_visualisation.html")
   NAME = ValueConstant("Name: ")
   INSTITUTION = ValueConstant("\nInstitution: ")
   JOB_TITLE = ValueConstant("\nJob Title: ")
   DISCIPLINE = ValueConstant("\nDiscipline: ")
   LOCATION_SECTION = ValueConstant("\nLocation: ")
   RESEARCH_THEMES = ValueConstant("\nResearch themes of interest: ")
   TRUE = ValueConstant(True)
   FALSE = ValueConstant(False)
   NEWLINE = ValueConstant("\n")
   VALUE = ValueConstant("value")
   ID = ValueConstant("id")
   TITLE = ValueConstant("title")
   ALPHABET = ValueConstant("alphabet")
   ALPHABETICAL = ValueConstant("Alphabetical")
   GROUP = ValueConstant("group")
   LABEL = ValueConstant("label")
   SIZE = ValueConstant("size")
   FIXED = ValueConstant("fixed")
   X = ValueConstant("x")
   Y = ValueConstant("y")
   PHYSICS = ValueConstant("physics")
   SHAPE = ValueConstant("shape")
   TMP = ValueConstant('tmp')
   WIDTH_CONSTRAINT = ValueConstant("widthConstraint")
   FONT = ValueConstant("font")
   DISCIPLINE_WORD = ValueConstant("Discipline")
   INSTITUTION_WORD = ValueConstant("Institution")
   SIZE = ValueConstant("size")
   LOCATION = ValueConstant("Location")
   PX = ValueConstant('{fpixels}px')
   HEIGHT = ValueConstant("1080px")
   WIDTH = ValueConstant("100%")
   BGCOLOUR = ValueConstant("#fffff")
   HTML_FILES = ValueConstant("html_files")
   FORMATTED_HTML_FILE_NAME = ValueConstant("{path_label}\\network_visualisation.html")
   PAGE_LAYOUT = ValueConstant("wide")
   ALL = ValueConstant("All") 
   EMPTY_STRING = ValueConstant("")

def setMemberColour(specialty):
   """
   Returns a specific node-colour based on the member's specialty.  
   """
   #Colours nodes a unique colour according to the specialty
   if (specialty == Discipline.COMPUTER_SCIENCE.value):
      #All Computer Scientists are coloured as red
      return Colour.RED.value
   elif (specialty == Discipline.ROBOTICS.value):
      #All Roboticists are coloured as blue
      return Colour.BLUE.value
   elif (specialty == Discipline.DESIGN_ENGINEERING_INNOVATION.value):
      #All Design Engineers are coloured Green
      return Colour.GREEN.value
   elif (specialty == Discipline.HEALTHCARE.value):
      #All Healthcare professionals are coloured yellow
      return Colour.YELLOW.value
   elif (specialty == Discipline.PHYSIOTHERAPY.value):
      #All Physiotherapsists are coloured orange
      return Colour.ORANGE.value
   elif (specialty == Discipline.ELECTRONIC_ENGINEERING.value):
      #All Electronic Engineers are coloured magenta
      return Colour.MAGENTA.value
   elif (specialty == Discipline.SOCIAL_CARE.value):
      #All Electronic Engineers are coloured purple
      return Colour.PURPLE.value

def format_motivation_text(motivationText, charLimit):
   """
   formats the passed in 'motivationText' to abide by the line character limit
   charLimit.
   """
   splitText = wrap(motivationText, charLimit)
   #formats 'motivationText' in to charLimit character blocks
   #each of these blocks are stored in the list splitText
   formattedMessage=Misc.NEWLINE.value + Misc.NEWLINE.value
   #Creates a two-line gap between the title and the text
   for i in range(len(splitText)):
      #Iterates through the 'splitText' array and concatenates charLimit
      #characters before a newline
      formattedMessage += splitText[i] + Misc.NEWLINE.value
   #returns a formattedMessage once this is complete
   return formattedMessage  

def git_push():
    #Checks for changes to the data file, if a new member has been added a commit is staged then pushed
    try:
        repo = Repo(Misc.PATH_OF_GIT_REPO.value)
        #Contains the repo object
        repo.git.add(Misc.EXCEL_FILE.value)
        #Stages the excel file containing all of the member data to git if there are any changes
        repo.index.commit(Misc.COMMIT_MESSAGE.value)
        #Commits the updated file with the commit message 'Update Network Visualisation'
        origin = repo.remote(name=Misc.ORIGIN.value)
        #Contains the origin branch of the repository
        origin.push()
        #pushes the changes up to the remote repository
    except:
        #If this process doesn't work print out an error message
        print(Misc.ERROR_MESSAGE.value)

def filterByTwoDifferentFactors(factor1, factor2, filterParameter1, filterParameter2, name):
     if ((factor1 == filterParameter1) and (factor2 == filterParameter2)):
         filterGraph1.append(name)

def filterByTwoSameFactors(factor1, factor2, filterParameter1, filterParameter2, name):
    if ((factor1 == filterParameter1) or (factor2 == filterParameter2)):
         filterGraph1.append(name)

def filterBySingleFactor(factor1, filterParameter1, name):
    if ((factor1 == filterParameter1)):
        filterGraph1.append(name)

def shorthandParameters(filterParameter1, filterParameter2):
    match filterParameter1:
       case Discipline.COMPUTER_SCIENCE_SHORTHAND.value:
           filterParameter1 = Discipline.COMPUTER_SCIENCE.value
       case Discipline.DESIGN_ENGINEERING_INNOVATION_SHORTHAND.value:
           filterParameter1 = Discipline.DESIGN_ENGINEERING_INNOVATION.value
       case Discipline.ELECTRONIC_ENGINEERING_SHORTHAND.value:
           filterParameter1 = Discipline.ELECTRONIC_ENGINEERING.value
       case Discipline.SOCIAL_CARE_SHORTHAND.value:
           filterParameter1 = Discipline.SOCIAL_CARE.value   
       case Institution.UNIVERSITY_OF_NOTTINGHAM_SHORTHAND.value:
           filterParameter1 = Institution.UNIVERSITY_OF_NOTTINGHAM.value 
    match filterParameter2: 
       case Discipline.COMPUTER_SCIENCE_SHORTHAND.value:
           filterParameter2 = Discipline.COMPUTER_SCIENCE.value
       case Discipline.DESIGN_ENGINEERING_INNOVATION_SHORTHAND.value:
           filterParameter2 = Discipline.DESIGN_ENGINEERING_INNOVATION.value
       case Discipline.ELECTRONIC_ENGINEERING_SHORTHAND.value:
           filterParameter2 = Discipline.ELECTRONIC_ENGINEERING.value
       case Discipline.SOCIAL_CARE_SHORTHAND.value:
           filterParameter2 = Discipline.SOCIAL_CARE.value 
       case Institution.UNIVERSITY_OF_NOTTINGHAM_SHORTHAND.value:
           filterParameter2 = Institution.UNIVERSITY_OF_NOTTINGHAM.value
    return filterParameter1, filterParameter2

nodesFiltered = False
filterCategory1 = ""
filterParameter1 = ""
filterCategory2 = ""
filterParameter2 = ""
if (len(sys.argv) == 3):
   nodesFiltered = True
   filterCategory1 = sys.argv[1]
   filterParameter1 = sys.argv[2]
elif (len(sys.argv) > 3):
   nodesFiltered = True
   filterCategory1 = sys.argv[1]
   filterParameter1 = sys.argv[2]
   filterCategory2 = sys.argv[3]
   filterParameter2 = sys.argv[4]

def setNodesFiltered(value):
   global nodesFiltered
   nodesFiltered = value

def filterNodesByCategories(filterCategory1, filterParameter1, filterCategory2, filterParameter2, member_name, member_institution, member_location, member_discipline): 
   match filterCategory1:
               case Misc.DISCIPLINE_WORD.value:
                  if (filterParameter1 == "All"):
                     match filterCategory2:
                        case Misc.LOCATION.value:
                           if (filterParameter2 == "All"):
                              setNodesFiltered(Misc.FALSE.value)
                           else:
                              filterByTwoDifferentFactors(member_discipline, member_location, filterParameter1, filterParameter2, member_name)
                        case Misc.DISCIPLINE_WORD.value:
                           setNodesFiltered(Misc.FALSE.value)
                        case Misc.ALPHABETICAL.value:
                           filterBySingleFactor(member_name[Misc.ZERO.value], filterParameter1, member_name)
                        case Misc.INSTITUTION_WORD.value:
                           filterBySingleFactor(member_institution, filterParameter1, member_name)
                        case Misc.EMPTY_STRING.value:
                           setNodesFiltered(Misc.FALSE.value)
                  else:
                     match filterCategory2:
                        case Misc.LOCATION.value:
                           if (filterParameter2 == "All"):
                              filterBySingleFactor(member_discipline, filterParameter1, member_name)
                           else:
                              filterByTwoDifferentFactors(member_discipline, member_location, filterParameter1, filterParameter2, member_name)
                        case Misc.DISCIPLINE_WORD.value:
                           if (filterParameter2 == "All"):
                              setNodesFiltered(False)
                           else:
                              filterByTwoSameFactors(member_discipline, member_discipline, filterParameter1, filterParameter2, member_name)
                        case Misc.ALPHABETICAL.value:
                           filterByTwoDifferentFactors(member_discipline, member_name[Misc.ZERO.value], filterParameter1, filterParameter2, member_name)
                        case Misc.INSTITUTION_WORD.value:
                           filterByTwoDifferentFactors(member_discipline, member_institution, filterParameter1, filterParameter2, member_name)
                        case Misc.EMPTY_STRING.value:
                           filterBySingleFactor(member_discipline, filterParameter1, member_name)

               case Misc.LOCATION.value:
                  if (filterParameter1 == "All"):
                     match filterCategory2:
                        case Misc.DISCIPLINE_WORD.value:
                           if (filterParameter2 == "All"):
                              setNodesFiltered(False)
                           else:
                              filterBySingleFactor(member_discipline, filterParameter2, member_name)
                        case Misc.INSTITUTION_WORD.value:
                           filterBySingleFactor(member_institution, filterParameter2, member_name)
                        case Misc.LOCATION.value:
                           setNodesFiltered(False)
                        case Misc.ALPHABETICAL.value: 
                           filterBySingleFactor(member_name[Misc.ZERO.value], filterParameter2, member_name)
                        case Misc.EMPTY_STRING.value:
                           setNodesFiltered(False)
                  else:
                     match filterCategory2:
                        case Misc.DISCIPLINE_WORD.value:
                           if (filterParameter2 == "All"):
                              filterBySingleFactor(member_location, filterParameter1, member_name)
                           else:
                              filterByTwoDifferentFactors(member_location, member_discipline, filterParameter1, filterParameter2, member_name)
                        case Misc.INSTITUTION_WORD.value:
                           filterByTwoDifferentFactors(member_location, member_institution, filterParameter1, filterParameter2, member_name)
                        case Misc.LOCATION.value:
                           if (filterParameter2 == "All"):
                              setNodesFiltered(False)
                           filterByTwoSameFactors(member_location, member_location, filterParameter1, filterParameter2, member_name)
                        case Misc.ALPHABETICAL.value: 
                           filterByTwoDifferentFactors(member_location, member_name[Misc.ZERO.value], filterParameter1, filterParameter2, member_name)
                        case Misc.EMPTY_STRING.value:
                           filterBySingleFactor(member_location, filterParameter1, member_name)
               case Misc.INSTITUTION_WORD.value: 
                  match filterCategory2:
                     case Misc.DISCIPLINE_WORD.value: 
                        filterByTwoDifferentFactors(member_institution, member_discipline, filterParameter1, filterParameter2, member_name)
                     case Misc.LOCATION.value: 
                        filterByTwoDifferentFactors(member_institution, member_location, filterParameter1, filterParameter2, member_name)
                     case Misc.INSTITUTION_WORD.value: 
                        filterByTwoSameFactors(member_institution, member_institution, filterParameter1, filterParameter2, member_name)
                     case Misc.ALPHABETICAL.value: 
                        filterByTwoDifferentFactors(member_institution, member_name[Misc.ZERO.value], filterParameter1, filterParameter2, member_name)
                     case Misc.EMPTY_STRING.value:
                        filterBySingleFactor(member_institution, filterParameter1, member_name)
               case Misc.ALPHABETICAL.value: 
                  match filterCategory2:
                     case Misc.DISCIPLINE_WORD.value:
                        filterByTwoDifferentFactors(member_name[Misc.ZERO.value], member_discipline, filterParameter1, filterParameter2, member_name)
                     case Misc.LOCATION.value: 
                        filterByTwoDifferentFactors(member_name[Misc.ZERO.value], member_location, filterParameter1, filterParameter2, member_name)
                     case Misc.INSTITUTION_WORD.value:
                        filterByTwoDifferentFactors(member_name[Misc.ZERO.value], member_institution, filterParameter1, filterParameter2, member_name)
                     case Misc.ALPHABETICAL.value: 
                        filterByTwoSameFactors(member_name[Misc.ZERO.value], member_name[Misc.ZERO.value], filterParameter1, filterParameter2, member_name)
                     case Misc.EMPTY_STRING.value:
                        filterBySingleFactor(member_name[Misc.ZERO.value], filterParameter1, member_name)
               case Misc.EMPTY_STRING.value:
                  match filterCategory2:
                     case Misc.DISCIPLINE_WORD.value:
                        filterBySingleFactor(member_discipline, filterParameter2, member_name)
                     case Misc.LOCATION.value: 
                        filterBySingleFactor(member_location, filterParameter2, member_name)
                     case Misc.INSTITUTION_WORD.value:
                        filterBySingleFactor(member_institution, filterParameter2, member_name)
                     case Misc.ALPHABETICAL.value: 
                        filterBySingleFactor(member_name[Misc.ZERO.value], filterParameter2, member_name)


filterParameter1, filterParameter2 = shorthandParameters(filterParameter1, filterParameter2)
    
filterGraph1 = []
filterGraph2 = []
#List containing the names of all the members in the network 
emergenceMemberNames = []
#Initialises a networkX graph for the legend nodes
emergenceMemberMotivations = []
nx_graph = nx.Graph()
#Reference to the excel file containing the member details 
emergenceExcelWorkbook = openpyxl.load_workbook(Misc.EXCEL_FILE.value)
#Reference to the first sheet in the excel file
emergenceExcelWorkbookSheet = emergenceExcelWorkbook.worksheets[Misc.ZERO.value]

#Stores the number of actual nodes & the number of nodes in the legend
num_actual_nodes = emergenceExcelWorkbookSheet.max_row-Misc.ONE.value
num_legend_nodes = Misc.SEVEN.value

#The Step value represents the spacing between each of the legend nodes
step = Misc.ONE_HUNDRED.value
#The x value represents the x position of the legend 
x = Misc.LEGEND_X_VALUE.value
#The y value represents the y position of the legend
y = Misc.LEGEND_Y_VALUE.value
#A list of all of the labels for the legend nodes
legend_labels = [Discipline.ROBOTICS.value, Discipline.HEALTHCARE.value, Discipline.COMPUTER_SCIENCE.value, Discipline.DESIGN_ENGINEERING_INNOVATION.value,
                 Discipline.ELECTRONIC_ENGINEERING.value, Discipline.SOCIAL_CARE.value, Discipline.PHYSIOTHERAPY.value]

#A list of tuples containing all of the legend nodes
legend_nodes = [
    (
        num_actual_nodes + legend_node, #Node ID set to the sum of the current numbher of nodes  
                                                                # + the index of the legend node
        {
            Misc.GROUP.value: legend_node, #Adds the new legend node to the group
            Misc.LABEL.value: legend_labels[legend_node],#Indexes the legend_labels list to return the appropriate label for the node
            Misc.SIZE.value: Misc.LEGEND_NODE_SIZE.value,#Defines the size of the legend nodes
            Misc.FIXED.value: Misc.TRUE.value,#Sets the legend position to fixed
            Misc.PHYSICS.value: Misc.FALSE.value, #Sets the legend to have no physics mechanics
            Misc.X.value: x, #Sets the x-value of the legend
            Misc.Y.value: Misc.PX.value.format(fpixels=y+legend_node*step), #Sets the y-value of the legend
            Misc.SHAPE.value: Misc.LEGEND_SHAPE.value, #Sets the shape of the legend nodes
            Misc.WIDTH_CONSTRAINT.value: Misc.LEGEND_WIDTH_CONSTRAINT.value, #Sets the width contraints for the legend
            Misc.FONT.value: {Misc.SIZE.value: Misc.LEGEND_FONT_SIZE.value}, #Sets the font size for the legend
            Misc.DISCIPLINE_WORD.value: Discipline.INCLUDE_LEGEND_NODES.value, #Sets the speciality attribute for the legend 'include-legend-nodes'
            Misc.INSTITUTION_WORD.value: Discipline.INCLUDE_LEGEND_NODES.value,#Sets the institution attribute for the legend 'include-legend-nodes'
            Misc.ALPHABET.value: Discipline.INCLUDE_LEGEND_NODES.value, #Sets the alphabet attribute for the legend 'include-legend-nodes'
            Misc.TITLE.value: Misc.LEGEND_TITLE.value + legend_labels[legend_node], #Sets the title attribute for the legend 'include-legend-nodes'
            Misc.LOCATION.value: Discipline.INCLUDE_LEGEND_NODES.value#Sets the location attribute to the 'include_legend_nodes' value
        }
      
    )
    for legend_node in range(num_legend_nodes)#Creates 'num_legend_nodes' legend nodes and specifies an attribute for all of them
]

nx_graph.add_nodes_from(legend_nodes) #Adds all of the legend nodes to the graph

nx_graph.add_node(Misc.CENTRAL_NODE_ID.value, label=Misc.CENTRAL_NODE_LABEL.value, title=Misc.CENTRAL_NODE_ID.value, physics=Misc.TRUE.value, color=Misc.CENRAL_NODE_COLOUR.value, location= Discipline.INCLUDE_CENTRAL_NODE.value, institution=Discipline.INCLUDE_CENTRAL_NODE.value, Discipline=Discipline.INCLUDE_CENTRAL_NODE.value, alphabet=Discipline.INCLUDE_CENTRAL_NODE.value, x=1000, y=1000)    
#Adds in the central node of the network visualisation which is labeled "EMERGENCE_Network"

for row_index in range(Misc.TWO.value, emergenceExcelWorkbookSheet.max_row+Misc.ONE.value):
     #Iterates through all of the rows in the excel document
          #if the row is not the title row 
          member_name = str(emergenceExcelWorkbookSheet.cell(row = row_index, column= Misc.SIX.value).value)
          #The member_name variable is extracted from the fifth column of the sheet
          member_institution = str(emergenceExcelWorkbookSheet.cell(row = row_index, column= Misc.SEVEN.value).value)
          #The member_institution variable is extracted from the sixth column of the sheet
          member_location = str(emergenceExcelWorkbookSheet.cell(row = row_index, column= Misc.EIGHT.value).value)
          #The member_location variable is extracted from the seventh column of the sheet
          member_job_title = str(emergenceExcelWorkbookSheet.cell(row = row_index, column= Misc.NINE.value).value)
          #The member_job_title variable is extracted from the eighth column of the sheet
          member_discipline = str(emergenceExcelWorkbookSheet.cell(row = row_index, column= Misc.TEN.value).value)
          #The member_specialty variable is extracted from the ninth column of the sheet
          member_colour = setMemberColour(member_discipline)
          #The member_name variable is assigned the result of the setMemberColour function
          member_network_motivation = format_motivation_text(str(emergenceExcelWorkbookSheet.cell(row = row_index, column= Misc.THIRTEEN.value).value), Misc.ONE_HUNDRED.value)
          #The member_network_motivation variable is assigned the result of the format_motivation_text function
          member_alphabet = member_name[Misc.ZERO.value]
          #The member_specialty variable is extracted from the ninth column of the sheet
          member_title = Misc.NAME.value + member_name + Misc.INSTITUTION.value + member_institution + Misc.JOB_TITLE.value + member_job_title + Misc.DISCIPLINE.value + member_discipline + Misc.LOCATION_SECTION.value + member_location + Misc.RESEARCH_THEMES.value + member_network_motivation
          #The member_title variable displays all of the member attributes when the node is hovered over
          nx_graph.add_node(member_name, label=member_name, title=member_title, physics=Misc.TRUE.value,  institution=member_institution, Discipline=member_discipline, alphabet=member_alphabet, color=member_colour, location=member_location)
          #Creates a new node for each of the EMERGENCE members with all of the relevant attributes
          emergenceMemberNames.append(member_name)
          #Appends each member to the member_names array
          if (member_network_motivation != format_motivation_text("None", Misc.ONE_HUNDRED.value)):
            emergenceMemberMotivations.append(member_network_motivation)
          if (nodesFiltered):
            filterNodesByCategories(filterCategory1,filterParameter1, filterCategory2, filterParameter2, 
                                    member_name, member_institution, member_location, member_discipline)

# Calculate layout
pos = nx.drawing.layout.spring_layout(nx_graph, scale=1000)

legend_node_names = [138, 139, 140, 141, 142, 143, 144]

legend_node_dict_mapping = [{138:Discipline.ROBOTICS.value}, {139 : Discipline.HEALTHCARE.value}, 
                             {140:Discipline.COMPUTER_SCIENCE.value}, {141: Discipline.DESIGN_ENGINEERING_INNOVATION.value},
                             {142:Discipline.ELECTRONIC_ENGINEERING.value}, {143:Discipline.SOCIAL_CARE.value}, {144:Discipline.PHYSIOTHERAPY.value } ]

legend_node_colour_mapping = {Discipline.ROBOTICS.value : setMemberColour(Discipline.ROBOTICS.value), 
                             Discipline.HEALTHCARE.value : setMemberColour(Discipline.HEALTHCARE.value),
                             Discipline.COMPUTER_SCIENCE.value : setMemberColour(Discipline.COMPUTER_SCIENCE.value),
                             Discipline.DESIGN_ENGINEERING_INNOVATION.value : setMemberColour(Discipline.DESIGN_ENGINEERING_INNOVATION.value),
                             Discipline.ELECTRONIC_ENGINEERING.value : setMemberColour(Discipline.ELECTRONIC_ENGINEERING.value),
                             Discipline.SOCIAL_CARE.value : setMemberColour(Discipline.SOCIAL_CARE.value),
                             Discipline.PHYSIOTHERAPY.value : setMemberColour(Discipline.PHYSIOTHERAPY.value)}

legend_node_count = 0
# Add coordinates as node annotations that are recognized by gravis
general_node_count = 0

legend_node_coordinates = [(250,750), (750,1250), (750,250), (500,-750), (150,-750), (-500,-750),(-750,250)]

for name, (x, y) in pos.items():
    node = nx_graph.nodes[name]
    if name == "Central Node":
        node['x'] = 0
        node['y'] = 0
        nx.set_node_attributes(nx_graph, {name : 75}, name="size")
        node['hover'] = name
    elif name in legend_node_names:
        legendDict = legend_node_dict_mapping[legend_node_count]
        nx_graph = nx.relabel_nodes(nx_graph, legendDict)
        name = legendDict[name]
        node = nx_graph.nodes[name]
        legend_node_coordinate = legend_node_coordinates[legend_node_count]
        node['x'] = legend_node_coordinate[0]
        node['y'] = legend_node_coordinate[1]
        nx.set_node_attributes(nx_graph, {name : 50}, name="size")
        hoverText = nx.get_node_attributes(nx_graph, "title")
        node['hover'] = name
        legend_node_count += 1
    else:
        node['x'] = random.randint(-1001,1001)
        node['y'] = random.randint(-1001,1001)
        nx.set_node_attributes(nx_graph, {name : 50}, name="size")
        hoverText = nx.get_node_attributes(nx_graph, "title")
        node['hover'] =  hoverText[name]
        general_node_count += 1

nx.set_node_attributes(nx_graph, legend_node_colour_mapping, name="color")

#nx_graph = nx.subgraph_view(nx_graph, filter_node=filter_node)

for i in range(Misc.ZERO.value, len(legend_labels)):
   #Iterates through the member_names array
   nx_graph.add_edge(Misc.CENTRAL_NODE_ID.value, legend_labels[i]) #Creates an edge between the central node and all the other nodes

for i in range(Misc.ZERO.value, len(legend_labels)):
   for node in nx_graph.nodes():
       selectedNode = nx_graph.nodes[node]
       if (selectedNode[Misc.LABEL.value] not in legend_labels):
         if (legend_labels[i] == selectedNode[Misc.DISCIPLINE_WORD.value]):
            legendPoint = legend_node_coordinates[i]
            selectedNode['x'] = random.randint(legendPoint[0] - 750,legendPoint[0] + 750)
            selectedNode['y'] = legendPoint[1] + random.randint(50, 400)
            nx_graph.add_edge(legend_labels[i], selectedNode[Misc.LABEL.value])

if (nodesFiltered):
   filterGraph1.append("Central Node")
   filterGraph1.append(filterParameter1)
   filterGraph1.append(filterParameter2)
   filteredView = nx_graph.subgraph(filterGraph1)
   figGravis = gv.d3(filteredView, zoom_factor=0.45, layout_algorithm_active=False, graph_height=900 )
else:
   figGravis = gv.d3(nx_graph, zoom_factor=0.45, layout_algorithm_active=False, graph_height=900)

fname = "NetworkVisualisationToolWebsite/templates/NetworkVisualisationToolWebsite/PythonNetworkVisualisation.html"
html_file_content = figGravis.to_html_standalone()
html_file = open(fname, "w", encoding="utf-8")
html_file.write(html_file_content)
html_file.close()






