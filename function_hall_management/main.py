from constants import CITIES
from storage import initialize_storage, save_all_data, halls_manager, get_halls_in_city, create_sample_hall_if_empty
from logger import log_event
from utils import format_currency, get_rating_stars, action_logger
from auth import authenticate, register_user
from models.user import User
import os
from typing import Optional

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu(user: Optional[User]):
    print("\n" + "═"*60)
    print("  FUNCTION HALL BOOKING SYSTEM  ".center(60))
    print("═"*60)
    if user:
        print(f"Logged in → {user.name} ({user.role.title()})")
        if user.is_owner:
            print(f"  You own {len(user.halls_owned)} hall(s)")
        elif user.is_customer:
            print(f"  You have {len(user.bookings or [])} booking(s)")
        print("─"*60)

    print("1. Browse all halls")
    print("2. Search by city")
    print("3. View hall details")
    if user:
        if user.is_owner:
            print("4. My halls (owner)")
            print("5. Add new hall (owner – dummy)")
        else:
            print("6. My bookings (customer – placeholder)")
    print("7. Login" if not user else "7. Logout")
    print("8. Register")
    print("0. Exit")
    print("─"*60)


@action_logger
def show_hall_details(hall_id: str):
    hall = halls_manager.get_hall(hall_id.upper())
    if not hall:
        print("Hall not found.")
        return

    print(f"\n{hall.name}  [{hall.id}]")
    print(f"  {hall.city}, {hall.area} • {hall.capacity} pax")
    print(f"  Base: {format_currency(hall.base_price_per_person)} / person")
    print(f"  {get_rating_stars(hall.average_rating)}  ({hall.review_count} reviews)")
    print(f"\n  {hall.description}")
    print("\nFeatures: " + ", ".join(sorted(hall.features)))
    print("\nPackages:")
    for name, pkg in hall.packages.items():
        print(f"  {name.title():<12} ₹{pkg['price_per_person']:,}  →  {', '.join(pkg['includes'])}")


@action_logger
def owner_my_halls(user: User):
    if not user.is_owner:
        print("Only owners can access this.")
        return

    owned = halls_manager.get_owner_halls(user.id)
    if not owned:
        print("You have no halls yet.")
        return

    print("\nYour Halls:")
    for h in owned:
        print(f"• {h.name} ({h.city}) – {h.rating_display}")


def main():
    initialize_storage()
    log_event("app_started")
    current_user: Optional[User] = None

    while True:
        clear_screen()
        display_menu(current_user)
        choice = input("Choice: ").strip()

        if choice == "0":
            save_all_data()
            print("\nGoodbye!\n")
            break

        elif choice == "1":
            if len(halls_manager) == 0:
                print("No halls registered yet.")
            else:
                for h in sorted(halls_manager._halls.values(), key=lambda x: x.base_price_per_person):
                    print(f"[{h.id}] {h.name} • {h.city} • {format_currency(h.base_price_per_person)}")

        elif choice == "2":
            city = input("City: ").strip().title()
            matches = get_halls_in_city(city)
            print(f"\n{len(matches)} hall(s) in {city}")
            for h in matches:
                print(f"• {h.name} ({h.area}) – {h.rating_display}")

        elif choice == "3":
            hid = input("Hall ID: ").strip()
            show_hall_details(hid)

        elif choice == "4" and current_user and current_user.is_owner:
            owner_my_halls(current_user)

        elif choice == "5" and current_user and current_user.is_owner:
            create_sample_hall_if_empty(current_user)

        elif choice == "7":
            if current_user:
                print(f"Goodbye, {current_user.name}!")
                current_user = None
            else:
                email = input("Email: ").strip()
                pwd = input("Password: ").strip()
                success, user, msg = authenticate(email, pwd)
                print(msg)
                if success:
                    current_user = user

        elif choice == "8":
            role = input("customer / owner: ").strip().lower()
            if role not in ("customer", "owner"):
                print("Invalid role.")
                continue
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            phone = input("Phone: ").strip()
            pwd = input("Password: ").strip()
            success, msg = register_user(role, name, email, phone, pwd)
            print(msg)

        else:
            print("Invalid or unavailable choice.")

        input("\nPress Enter…")


if __name__ == "__main__":
    main()