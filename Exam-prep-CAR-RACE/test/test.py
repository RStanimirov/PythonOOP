from project.team import Team
import unittest


class TestTeam(unittest.TestCase):
    def test_init(self):
        jaguars_team = Team("Jaguars")
        self.assertEqual("Jaguars", jaguars_team.name)
        self.assertEqual({}, jaguars_team.members)
        jaguars_team.members = {"Ivan": 32, "Miro": 33, "Rumen": 34}
        self.assertEqual({"Ivan": 32, "Miro": 33, "Rumen": 34}, jaguars_team.members)

    def test_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ex:
            jaguars_team = Team("Jaguars234")
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_name_setter_successful(self):
        jaguars_team = Team("Jaguars")
        self.assertEqual("Jaguars", jaguars_team.name)

    def test_add_member_new(self):
        jaguars_team = Team("Jaguars")
        jaguars_team.members = {"Ivan": 32, "Miro": 33, "Rumen": 34}
        print_msg = "Successfully added: Stoyan, Dragan"
        self.assertEqual({"Ivan": 32, "Miro": 33, "Rumen": 34}, jaguars_team.members)
        self.assertEqual(print_msg, jaguars_team.add_member(Stoyan=35, Dragan=36))
        self.assertEqual({"Ivan": 32, "Miro": 33, "Rumen": 34, "Stoyan": 35, "Dragan": 36}, jaguars_team.members)
        # self.assertEqual(35, jaguars_team.members["Stoyan"])
        # self.assertEqual(36, jaguars_team.members["Dragan"])

    def test_remove_member_with_existing_name(self):
        jaguars_team = Team("Jaguars")
        jaguars_team.members = {"Ivan": 32, "Miro": 33, "Rumen": 34, "Stoyan": 35, "Dragan": 36}
        print_msg = "Member Dragan removed"
        self.assertEqual(print_msg, jaguars_team.remove_member("Dragan"))
        self.assertEqual({"Ivan": 32, "Miro": 33, "Rumen": 34, "Stoyan": 35}, jaguars_team.members)

    def test_remove_member_non_existing(self):
        jaguars_team = Team("Jaguars")
        jaguars_team.members = {"Ivan": 32, "Miro": 33, "Rumen": 34, "Stoyan": 35}
        print_msg = "Member with name Dragan does not exist"
        self.assertEqual(print_msg, jaguars_team.remove_member("Dragan"))

    def test__gt__true(self):
        jaguars_team = Team("Jaguars")
        jaguars_team.members = {"Ivan": 32, "Miro": 33, "Rumen": 34, "Stoyan": 35}
        lions_team = Team("Lions")
        lions_team.members = {"Lion1": 30, "Lion2": 31, "Lion3": 32}
        self.assertEqual(len(jaguars_team) > len(lions_team), True)

    def test__gt__false(self):
        jaguars_team = Team("Jaguars")
        jaguars_team.members = {"Ivan": 32, "Miro": 33, "Rumen": 34, "Stoyan": 35}
        lions_team = Team("Lions")
        lions_team.members = {"Lion1": 30, "Lion2": 31, "Lion3": 32}
        self.assertEqual(jaguars_team.__gt__(lions_team), True)

    def test__len__(self):
        jaguars_team = Team("Jaguars")
        jaguars_team.members = {"Ivan": 32, "Miro": 33, "Rumen": 34, "Stoyan": 35}
        self.assertEqual(4, jaguars_team.__len__())

    def test_add_other_team(self):
        jaguars_team = Team("Jaguars")
        jaguars_team.members = {"Ivan": 32, "Miro": 33, "Rumen": 34}
        lions_team = Team("Lions")
        lions_team.members = {"Lion1": 30, "Lion2": 31, "Lion3": 32}
        jaguars_team.__add__(lions_team)
        return_result = "Team name: JaguarsLions\nMember: Rumen - 34-years old\nMember: Miro - 33-years old\nMember: Ivan - 32-years old\nMember: Lion3 - 32-years old\nMember: Lion2 - 31-years old\nMember: Lion1 - 30-years old"
        self.assertEqual(return_result, jaguars_team.__add__(lions_team).__str__())
        self.assertEqual("JaguarsLions", jaguars_team.__add__(lions_team).name)
        self.assertEqual({'Ivan': 32, 'Miro': 33, 'Rumen': 34, 'Lion1': 30, 'Lion2': 31, 'Lion3': 32}, jaguars_team.__add__(lions_team).members)
        self.assertEqual("Successfully added: Lion4", jaguars_team.__add__(lions_team).add_member(Lion4=33))

    def test_str(self):
        jaguars_team = Team("Jaguars")
        jaguars_team.members = {"Ivan": 32, "Miro": 33, "Rumen": 34}
        print_result = "Team name: Jaguars\nMember: Rumen - 34-years old\nMember: Miro - 33-years old\nMember: Ivan - 32-years old"
        self.assertEqual(print_result, jaguars_team.__str__())


if __name__ == '__main__':
    unittest.main()




# jaguars_team = Team("Jaguars")
# lions_team = Team("Lions")
# jaguars_team.members = {"Ivan": 32, "Miro": 33, "Rumen": 34}
# lions_team.members = {"Lion1": 30, "Lion2": 31, "Lion3": 32}
# print(jaguars_team.__str__())
# print(jaguars_team.add_member(Stoyan=35, Dragan=36))
# print(jaguars_team.__str__())
# print(jaguars_team.remove_member("Dragan"))
# print(jaguars_team.__gt__(lions_team))
# print(jaguars_team.__len__())
#
# print(jaguars_team.__add__(lions_team))

# Team name: JaguarsLions
# Member: Rumen - 34-years old
# Member: Miro - 33-years old
# Member: Ivan - 32-years old
# Member: Lion3 - 32-years old
# Member: Lion2 - 31-years old
# Member: Lion1 - 30-years old