from pyrogram import Client
from pyrogram import filters
from ZelzalMusic import app

#SouRce Teto
@app.on_message(filters.text)
async def delete_text(client, message):
    word_list = ["سكس", "خول", "شرموط", "معرص", "ابن خول", "متناكه", "شرموط", "احا", "نيك", "انيكك", "مصه", "قحبه", "قحاب", "نودز", "يبن المتناكه", "يبن الشرموطه", "كسمك", "كسمينك", "شاذ", "بحب امك", "طيزك", "تع يكسمك", "انت متناك", "كسمين امك", "يبن الزانيه", "امك شرموطه", "اختك شرموطه", "بحب امك", "يكسمك", "يبن المره", "يلبوه", "دين امك", "هركب دين امك", "زبي", "كس", "قضيب", "سحاقه", "تيزك", "نيكني", "يبن الوسخه", "شرموطه", "كسمين امك", "يشاذ", "انت ترموطه", "كسمك يبت", "كسمك يلا", "وريني طيزك", "كسك", "هايجه", "هايج", "زبري", "بزك", "بزازها", "انيكها", "يالبوه", "كسها", "نجيبهم كول", "نجيبهم سوا", "سحاق", "هدخله كله", "هدخله براحه", "هدخله جامد", "عايز انيكك", "بحب النيك", "عايزه جاد"]
    if message.text in word_list:
        await client.delete_messages(message.chat.id, message.id)
        await client.send_message(message.chat.id, f"↢ ممنوع السب {message.from_user.first_name}")
