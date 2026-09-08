import json

FILE_NAME = "youtube.txt"

def load_data():
    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    except FileNotFoundError:
            return []

def save_data_helper(videos):
    with open(FILE_NAME,"w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video["name"]}, Duaration {video["time"]}")
    print("*" * 70)
    print("\n")

def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    videos.append({"name":name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video no to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index -1] = {"name":name, "time":time}
        save_data_helper(videos)
    else:
        print("Invalid index selected.")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to delete: "))
    if 1 <= index <= len(videos):
        pop = videos.pop(index-1)
        print(f"{pop} deleted from the list")
        save_data_helper(videos)
    else:
        print("Invalid index selected.")

def main():
    videos = load_data()
    while True:
        print("\n **Youtube Manager**")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        print("")
        choice = input("Enter Your choice: ")
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid number")


if __name__ == "__main__":
    main()