from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, LikeEvent, JoinEvent, GiftEvent, LiveEndEvent, FollowEvent

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@alaixmc")


# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)

# Notice no decorator?
async def on_comment(event: CommentEvent):
    fic1 = open("chat.txt", "w", encoding="utf-8")
    fic1.write("[0] " + event.user.nickname + ": " + event.comment + "\n")


@client.on("like")
async def on_like(event: LikeEvent):
    fic2 = open("like.txt", "w", encoding="utf-8")
    fic2.write(f"[0] {event.user.nickname}") 

@client.on("join")
async def on_join(event: JoinEvent):
    fic3 = open("join.txt", "w", encoding="utf-8")
    fic3.write(f"[0] {event.user.nickname}") 

@client.on("gift")
async def on_gift(event: GiftEvent):
    # If it's type 1 and the streak is over
    if event.gift.gift_type == 1 and event.gift.repeat_end == 1:
        print(f"{event.user.uniqueId} qui à envoyer {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\"")
        fic4 = open("giftr.txt", "w", encoding="utf-8")
        fic4.write(f"[0] {event.user.uniqueId} qui à envoyer {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\"") 


    # It's not type 1, which means it can't have a streak & is automatically over
    elif event.gift.gift_type != 1:
        print(f"{event.user.uniqueId} qui à envoyer \"{event.gift.extended_gift.name}\"")
        fic5 = open("giftr.txt", "w", encoding="utf-8")
        fic5.write(f"[0] {event.user.uniqueId} qui à envoyer {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\"") 

@client.on("follow")
async def on_follow(event: FollowEvent):
    fic6 = open("follow.txt", "w", encoding="utf-8")
    fic6.write(f"[0] {event.user.nickname}") 


# Define handling an event via "callback"
client.add_listener("comment", on_comment)

if __name__ == '__main__':
    client.run()