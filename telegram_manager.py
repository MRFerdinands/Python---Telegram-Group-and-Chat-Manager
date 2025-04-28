from telethon import TelegramClient, sync
from telethon.tl.types import Channel, Chat, User, Dialog
import asyncio
import os
import getpass
import platform

# ANSI color codes
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    """Clear the terminal screen based on the operating system."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

async def process_groups(client, groups):
    if groups:
        print(f"\n{Colors.BOLD}Found {len(groups)} groups/channels:{Colors.END}")
        
        for i, group in enumerate(groups, 1):
            group_name = group.name
            print(f"{i}. {Colors.BLUE}{group_name}{Colors.END}")
            leave_input = input(f"   Leave this group? (Y/n): ") or "y"
            
            if leave_input.lower() == "y":
                try:
                    await client.delete_dialog(group.entity)
                    print(f"   {Colors.GREEN}Successfully left {group_name}{Colors.END}")
                except Exception as e:
                    print(f"   {Colors.RED}Error leaving {group_name}: {e}{Colors.END}")
    else:
        print(f"{Colors.YELLOW}No groups found!{Colors.END}")
    
    input(f"\n{Colors.CYAN}Press Enter to return to the main menu...{Colors.END}")
    clear_screen()

async def process_chats(client, chats):
    if chats:
        print(f"\n{Colors.BOLD}Found {len(chats)} private chats:{Colors.END}")
        
        for i, chat in enumerate(chats, 1):
            user = chat.entity
            chat_name = f"{user.first_name} {user.last_name if user.last_name else ''}"
            print(f"{i}. {Colors.PURPLE}{chat_name.strip()}{Colors.END}")
            delete_input = input(f"   Delete this chat? (Y/n): ") or "y"
            
            if delete_input.lower() == "y":
                try:
                    await client.delete_dialog(chat.entity)
                    print(f"   {Colors.GREEN}Successfully deleted chat with {chat_name.strip()}{Colors.END}")
                except Exception as e:
                    print(f"   {Colors.RED}Error deleting chat: {e}{Colors.END}")
    else:
        print(f"{Colors.YELLOW}No private chats found!{Colors.END}")
    
    input(f"\n{Colors.CYAN}Press Enter to return to the main menu...{Colors.END}")
    clear_screen()

async def show_menu(client):
    clear_screen()
    
    while True:
        # Get all dialogs (conversations)
        print(f"{Colors.CYAN}Fetching your conversations...{Colors.END}")
        dialogs = await client.get_dialogs()
        
        # Separate groups and private chats
        groups = []
        chats = []
        
        for dialog in dialogs:
            entity = dialog.entity
            if isinstance(entity, (Channel, Chat)) and not isinstance(entity, User):
                groups.append(dialog)
            elif isinstance(entity, User):
                chats.append(dialog)
        
        print(f"\n{Colors.BLUE}{Colors.BOLD}Telegram Group and Private Chat Manager{Colors.END}")
        print(f"{Colors.CYAN}Select an action:{Colors.END}")
        print(f"1. {Colors.BLUE}Leave groups ({len(groups)} available){Colors.END}")
        print(f"2. {Colors.PURPLE}Delete private chats ({len(chats)} available){Colors.END}")
        print(f"3. {Colors.RED}Exit{Colors.END}")
        
        action = input(f"Enter your choice (1/2/3): ")
       
        if action == "1":
            clear_screen()
            await process_groups(client, groups)
                
        elif action == "2":
            clear_screen()
            await process_chats(client, chats)
        
        elif action == "3":
            clear_screen()
            print(f"{Colors.GREEN}{Colors.BOLD}Exiting program. Goodbye!{Colors.END}")
            break
        
        else:
            print(f"{Colors.RED}Invalid choice. Please try again.{Colors.END}")
            await asyncio.sleep(1)
            clear_screen()

async def main():
    clear_screen()
    print(f"{Colors.BOLD}{Colors.BLUE}Telegram Group and Chat Manager{Colors.END}")
    print(f"{Colors.CYAN}Please enter your credentials:{Colors.END}\n")
    
    # Get user credentials
    api_id = input("Enter your Telegram API ID: ")
    api_hash = input("Enter your Telegram API hash: ")
    phone = input("Enter your phone number (with country code): ")
    
    # Create the client
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(phone)
    
    # Ensure we're connected
    if not await client.is_user_authorized():
        print(f"{Colors.RED}Authentication failed. Please try again.{Colors.END}")
        await asyncio.sleep(2)
        return
    
    print(f"{Colors.GREEN}Successfully logged in!{Colors.END}")
    await asyncio.sleep(1)
    
    # Show main menu
    await show_menu(client)
    
    # Disconnect when done
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
