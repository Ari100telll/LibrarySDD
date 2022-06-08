from flask import Blueprint, jsonify, request

rents_bp = Blueprint("rents_blueprint", __name__, url_prefix="/rents")


@rents_bp.route("/", methods=["GET"])
def get_all_rents():
    rents = [
        {
            "id": 1,
            "user": {
                "id": 1,
                "name": "Kuipers",
                "surname": "Alkyone",
                "phoneNumber": "+380(048)69-85-63",
                "address": "Ukraine, Chernigiv, Starobіlouska Vul., bld. 33, appt. 69",
                "category": {"category": "reader1", "discountPercentage": 20.0},
            },
            "rent_start_date": "2021-09-19 07:12:15",
            "expected_rent_end_date": "2021-10-05 20:18:46",
            "rent_end_date": "",
            "library_item": {
                "id": 1,
                "pledge_price": 191,
                "quantity": 42,
                "title": "Synergized scalable help-desk",
                "author": "Yancy Chilles",
                "genre": "luctus",
            },
            "rent_price": 697,
            "fine_price": 120,
            "damage_level": {
                "id": 1,
                "level": "level1",
                "finePercentage": 20.0,
            },
        },
        {
            "id": 2,
            "user": {
                "id": 2,
                "name": "Micaela",
                "surname": "Stack",
                "phoneNumber": "+380(0542)34-17-38",
                "address": "Ukraine, Rivne, Shevchenko Vul., bld. 21, appt. 32",
                "category": {"category": "reader2", "discountPercentage": 25.0},
            },
            "rent_start_date": "2021-07-17 19:36:37",
            "expected_rent_end_date": "2021-09-16 17:09:06",
            "rent_end_date": "",
            "library_item": {
                "id": 2,
                "pledge_price": 51,
                "quantity": 12,
                "title": "Front-line dedicated local area network",
                "author": "Nickola Batalle",
                "genre": "sagittis",
            },
            "rent_price": 822,
            "fine_price": 324,
            "damage_level": {
                "id": 2,
                "level": "level2",
                "finePercentage": 25.0,
            },
        },
        {
            "id": 3,
            "user": {
                "id": 3,
                "name": "Hanifa",
                "surname": "Nicolai",
                "phoneNumber": "+380(0692)49-94-67",
                "address": "Ukraine, Priluki, Polova Vul., bld. 100, appt. 54",
                "category": {"category": "reader3", "discountPercentage": 15.0},
            },
            "rent_start_date": "2021-10-29 00:32:46",
            "expected_rent_end_date": "2021-12-22 22:35:21",
            "rent_end_date": "",
            "library_item": {
                "id": 3,
                "pledge_price": 59,
                "quantity": 37,
                "title": "Phased logistical emulation",
                "author": "Ritchie Saph",
                "genre": "nullam",
            },
            "rent_price": 527,
            "fine_price": 0,
            "damage_level": {
                "id": 3,
                "level": "level3",
                "finePercentage": 15.0,
            },
        },
        {
            "id": 4,
            "user": {
                "id": 5,
                "name": "Zaman",
                "surname": "Malloye",
                "phoneNumber": "+380(06562)4-00-63",
                "address": "Ukraine, Lviv, Naukova Vul., bld. 13, appt. 20",
                "category": {"category": "reader5", "discountPercentage": 25.0},
            },
            "rent_start_date": "2022-03-15 08:42:58",
            "expected_rent_end_date": "2022-05-18 12:17:33",
            "rent_end_date": "2022-03-23 00:51:16",
            "library_item": {
                "id": 4,
                "pledge_price": 398,
                "quantity": 9,
                "title": "Re-engineered demand-driven structure",
                "author": "Bendix Dunsmuir",
                "genre": "primis",
            },
            "rent_price": 342,
            "fine_price": 0,
            "damage_level": {
                "id": 4,
                "category": "level4",
                "finePercentage": 30.0,
            },
        },
        {
            "id": 5,
            "user": {
                "id": 4,
                "name": "Alden",
                "surname": "Gunnarr",
                "phoneNumber": "+380(0652)22-17-09",
                "address": "Ukraine, Kharkiv, Odeska Vul., bld. 2, appt. 26",
                "category": {"category": "reader4", "discountPercentage": 30.0},
            },
            "rent_start_date": "2022-01-17 13:23:07",
            "expected_rent_end_date": "2022-04-14 23:58:38",
            "rent_end_date": "2022-01-18 14:24:19",
            "library_item": {
                "id": 5,
                "pledge_price": 397,
                "quantity": 84,
                "title": "Ergonomic empowering success",
                "author": "Drusy Spaduzza",
                "genre": "neque",
            },
            "rent_price": 155,
            "fine_price": 0,
            "damage_level": {
                "id": 5,
                "level": "level5",
                "finePercentage": 45.0,
            },
        },
    ]
    return jsonify(rents)


@rents_bp.route("/<int:rent_id>", methods=["GET"])
def get_rent(rent_id: int):
    rent = {
        "id": rent_id,
        "user": {
            "id": 1,
            "name": "Kuipers",
            "surname": "Alkyone",
            "phoneNumber": "+380(048)69-85-63",
            "address": "Ukraine, Chernigiv, Starobіlouska Vul., bld. 33, appt. 69",
            "category": {"category": "reader1", "discountPercentage": 20.0},
        },
        "rent_start_date": "2022-02-19 18:09:33",
        "expected_rent_end_date": "2022-06-03 16:40:30",
        "rent_end_date": "2022-03-31 11:03:38",
        "library_item": {
            "id": 47,
            "pledge_price": 867,
            "quantity": 32,
            "title": "Right-sized interactive open architecture",
            "author": "Willey Bricknell",
            "genre": "vitae",
        },
        "rent_price": 352,
        "fine_price": 0,
        "damage_level": {
            "id": 3,
            "level": "level5",
            "finePercentage": 45.0,
        },
    }
    return jsonify(rent)


@rents_bp.route("/", methods=["POST"])
def create_rent():
    new_rent = request.get_json()
    new_rent["id"] = 123
    return jsonify(new_rent)


@rents_bp.route("/<int:rent_id>", methods=["PUT"])
def update_rent(rent_id: int):
    old_rent = {
        "id": rent_id,
        "user": {
            "id": 2,
            "name": "Micaela",
            "surname": "Stack",
            "phoneNumber": "+380(0542)34-17-38",
            "address": "Ukraine, Rivne, Shevchenko Vul., bld. 21, appt. 32",
            "category": {"category": "reader2", "discountPercentage": 25.0},
        },
        "rent_start_date": "2022-03-15 08:42:58",
        "expected_rent_end_date": "2022-05-18 12:17:33",
        "rent_end_date": "2022-03-23 00:51:16",
        "library_item": {
            "id": 4,
            "pledge_price": 398,
            "quantity": 9,
            "title": "Re-engineered demand-driven structure",
            "author": "Bendix Dunsmuir",
            "genre": "primis",
        },
        "rent_price": 342,
        "fine_price": 0,
        "damage_level": {
            "id": 4,
            "category": "level4",
            "finePercentage": 30.0,
        },
    }
    return jsonify(old_rent)


@rents_bp.route("/<int:rent_id>", methods=["DELETE"])
def delete_rent(rent_id: int):
    deleted_rent = {
        "id": rent_id,
        "user": {
            "id": 4,
            "name": "Alden",
            "surname": "Gunnarr",
            "phoneNumber": "+380(0652)22-17-09",
            "address": "Ukraine, Kharkiv, Odeska Vul., bld. 2, appt. 26",
            "category": {"category": "reader4", "discountPercentage": 30.0},
        },
        "rent_start_date": "2022-03-15 08:42:58",
        "expected_rent_end_date": "2022-05-18 12:17:33",
        "rent_end_date": "2022-03-23 00:51:16",
        "library_item": {
            "id": 4,
            "pledge_price": 398,
            "quantity": 9,
            "title": "Re-engineered demand-driven structure",
            "author": "Bendix Dunsmuir",
            "genre": "primis",
        },
        "rent_price": 342,
        "fine_price": 0,
        "damage_level": {
            "id": 4,
            "category": "level4",
            "finePercentage": 30.0,
        },
    }
    return jsonify(deleted_rent)
