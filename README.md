<h1 align="center"><img src="Images\photo_2024-04-15_20-49-37.jpg" height="100" /></h1>
<h1 align="center">Команда COZYDUKE</a> 


## Состав команды:
 - Бадретдинова Рушания
 - Гайсина Лиана 
 - Казаченко Екатерина
 - Кириленков Кирилл
 - Кирсанов Вадим
 - Федеряев Клим

## Кейс

**ПАО «Газпром Нефть»**
Подробное описание кейса можно найти по [ссылке](Задача_хакатона.md)

**Цель проекта:** Разработка веб-сервиса, который будет автоматически анализировать тексты двух документов, искать соответствие между ними и присваивать статус соответствия

**Задачи проекта:**

1) Разработка модели для автоматического анализа текста двух документов
2) Разработка модели для поиска соответствия между текстовыми документами 
3) Вывод по результатам работы модели списка пар требований и соответствующих им характеристик с пометкой о полном или частичном соответствии или несоответствии
3) Разработка критерия для оценки соответствия и принятия решения о присвоении статуса соответствия (соответствии/частичном соответствии/несоответсвии документов)
4) Финальное оформление веб-сервиса с возможностью загрузки сравниваемых документов  

## Инструкция по разворачиванию каждого модуля прототипа системы
Итоговое решение [по ссылке](https://github.com/Kirilenkov/docx_semantic_similarity/blob/main/Cozyduke_v2.ipynb)
А также по [ссылке в Google Colab](https://colab.research.google.com/drive/1awWW0mdWqpveewJf0CDHcWKQgD8N_MH1?usp=sharing)
Черновик решения можно посмотреть по [ссылке](https://github.com/Kirilenkov/docx_semantic_similarity/blob/main/Cozyduke.ipynb)

## Анализ имеющихся моделей для решения задачи сопоставления требований с характеристиками и оценки степени удовлетворения требованию

Обработка естественного языка *(Natural Language Processing, NLP)* — пересечение машинного обучения и математической лингвистики, направленное на изучение методов анализа и синтеза естественного языка. В задачи NLP может входить распознавание текста, выделение слов, синтаксический разбор, токенизация предложений, 
Извлечение отношений, аннотация документа и анализ тематики. Для решения задач сопоставления документов могут быть рассмотрены следующие направления NLP: 
     - Векторизация
     - Дедубликация
     - Семантический анализ

### *Модели для Векторизации*
Эти модели используются для преобразования текста в числовой формат, который могут обрабатывать алгоритмы машинного обучения.

#### TF-IDF (Term Frequency-Inverse Document Frequency)
TF-IDF - это статистическая мера, используемая для оценки важности слова в документе, который является частью корпуса. Она увеличивается пропорционально числу раз, когда слово появляется в документе, но подавляется частотой слова в корпусе. Это помогает в выделении слов, важных для конкретного документа, но не обязательно для всего корпуса.

Преимущества:
 - Учитывает не только частоту слова в документе, но и обратную частоту документа, что помогает уменьшить влияние часто встречающихся, но малоинформативных слов.
 - Легко реализуется и понимается.

Недостатки:
 - Не учитывает порядок слов и контекст.
 - Может дать большой вес редким словам, которые не важны для смысла.

Ограничения:
 - Не подходит для моделирования семантики или понимания контекста слов.
 - Разреженные матрицы при большом словаре.

Требования:
 - Необходимо подготовить корпус документов и предварительно обработать текст (например, удаление стоп-слов, стемминг).

#### HashingVectorizer
HashingVectorizer преобразует текст в числовой вектор с использованием хэш-функции. Вместо хранения слов в словаре, он преобразует слова в индексы с помощью хэш-функции. Это позволяет избежать необходимости хранения словаря в памяти, что делает его масштабируемым и эффективным для больших наборов данных. Однако, этот подход может привести к коллизиям, когда разные слова имеют один и тот же хэш.

Преимущества:
 - Не требует предварительного словаря, поэтому используется меньше памяти и ускоряется обработка.
 - Подходит для онлайн- или потоковой обработки текста.

Недостатки:
 - Коллизии хеширования могут привести к потере информации.
 - Невозможность обратного преобразования из хеша в слова.

Ограничения:
Не подходит для задач, где важно точно знать соответствие слов и индексов.

Требования:
Подбор размера признакового пространства, чтобы снизить вероятность коллизий.

#### Word2Vec
Word2Vec создает векторы слов, где каждое слово представлено уникальным вектором в многомерном пространстве. Эти векторы пытаются уловить семантические и синтаксические отношения между словами на основе их совместной встречаемости в больших текстовых корпусах.

Преимущества:
 - Улавливает семантические отношения между словами, так как векторы слов обучаются на основе их контекста.
 - Создает плотные векторы (мало нулевых элементов), что может быть более эффективно в вычислительном отношении.

Недостатки:
 - Требует большого набора данных для обучения для получения качественных векторов.
 - Не учитывает порядок слов в предложении (хотя есть расширения, такие как Doc2Vec).

Ограничения:
 - Сложность в интерпретации векторов.
 - Не улавливает многозначность (одно слово — один вектор), если только не используются расширенные модели.

Требования:
 - Необходим большой и качественный обучающий корпус текстов.
 - Время и ресурсы для обучения модели.

#### BERT (Bidirectional Encoder Representations from Transformers)
BERT генерирует контекстуальные вложения, что означает, что векторное представление слова может изменяться в зависимости от его контекста (то есть окружающих его слов) в предложении. Это позволяет уловить более тонкие семантические отношения. Они особенно хороши в задачах, где важен контекст, например, при сопоставлении документов по конкретной теме.

Преимущества:
 - Учитывает двунаправленный контекст слов, что позволяет лучше понимать смысл.
 - Может быть дообучен на специфических данных (fine-tuning), что улучшает качество векторов для конкретного приложения.

Недостатки:
 - Очень требовательно к вычислительным ресурсам, особенно при обучении с нуля.
 - Сложно в понимании и реализации по сравнению с более простыми моделями.

Ограничения:
 - Необходимы хорошие вычислительные ресурсы для эффективной работы.
 - Может быть избыточным для некоторых более простых задач векторизации.

Требования:
 - Предварительно обученные модели доступны, но для специфических задач может потребоваться дообучение.
 - Нужны знания в области трансформеров и навыки работы с библиотеками глубокого обучения, такими как TensorFlow или PyTorch.

### *Модели для Дедубликации*
*Дедупликация документов* — это процесс идентификации и удаления дублирующихся записей в данных. В контексте сопоставления документов с требованиями и документов с характеристиками, задача дедупликации может включать определение степени соответствия документа заданным критериям. 

#### Сиамские нейронные сети (Siamese Neural Networks)
Siamese Networks или другие нейросетевые архитектуры, специально настроенные на сравнение текстов, могут быть обучены на задаче определения степени соответствия между документами.

Преимущества:
 - Обучаются на парах схожих или различных объектов, что позволяет эффективно определять степень схожести.
 - Могут быть использованы для сравнения векторов вложений документов, полученных, например, с помощью BERT.

Недостатки:
 - Требуют большого количества парных данных для эффективного обучения.
 - Сравнительно высокие вычислительные требования для обучения.

Ограничения:
 - Необходимо иметь качественные и репрезентативные данные для тренировки модели.

Требования:
 - Хорошо подготовленный датасет с метками схожести.
 - Вычислительные ресурсы для обучения и инференса модели.

#### Решения на основе правил (Rule-Based Systems)
Rule-Based Systems - это системы, которые используют набор заранее заданных правил для принятия решений или выводов. В контексте NLP правила могут включать грамматические структуры, ключевые слова или шаблоны, и они могут применяться для классификации текста, извлечения информации и других задач. Хотя такие системы могут быть очень точными в определенных случаях, они часто требуют значительных усилий для создания и поддержки правил.

Преимущества:
 - Просты в понимании и реализации.
 - Не требуют обучения на данных, а работают на основе заранее заданных правил.

Недостатки:
 - Могут не справляться с большой вариативностью текста и сложными случаями.
 - Трудоемкий процесс создания и поддержки сложного набора правил.

Ограничения:
 - Низкая масштабируемость и гибкость, особенно когда требуется адаптация к новым данным.

Требования:
 - Знание предметной области и особенностей данных для создания эффективных правил.

Обе эти модели могут быть использованы для сравнения текстовых документов в целях дедупликации. Однако их эффективность будет сильно зависеть от конкретного использования и качества входных данных. В случае сиамских сетей важно иметь достаточное количество примеров для обучения, в то время как системы на основе правил требуют тщательной разработки правил для адекватного покрытия различных случаев дедупликации.

### *Модели для Семантического анализа*
Семантический анализ в обработке естественного языка (Natural Language Processing, NLP) направлен на понимание и интерпретацию смысла слов, предложений и текстовых документов.
Latent Dirichlet Allocation (LDA)

#### Latent Semantic Analysis (LSA)
Latent Semantic Analysis (LSA) - это техника в NLP для извлечения и представления скрытых (латентных) семантических отношений в данных. Она работает путем сокращения размерности матрицы терминов-документов с использованием сингулярного разложения (SVD). LSA помогает обнаружить структуру, скрытую в связях между словами и документами, и часто используется для поддержки семантического поиска, кластеризации и классификации текстов.

Преимущества:
 - Способен выявлять скрытые семантические структуры в данных.
 - Уменьшает размерность данных, сохраняя при этом важные семантические отношения.

Недостатки:
 - Модель линейна и может не улавливать более сложные паттерны в данных.
 - Потеря информации из-за снижения размерности.

Ограничения:
 - Не учитывает синтаксические отношения между словами.

Требования:
 - Достаточно большой корпус текстов для выявления семантических отношений.

#### GloVe (Global Vectors for Word Representation)

GloVe сочетает в себе идеи из двух основных подходов к представлению слов в векторном пространстве: матричной факторизации (как в LSA) и локального контекстного окна (как в Word2Vec).

Преимущества:
 - Улучшенное представление слов благодаря использованию глобальной статистики совместной встречаемости слов.
 - Хорошо отлавливает как семантические, так и синтаксические отношения между словами.

Недостатки:
 - Не учитывает порядок слов и не может различать слова с несколькими значениями.

Ограничения:
 - Требуются большие объемы текста для создания матрицы совместной встречаемости слов.

#### Latent Dirichlet Allocation (LDA)
LDA — это генеративная статистическая модель, которая позволяет обнаруживать скрытые тематические структуры в больших объемах текстовых данных. Она предполагает, что каждый документ представляет собой смесь нескольких тем, где каждая тема характеризуется распределением по словам.

Преимущества:
 - Способна выявлять скрытые темы в текстовых данных.
 - Полезна для организации, суммаризации и понимания больших коллекций документов.

Недостатки:
 - Требует тщательного подбора числа тем и тонкой настройки гиперпараметров.
 - Может быть неэффективной в случае коротких текстов или текстов с очень специфической тематикой.

Ограничения:
 - Предполагает, что слова обмениваются (то есть порядок слов в документе не важен), что не всегда верно для реального использования языка.
 - Использование: LDA применяется для анализа тематик в коллекциях документов, в системах рекомендаций и для улучшения информационного поиска.

Модели Word2Vec и BERT являются инструментами для векторизации, однако, благодаря их способности улавливать семантические отношения, они также играют ключевую роль в семантическом анализе.

***Лучший выбор модели зависит от конкретных требований задачи:***

 - Если важен контекст и глубокое понимание семантики, BERT и подобные ему модели могут дать лучшие результаты.
 - Для кластеризации на основе тематического содержания LDA может быть хорошим выбором.
 - Если нужно быстро сравнить документы по семантически близким словам, Word2Vec или GloVe могут быть достаточными.
 - Для высоко специализированных задач, где критерии соответствия строго определены, специализированные нейросетевые архитектуры, такие как Siamese Networks, могут быть наиболее эффективными.
