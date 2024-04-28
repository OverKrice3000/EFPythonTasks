import unittest

from battleshipValidator import ShipsNumberValidator, ShipFieldValidator, ShipFormValidator, \
    ShipsIntersectionsValidator, CompositeValidator


class TestCorrectness(unittest.TestCase):
    def test_correct_field_validation_(self):
        field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        ship_field_validator = ShipFieldValidator(field)
        ship_form_validator = ShipFormValidator(field)
        ships_number_validator = ShipsNumberValidator(field)
        ships_intersections_validator = ShipsIntersectionsValidator(field)
        composite_validator = CompositeValidator().add_primitive(ship_field_validator).add_primitive(
            ship_form_validator).add_primitive(ships_number_validator).add_primitive(
            ships_intersections_validator)

        self.assertTrue(ship_field_validator.validate())
        self.assertTrue(ship_form_validator.validate())
        self.assertTrue(ships_number_validator.validate())
        self.assertTrue(ships_intersections_validator.validate())
        self.assertTrue(composite_validator.validate())

    def test_incorrect_field_form_validation_fails(self):
        field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        ship_field_validator = ShipFieldValidator(field)
        ship_form_validator = ShipFormValidator(field)
        ships_number_validator = ShipsNumberValidator(field)
        ships_intersections_validator = ShipsIntersectionsValidator(field)
        composite_validator = CompositeValidator().add_primitive(ship_field_validator).add_primitive(
            ship_form_validator).add_primitive(ships_number_validator).add_primitive(
            ships_intersections_validator)

        self.assertFalse(ship_field_validator.validate())
        self.assertFalse(composite_validator.validate())

    def test_incorrect_ship_form_validation_fails(self):
        field = [[1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        ship_field_validator = ShipFieldValidator(field)
        ship_form_validator = ShipFormValidator(field)
        ships_number_validator = ShipsNumberValidator(field)
        ships_intersections_validator = ShipsIntersectionsValidator(field)
        composite_validator = CompositeValidator().add_primitive(ship_field_validator).add_primitive(
            ship_form_validator).add_primitive(ships_number_validator).add_primitive(
            ships_intersections_validator)

        self.assertTrue(ship_field_validator.validate())
        self.assertFalse(ship_form_validator.validate())
        self.assertFalse(ships_number_validator.validate())
        self.assertTrue(ships_intersections_validator.validate())
        self.assertFalse(composite_validator.validate())

    def test_incorrect_ships_number_validation_fails(self):
        field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        ship_field_validator = ShipFieldValidator(field)
        ship_form_validator = ShipFormValidator(field)
        ships_number_validator = ShipsNumberValidator(field)
        ships_intersections_validator = ShipsIntersectionsValidator(field)
        composite_validator = CompositeValidator().add_primitive(ship_field_validator).add_primitive(
            ship_form_validator).add_primitive(ships_number_validator).add_primitive(
            ships_intersections_validator)

        self.assertTrue(ship_field_validator.validate())
        self.assertTrue(ship_form_validator.validate())
        self.assertFalse(ships_number_validator.validate())
        self.assertTrue(ships_intersections_validator.validate())
        self.assertFalse(composite_validator.validate())

    def test_incorrect_ships_placement_validation_fails(self):
        field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        ship_field_validator = ShipFieldValidator(field)
        ship_form_validator = ShipFormValidator(field)
        ships_number_validator = ShipsNumberValidator(field)
        ships_intersections_validator = ShipsIntersectionsValidator(field)
        composite_validator = CompositeValidator().add_primitive(ship_field_validator).add_primitive(
            ship_form_validator).add_primitive(ships_number_validator).add_primitive(
            ships_intersections_validator)

        self.assertTrue(ship_field_validator.validate())
        self.assertTrue(ship_form_validator.validate())
        self.assertTrue(ships_number_validator.validate())
        self.assertFalse(ships_intersections_validator.validate())
        self.assertFalse(composite_validator.validate())
