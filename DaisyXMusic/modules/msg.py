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
** Hey Xoş gəlmisiniz {PROJECT_NAME}

⚪️ {PROJECT_NAME} qrupunuzun səsli söhbətində və kanal səsli söhbətlərində musiqi oxuya bilər

⚪️ Köməkçi adı >>  @{ASSISTANT_NAME} \n \n Təlimatlar üçün növbəti düyməni basın**
""",

f"""
**Ayarlamaq**

1) Bot idarəçisi olun (cplay istifadə edərsə qrupda və kanalda)
2) Səsli söhbətə başlayın
3) Bir admin tərəfindən ilk dəfə [mahnı adı] sınayın /çalın
*) İstifadəçi botu qoşulubsa, musiqidən zövq alın, @{ASSISTANT_NAME} qrupunuza əlavə edilməyibsə yenidən cəhd edin

** Kanal Musiqisi üçün **
1) Məni kanalınızın idarəçisi edin
2) Bağlı qrupa /userbotjoinchannel göndərin
3) İndi əlaqəli qrupda əmrlər göndərin

**Komutlar**

**=>> Mahnı Çalma 🎧**

- /play: İstədiyiniz mahnını səsləndirin
- /play [yt url]: Verilmiş yt urlini oxudun
- /play [səsə cavab ver]: Cavab verilən səsi oxudun
- /dplay: Mahnını deezer vasitəsilə çalın
- /splay: Jio saavn vasitəsilə mahnı oxudun
- /ytplay: Birbaşa Youtube Music vasitəsilə mahnı oxudun

**=>> Musiqi Zamanı ⏯**

- /player: Playerin Ayarlar menyusunu açın
- /skip: Musiqini atlayır
- /pause: Parçanı durdur
- /Resume: Durdurulan parçanı davam etdirir
- /end: Medianın oxunmasını dayandırır
- /current: Mövcud Musiqi parçasını göstərir
- /playlist: çalğı siyahısını göstərir
Player Komutu və /play, /current və /playlist istisna olmaqla bütün digər Komutlar yalnız qrup rəhbərləri üçündür.
""",
        
f"""
**=>> Komutlar 🛠**

⚪️ Yalnız əlaqəli qrup rəhbərləri üçün:

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

Komut əvəzinə kanal da istifadə edilə bilər ( /cplay = /channelplay)

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
Sudo İstifadəçiləri istənilən qrupdakı istənilən əmri yerinə yetirə bilərlər

"""
      ]
