# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Salam 👋 [{}](tg://user?id={})!**\n\n🤖Telegram Qruplarının və Kanallarının səsli söhbətlərində musiqi çalmaq üçün yaradılmış inkişaf etmiş bir botam. \n\n✅ Daha çox məlumat üçün mənə /help göndərin. "
      HELP_MSG = [
        ".",
f"""
**Hey 👋 Welcome back to {PROJECT_NAME}

⚪️ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**Setting up**

1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry

**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group

**Commands**

**=>> Song Playing 🎧**

- /play: Play the requestd song
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /dplay: Play song via deezer
- /splay: Play song via jio saavn
- /ytplay: Directly play song via Youtube Music

**=>> Playback ⏯**

- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",
        
f"""
**=>> Komutlar 🛠**

⚪️ For linked group admins only:

- /cplay [mahnı adı] - istədiyiniz mahnını səsləndirin
- /cdplay [mahnı adı] - deezer vasitəsilə istədiyiniz mahnını səsləndirin
- /csplay [mahnı adı] - jio saavn vasitəsilə istədiyiniz mahnını çalın
- /cplaylist - İndi ifa siyahısını göstər
- /cccurrent - İndi oynayan göstər
- /cplayer - musiqi pleyerinin ayar panelini açın
- /cpause - mahnı çalmağı dayandırın
- /cresume - mahnı ifasına davam et
- /cskip - növbəti mahnını oxudun
- /cend - musiqi çalmağı dayandırın
- /userbotjoinchannel - söhbətinizə köməkçi dəvət edin

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ Bağlı qrupda oynamaq istəmirsinizsə:

1) Kanal nömrənizi əldə edin.
2) Başlığı olan bir qrup yaradın: Kanal Musiqisi: kanalınız_kimi
3) Tam icazə ilə Kanal idarəçisi olaraq bot əlavə edin
4) Kanala admin olaraq @{ASSISTANT_NAME} əlavə edin.
5) Sadəcə qrupunuzdakı əmrləri göndərin.
""",

f"""
**=>> Diğər Komutlar🧑‍🔧**

-/musicplayer [on/off]: Musiqi pleyerini aktiv edin/deaktiv edin
- /admincache: Qrupunuzun admin məlumatlarını yeniləyir. Botun administratoru tanımadığını sınayın
- /userbotjoin: @{ASSISTANT_NAME} istifadəçi botunu söhbətinizə dəvət edin

**=>> Admin Komutları ⚔️**

- /userbotleaveall - köməkçini bütün söhbətlərdən silin
 - /gcast <mesaja cavab ver> - qlobal miqyasda brodcast bütün söhbətlərə mesajı cavablandırdı
 -/pmpermit [on/off] - pmpermit mesajını aktivləşdir/söndür
*Sudo İstifadəçiləri istənilən qrupdakı istənilən əmri yerinə yetirə bilərlər

"""
      ]
