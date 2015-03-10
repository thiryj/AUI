#import section

#def constants

#Data Structure:
    #action[0...i][0]=sequence
    #action[0...i][1]=verb
    #action[0...i][2...j][0] =ingredient list
        #action[0...i][2...j][0].name=ingredient name
        #action[0...i][2...j][0].unit=unit of measure
        #action[0...i][2...j][0].alias = list of alias names
    #action[0...i][2...j][1] = quantity

class ingredient():
    def __init__(self,name,unit,alias_list):
        self.name = name
        self.unit = unit
        self.alias = alias_list

class recipe():
    def __init__(self,name,product,servings,unit):
        self.name = name
        self.product = product
        self.serving_quant = servings
        self.unit = unit

def get_recipe_action_line(myrec9ipe, step):
    #initialize constants
    verb=1
    ing_package_list=2
    ing=0
    quantity=1

    #initialize variables
    ingredient_report = ""

    #build action line item report
    action_verb = step[1]    
    #loop through ingredient list [step][2]
    for ing_package in step[ing_package_list][:-1]:     #all but last ingredient package
        ingredient_name = ing_package[ing].name
        ingredient_unit = ing_package[ing].unit
        ingredient_quantity = ing_package[quantity]
        #handle plural (curse you english language)
        if ingredient_quantity == 1:
            ingredient_report = ingredient_report + str(ingredient_quantity)+" "+ingredient_unit+ " "+ingredient_name
        else:
            ingredient_report = ingredient_report + str(ingredient_quantity)+" "+ingredient_unit+ "s "+ingredient_name
        ingredient_report = ingredient_report + " and "
    else:                                           #process last ingredient package
        ing_package = step[ing_package_list][-1]
        ingredient_name = ing_package[ing].name
        ingredient_unit = ing_package[ing].unit
        ingredient_quantity = ing_package[quantity]
        #handle plural (curse you english language)
        if ingredient_quantity == 1:
            ingredient_report = ingredient_report + str(ingredient_quantity)+" "+ingredient_unit+ " "+ingredient_name
        else:
            ingredient_report = ingredient_report + str(ingredient_quantity)+" "+ingredient_unit+ "s "+ingredient_name
    step_report = action_verb + " " + ingredient_report
    return(step_report)

def recipe_load():
    #beam in the ingredients - normally this would be built from user input or read from file
    #instantiate the ingredients for oatmeal
    ingredient_1 = ingredient("oats","cup", ["grains", "starch"])
    ingredient_2 = ingredient("water","cup",[])
    ingredient_3 = ingredient("milk","cup",[])
    ingredient_4 = ingredient("maple sugar", "tablespoon", [])

    #instantiate a recipe for oatmeal
    r=recipe('oatmeal','heated oatmeal',1, 'serving')
    r.action_list=[[1,"Heat to taste",[[ingredient_2,1]]]]
    r.action_list=r.action_list + [[2,"Combine",[[ingredient_2,1],[ingredient_1,0.5]]]]
    r.action_list=r.action_list + [[3,"Sprinkle over",[[ingredient_4,1]]]]
    return(r)

def recipe_full_report(recipe):
    r=recipe_load()
    #Build recipe report
    report = ""
    report_intro = "Recipe for " + r.name + ". This recipe makes "
    if r.serving_quant >> 1:
        report_serving = str(r.serving_quant) + " " + str(r.unit)
    else:
        report_serving = str(r.serving_quant) + " " + str(r.unit) + "s"
    report = report_intro + report_serving
    #loop through number of steps and string together
    for step in r.action_list:
        report_line = get_recipe_action_line(r, step)
        report = report + "\n" + report_line
    return report


                               

          


