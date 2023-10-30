﻿
init python:
    InventoryList = []
    ChoiceChecker = [] 
    Character1 = {}
    AnxietyMeter = 0
    Batterymeter = 0 

#screen Thoughts():
    #frame:
        #xysize (150, 150)
        #align (1.0, 0.0)
        #vbox:
            #xalign 0.25
            #yalign 0.0
            #python:
                #k = 0
                #kcount = InventoryList.count
                #while k != kcount:                        
                    #print(Thoughts[k] + "\n")

label start():


    "Вокруг Вас звучит оглушающий звук сирены. Где-то сверху угрожающе потрескивают провода. Ваша голова раскалывается. Кажется, что Ваше тело было под влиянием гидравпресса. Или грузовика. \nСпустя пару минут – часов? – вы находите в себе силы открыть глаза. Вашему вниманию предстает темная комната, освещаемая лишь мигающими красными фонарями тревоги."
    "Несмотря на нежелание тела совершать какие-либо движения, Вы заставляете его двигаться и медленно садитесь, опираясь спиной на металлическую стену за вами."
    menu Room1:           
        ">осмотреть комнату" if 'Room1Check' not in ChoiceChecker:
            "Вы прищуриваетесь и более внимательно вглядываетесь в плохо освещенное пространство перед Вами. Около Вас находится выдернутый из пола металлический письменный стол. То, что послужило причиной его нынешнего состояния, действовало с такой силой, что большинство ящиков вылетело наружу. Внутри них виднеются очертания стопок холопланшетов.\nНа стене напротив висит еле светящийся холомонитор. Кажется, что он был минимально поврежден. Поверх его домашней страницы висит красное окошко неизвестной тебе ошибки."    
            $ ChoiceChecker.append('Room1Check')

        ">рассмотреть обломки стола" if 'TableCheck' not in ChoiceChecker and 'Room1Check' in ChoiceChecker:
            "Начиная рассматривать пространство рядом со столом, вы натыкаетесь на огромное количество безделушек и рассыпанных холопланшетов. Большинство из них не пережило катастрофы. Вы с разочарованием кидаете их все в одну большую кучу сломанных вещей."
            "Расследование содержимого выпавших ящиков приносит больше плодов. Из-за дополнительной защиты многие холопланшеты остались в рабочем состоянии. Методом проб и ошибок Вы смогли их включить. На планшетах хранится огромное количество информации; каждый из них раскидывает в воздух целый веер заполненных текстом и диаграммами окон. Незнание языка только ухудшает Ваше желание понять, о чем именно идет речь. Вы аккуратно складываете работающие холопланшеты в стопку, оставляя пару из них включенными: свет голограммных окон делает все вокруг менее пугающим и темным."
            "Нижние ящики остались внутри остова стола; это заставляет Вас на мгновение задуматься. Быстрый взгляд в верхние из них показывает вам разнообразие инструментов и запечатанных упаковок гипоспреев. Вы принимаете решение не церемониться и полностью разграбить ящики из пазов."
            $ ChoiceChecker.append('TableCheck')
            jump Table

        ">прочитать документы в голоплашетах" if 'TranslatorCheck' in ChoiceChecker and 'DocsCheck' not in ChoiceChecker:
            "Первый документ - тот, за который зацепились Ваши глаза, - кажется чьим-то дневником. Не то чтобы Вы хотели его читать, но Вы были слишком удивлены тем, что вы {i}можете{/i} читать. Тем более, кажется, что это был дневник обладателя стола.\nВы также помните, что клали на верх стопки работающих голограммных планшетов один, содержащий большое количество схем чего-то сильно механического."
            jump Documents
            if 'TechdocCheck' in ChoiceChecker and 'DiaryCheck' in ChoiceChecker:
                "Вы тратите еще несколько минут на то, чтобы хотя бы прочитать первую строчку всех документов, которые казались вам интеремными тогда, когда Вы не могли понять, что было написано, но не находите ничего полезного."
                $ ChoiceChecker.append('DocsCheck')
                   
        ">открыть сейф" if 'DiaryCheck' in ChoiceChecker and 'SafeCheck' not in ChoiceChecker:
            $ password = renpy.input("Вы повторяете описанные в дневнике действия для активации панели ввода пароля.").strip()
            if password == "1486":
                "С легким щелчком, дверка сейфа отъезжает в сторону. \nВнутри лежит белый - и, на взгляд, легкий, - станнер в кабуре. Он подозрительно сильно напоминает вам своим видом пистолет."
                "Осторожно достав и проверив, что станнер переведен в состояние покоя, вы прикрепляете кабуру к своему поясу."
                $ ChoiceChecker.append('GunCheck')
                $ ChoiceChecker.append('SafeCheck')
            else:
                "Панель ввода сливается с одной из стенок сейфа. Сейф отказывается открываться."
            jump Room1

        ">понять, что у вас есть на себе" if 'SelfCheck' not in ChoiceChecker:
            "Вы неловко охлапываете свою одежду, пытаясь не потревожить ноющее тело больше, чем нужно. Плотно прилегающая тяжелая ткань не оставляет пространства для скрытых карманов; эта одежда чем-то напоминает Вам гидрокостюм, - если бы гидрокостюм был создан для постоянного ношения.\nВаше внимание привлекает инструментый пояс - к нему прикреплены {i}перчатки{/i} и маленькая сумка. Внутри нее вы находите {i}идентификационную карту{/i}, - Вы не можете прочитать, что на ней написано, но почему-то совершенно точно уверены в том, чем она является, - {i}электрический паяльник{/i} и {i}4 универсальные батареи{/i}."
            $ InventoryList.append("перчатки")
            $ InventoryList.append("электрический паяльник")
            $ InventoryList.append("f{Batterymeter} universal batteries")
            $ ChoiceChecker.append('SelfCheck')
            $ Batterymeter = Batterymeter + 4
        
        ">попытаться вспомнить, что произошло" if 'MemoryCheck' not in ChoiceChecker:
            "Вы тратите несколько мгновений на то, чтобы покопаться в собственном мозгу. Вместо воспоминаний из прошлого Вас встречает матовая пустота. Вы уверены, что Там что-то было, но каждый раз, когда Вы пытаетесь сосредоточиться на чем-то конкретном, оно перестает существовать. В вашей памяти существует только взрыв, запах гари и темнота комнаты, в которой Вы открыли глаза. Вы не уверены в том, что Вы знаете. Вы не уверены в том, что Вы умеете. Вы не понимаете, как Вы здесь оказались."
            $ ChoiceChecker.append('MemoryCheck') 
            jump AnxietyRoom1 
        ">подойти к холотерминалу" if 'TerminalCheck' not in ChoiceChecker:
            "Пошатываясь и иногда останавливаясь из-за кружащейся головы, Вы доходите до терминала."
            if 'TranslatorCheck' not in ChoiceChecker:
                "Присматриваясь к надписям на экране терминала, Вы с подступающим ужасом понимаете, что не можете ничего прочитать. Несмотря на то, что холотерминал - На Ваш взгляд, - выглядит рабочим, вы не решаетесь как-либо с ним взаимодейстовать. Вы не знаете, чего Вы ожидали, но, почему-то, Вы ощущаете призрак разочарования."
            else:
                jump Terminallabel
        ">выйти из комнаты":            
            jump coridor

    jump Room1 
    return

    menu Table:
        ">достать верхний ящик" if 'Table1Check' not in ChoiceChecker:
            "Верхний ящик практически пуст; его большую часть занимает вмонитрованный плоский сейф, который остался закрытым несмотря на все произошедшее. Рядом с дверкой сейфа лежит вытянутый черный цилиндр. При взгляде на него Вам кажется, что его черная сущность как будто поглощает свет."
            "Цилиндр кажется полной противоположностью вещей, которые ощущаются неправильными из-за того, что не принадлежат месту, в котором они находятся. Он принадлежит этому месту гораздо больше, чем само место. С каждой секундой само место вокруг Вас становится черным цилиндром. \nВы отводите взгляд и пытаетесь как можно быстрее и осторожнее поставить ящик с цилиндром на пол, но цилиндр оказывается быстрее. Как будто заметив Ваше внимание к нему, он еще сильнее вытягивается в длину, и, как ожившая гусеница, начинает стремительно ползти в сторону Вашей руки. "
            "Вы не успеваете среагировать. Он оборачивается вокруг пальцев и начинает медленно подниматься вверх. То, чего коснулась его темнота, на мгновение перестает существовать. Когда темнота доходит до головы, она на мгновение замирает, и у Вас появляется момент для испытания паники. В следующую секунду она накрывает Вас полностью."
            "Когда темнота наконец решает пропасть, она оставляет Вас дрожащими от холода и с пониманием того, что что-то было изменено. Вы не можете сказать, что именно, но Вы что-то потеряли. \nЯщик вываливается из Ваших рук, и Вы еле успеваете отпрыгнуть от него в сторону. Вы наклоняетесь над ним и осторожно проверяете его на наличие цилиндра. Ящик, - за исключением все еще существующего внутри него сейфа, - теперь является пустым."
            "Пытаясь понять произошедшее, Вы позволяете вашему взгляду блуждать по комнате, выхватывая незначительные детали. Он останавливается на светящихся холопадах; Вам требуется несколько минут для осознания, но потом происходящее ударяет Вас со всей силы: Вы понимаете смысл написанного."
            $ ChoiceChecker.append('Table1Check')
            $ ChoiceChecker.append('TranslatorCheck')
            jump Table
        ">достать ящик с медикаментами" if 'Table2Check' not in ChoiceChecker:
            if 'TranslatorCheck' in ChoiceChecker:
                "Вы прищуриваетесь, пытаясь разобрать мелкий текст на упаковке. Описание наполнено профессиональным жаргоном, но Вам удается понять, что данные применение данных гипоспреев необходимо для нахождения в инженерной комнате. Описание также подчеркивает, что новый гипоспрей надо вводить каждые две минуты, и что за раз не рекомендуется применять больше, чем пять гипоспреев. \nПокопавшись в ящике, Вы находите самую свежую неоткрытую пачку гипоспреев. Она легко помещается в поясную сумку."
            if 'TranslatorCheck' not in ChoiceChecker:
                "Вы навскидку берете первую попавшуюся пачку гипоспреев из ящика. Вам не знакомен язык, но Вы все равно пытаетесь понять хотя бы капельку информации из наполненных неизвестными символами предложений. Кажется, что данные гипо помогают от чего-то, что могло убить человека за очень короткое время? Вы тратите несколько минут, пытаясь сопоставить классификационные знаки с тем, что есть в Вашей голове, но просветление не приходит. Вы с досадой закидываете первую попавшуюся пачку гипоспреев в поясную сумку."
            $ ChoiceChecker.append('HypoCheck')
            $ ChoiceChecker.append('Table2Check')
            jump Table
        ">достать ящик с инструментами" if 'Table3Check' not in ChoiceChecker:
            "эТО ОЧЕНЬ тяжелый ящик. Вы еле вытаскиваете из пазов. Каждую секунду, которую вы тратите на данное действие, вы спрашиваете себя, действительно ли Вам это нужно. Вашему телу совершенно не нравится происходящее. Вы ощущаете себя полностью выдавленными.\nВнутри находится огромное количество видавших лучшие дни инструментов. Они совершенно Вам непонятны и неизвестны. Вы ощущаете себя уставшими. Возможно, внутри этого ящика и находится что-то нужное, но у Вас совершенно нет сил копаться внутри этого монстра."
            if AnxietyMeter>0:
                "Вы несколько минут смотрите на ящик, думая, стоит ли Вам пытаться что-то в нем найти. Устаревшая, помятая техника внутри ящика не внуушает Вам надежды на нахождение чего-то полезного; тем более, Вы и так уже потеряли из-за него много времени.\nВы отходите от него в сторону."
            else:
                "В любом случае, инстинкты требуют от Вас сделать хотя бы попытаться предпринять все, может помочь Вам выжить.\nВы переворачивате ящик на бок и смотрите, как все его содержимое выплескивается на пол. Ваш взгляд зацепляется за немного громоздкую, как будто не сочетающуюся со всей остальной станцией форму старого фонаря. Заинтересовавшись, Вы подбираете фонарь для его осмотра. Несмотря на его возраст, кажется, что даже этот старый инструмент может работать от универсальных батарей из Вашей сумки."
                "Вы экспериментально засовываете внутрь две батарейки и нажимаете на кнопку включения. К Вашему удивлению, он освещает пространство вокруг мягким желтым светом."
                "Крепко зажимая фонарь в руке и чувствуя себя немного увереннее, Вы продолжаете свое исследование комнаты."
                $ Batterymeter = Batterymeter - 2
            $ ChoiceChecker.append('Table3Check')
            $ InventoryList.append('фонарик')
            jump Table
        "решить заняться чем-то другим":
            jump Room1


    menu Documents:
        "просмотреть дневник владельца стола" if 'DiaryCheck' not in ChoiceChecker:
            "Данный дневник принадлежит исследователю Йогран Эт-ал. Кажется, что сначала этот файл начинался как черновик официального исследования нового типа реактора, но с течением времени он становился все менее и менее вычитанным и лишенным человеческих чувств.\nЙогран описывает исследование возможностей реактора, основанного на взаимодействии с вне-реальной силой и соединении с выбранными сферами миров. Она говорит о реакторе как о прекрасном примере, доказывающем теории, лежащие в основании ее поля науки. Несмотря на ее восхищение, она также призывает к осторожному и вдуманному обращению с реактором. Чем ближе Вы приближаетесь к концу документу, тем подозрительнее и резче Йогран отзывается в сторону реактора и окружающих его людей."
            "Йогран также упоминает, что для достижения результатов, удовлетворяющих спонсирующую исследования кампанию, станция решает увеличить количество экспериментов и, также, значительно облегчает правила безопасности для работы с реактором. В какой-то момент она начинает каждый день описывать изменения, которые, как ей кажется, начинают охватывать станцию. С каждым днем количество изменений растет, и в определенный момент Йогран останавливается из-за того, что уже не может вспомнить, какой станция - и ее обитатели, - были в самом начале, и даже ее записи и многочисленные сохраненные видео из прошлого не помогают так, как должны."
            "Она все еще точно уверена в том, что большинство находящихся сейчас на станции личностей не были здесь с самого начала запуска станции, и что их количество и состав меняются изо дня в день. Ее мысли сбивчивы, и она начинает вносить в файл изменения, которые она начинает замечать в себе."
            "В одной из последних записей Эт-ал в приступе ясности - или очередного изменения, - говорит о том, что она смогла пробиться к серверу межстанционного сообщения и заказать боевой станнер. Она не уверена ни в том, что он дойдет (в одной из ее теорий она упоминает о том, что, возможно, в определенный момент сама станция пропадет из ее привычных космических координат), ни что она будет помнить, для чего он ей был нужен, ни то, куда она его хотела спрятать. С этого момента она начинает ежедневно заносить в файл способ открыть сейф, спрятанный в ящике ее стола, и код к нему. К концу прочтения дневника Вы уже наизусть помните и действия для активации панели ввода кода, и сам код - 1486."
            $ ChoiceChecker.append('DiaryCheck') 
            jump Documents
        "просмотреть очень технический документ" if 'TechdocCheck' not in ChoiceChecker:
            "оно должно давать объяснения того, что нужно делать в комнате с реактором, но типо. она все равно не сделана. пасхалка лмао"
            jump Documents
            $ ChoiceChecker.append('TechdocCheck') 
        "решить заняться чем-то другим":
            jump Room1
        
    menu AnxietyRoom1:
        ">погрузиться в свой страх":
            "Вас охватывает страх. Вы не можете двигаться. Каждый вздох и выдох становится тем, что Вам приходиться с огромным усилием напоминать себе делать. У Вас начинает раскалываться голова. "
            "Вы не понимаете, сколько Вам потребовалось времени для того, чтобы прийти в себя. Вы не знаете, хотите ли Вы это знать."
            $ AnxietyMeter = AnxietyMeter + 1
            jump Room1
        
        ">попытаться успокоиться":
            "Чувствуя подступление панической атаки, Вы сосредотачиваетесь на своем дыхании. Пока что лучше не думать о том, что было в прошлом."
            jump Room1

label Terminallabel():
    "Подойдя к экрану терминала, Вы понимаете, что можете без труда понять смысл висящего перед Вами окна ошибки. Терминал требует перезагрузки для перехода на альтернативный способ питания для нормальной работы системы."
    "Спустя нескольких минут Вы находите кнопку перезагрузки - или то, что Вы отчаянно хотите считать кнопкой перезагрузки. \nПомолившись Космосу, Вы нажимаете на кнопку и надеeтесь на лучшее."
    "Терминал погружается в темноту, и Вы задерживаете дыхание. Через несколько секунд терминал издает тонкий писк и включается опять."
    "{i}{b}Привествуем Вас в системе управления и взаимодействия со станцией! В данный момент большинство возможностей системы терминала недоступно. Данный терминал может предоставить доступ к своему хранилищу и мануалам по действиям в экстренных случаях.\nНачинаю авторизацию пользователя для предоставления персонализированной помощи... {/i}{/b}"
    "Терминал замолкает. Когда его голос раздается снова, Вы отчетливо слышите в нем запрограмированные эмоции непонимания и, немного, стыда."
    "{i}{b}Прошу прощения. Мои сканеры распознают Вашу идентификационную карту как принадлежащую данной станции, но также не могут прочитать что-либо более конкретное.{/i}{/b}"
    "{i}{b}В последнее время у нас были... неполадки с базой данных сотрудников. Катастрофа могла оказать на нее еще большее влияние. Прошу Вас назвать свои учетные данные. Учитывая происходящую ситуацию, если они не будут совпадать с учетными данными уже существующего пользователя, будет создан временный новый профиль.{/i}{/b}" 
    $ nameinp = renpy.input("Перед Вами выскакивает голограммное окно, просящее ввести Ваше имя.").strip().capitalize()
    if any(symbol.isdigit() for symbol in nameinp):
        "{i}{b}О, неожиданно встретить последователя нумеризации так далеко от Центра! Надеюсь, у нас в будущем будет время поговорить о философии именования среди разных культур и видов.\nВ любом случае, Ваш аккаунт был создан!{/i}{/b}"
    elif nameinp == "":
        "{i}{b}Хм, отсутствие имени? Возможно, с Бета-карл-один... Прошу прощения, я должен дать Вам временное обозначение для аккаунта. Автоматически ввожу обозначение Ноль.{/i}{/b}"
        $ nameinp = "Ноль"
   
    elif nameinp == "Йорган" or "Йорган Эт-ал":
        "{i}{b}Файл с Вашими данными был найден, мк. Йорган Эт-ал! Вашей карте дана возможность взаимодейстововать с комнатой 4590 и лабораторией 01.{/i}{/b}"
        $ ChoiceChecker.append('Yaccess')
    else:
        "{i}{b}Временный аккаунт был создан.{/i}{/b}"
    "{i}{b}В связи с экстренной ситуацией был максимально повышен уровень доступа Вашей идентификационной карты. теперь вы имеете полный контроль над всем, что входит в систему станции. {/i}{/b}"
    $ Character1["name"] = nameinp
    "{i}{b}[Character1[name]], прошу сконцентрировать Ваше внимание на обновлении статуса реактора и его выключении. \nЕсли Вам нужна какая-либо помощь, обращайтесь ко мне! {/i}{/b}"
    #menu Terminal:
        #"Попросить "
    return 
label coridor():
    "nothing here for now"    
