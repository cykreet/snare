actions = [
	{
		"title": "Tutoring",
		"message": "This student may benefit from additional tutoring sessions to improve their academic performance.",
		"criteria": lambda attributes: attributes["tutoring"] == "0",
	},
]


def evaluate_grade(grade, study_time, absences, tutoring, parent_support, extra, sports, music, volunteer):
	grades = ["A", "B", "C", "D", "F"]
	grade_colours = ["green", "green", "orange", "orange", "red"]
	grade_messages = [
		"This student shows potential for good academic performance.",
		"This student shows potential for good academic performance.",
		"This student may need additional support to improve their academic performance.",
		"This student requires immediate attention to improve their academic performance.",
		"This student shows signs of academic failure and requires immediate attention.",
	]

	clean_grade = grades[grade]
	attributes = {
		"grade": grade,
		"study_time": study_time,
		"absences": absences,
		"tutoring": tutoring,
		"parent_support": parent_support,
		"extra": extra,
		"sports": sports,
		"music": music,
		"volunteer": volunteer,
	}

	applied_actions = []
	for action in actions:
		criteria = action.get("criteria")
		if criteria(attributes) is not True:
			continue

		applied_actions.append(action)

	return {
		"grade": clean_grade,
		"grade_colour": grade_colours[grade],
		"grade_message": grade_messages[grade],
		"actions": applied_actions,
	}
