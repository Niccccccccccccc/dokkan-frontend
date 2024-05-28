import csv
def storedatabase(directory,name,printing=True):
    directory+=name
    file = open(directory, encoding="Latin-1")
    dbtemp=csv.reader(file)
    name=[]
    for row in dbtemp:
        name.append(row)
    return(name)

directory="data/"

active_skills=storedatabase(directory,"active_skills.csv")
active_skill_sets=storedatabase(directory,"active_skill_sets.csv")
battle_params=storedatabase(directory,"battle_params.csv")

cards=storedatabase(directory,"cards.csv")
card_active_skills=storedatabase(directory,"card_active_skills.csv")
card_awakening_routes=storedatabase(directory,"card_awakening_routes.csv")
card_card_categories=storedatabase(directory,"card_card_categories.csv")
card_categories=storedatabase(directory,"card_categories.csv")
card_growths=storedatabase(directory,"card_growths.csv")
card_specials=storedatabase(directory,"card_specials.csv")
card_unique_info_set_relations=storedatabase(directory,"card_unique_info_set_relations.csv")

dokkan_fields=storedatabase(directory,"dokkan_fields.csv")
dokkan_field_passive_skill_relations=storedatabase(directory,"dokkan_field_passive_skill_relations.csv")

leader_skills=storedatabase(directory,"leader_skills.csv")
link_skills=storedatabase(directory,"link_skills.csv")
link_skill_efficacies=storedatabase(directory,"link_skill_efficacies.csv")
link_skill_lvs=storedatabase(directory,"link_skill_lvs.csv")

optimal_awakening_growths=storedatabase(directory,"optimal_awakening_growths.csv")

passive_skills=storedatabase(directory,"passive_skills.csv")
passive_skill_sets=storedatabase(directory,"passive_skill_sets.csv")
passive_skill_set_relations=storedatabase(directory,"passive_skill_set_relations.csv")
potential_events=storedatabase(directory,"potential_events.csv")
potential_squares=storedatabase(directory,"potential_squares.csv")
potential_square_relations=storedatabase(directory,"potential_square_relations.csv")

skill_causalities=storedatabase(directory,"skill_causalities.csv")
specials=storedatabase(directory,"specials.csv")
special_bonuses=storedatabase(directory,"special_bonuses.csv")
special_sets=storedatabase(directory,"special_sets.csv")
sub_target_types=storedatabase(directory,"sub_target_types.csv")
