import PyInstaller.__main__
import streamlit as st
import time
import os
from streamlit.errors import DuplicateWidgetID

#Initializing Variables

strengths_str1 = " "
strengths_str2 = " "
strengths_str3 = " "
strengths_str4 = " "
strengths_str5 = " "
strengths_output = " "
improvement_str1 = " "
improvement_str2 = " "
improvement_str3 = " "
improvement_str4 = " "
improvement_str5 = " "
improvement_output = " "
gramNsyn_str1 = " "
gramNsyn_str2 = " "
gramNsyn_str3 = " "
gramNsyn_str4 = " "
gramNsyn_str5 = " "
gramNsyn_output = " "
voc_str1 = " "
voc_str2 = " "
voc_str3 = " "
voc_str4 = " "
voc_str5 = " "
voc_output = " "
writ_str1 = " "
writ_str2 = " "
writ_str3 = " "
writ_str4 = " "
writ_str5 = " "
writ_output = " "

pos1 = False
pos2 = False
pos3 = False
pos4 = False
pos5 = False
imp1 = False
imp2 = False
imp3 = False
imp4 = False
imp5 = False
gns1 = False
gns2 = False
gns3 = False
gns4 = False
gns5 = False
voc1 = False
voc2 = False
voc3 = False
voc5 = False
writ1 = False
writ2 = False
writ3 = False
writ4 = False
writ5 = False


def run():
    #Student_List
    global student_list, pronoun1, pronoun2, strengths_output, improvement_output, gramNsyn_output, voc_output, writ_output
    student_list = st.selectbox(
        '**Select Student**',
        (" ", "Antonio", "Begonia", "Leila", "Noe", "Snizhana", "Amos", "Antoine"))
        #Pronouns1
    pronoun1 = st.selectbox(
        '**Select Pronouns**',
        (' ', 'he', 'she', 'they'))
        # Pronouns2
    pronoun2 = st.selectbox(
        '**Select Pronouns**',
        (' ', 'his', 'her', 'their'))

    #Strengths
    st.header(':green[Strengths]')

    pos1 = st.checkbox("Good effort, [student's name]! [They/He/She] continues to demonstrate a strong commitment to improving [their/his/her] English skills.")
    pos2 = st.checkbox("Well done, [student's name]! [Their/His/Her] dedication to mastering English is commendable and will lead to success.")
    pos3 = st.checkbox("Excellent job, [student's name]. Your hard work and enthusiasm are reflected in the quality of your writing.")
    pos4 = st.checkbox("In today's lesson [student's name] successfully made good use of vocabulary related to [XXXX]")
    pos5 = st.checkbox("[Student's name] also did a good job using the XXX tense.")

    if pos1:
        strengths_str1 = str(("Good effort, ") + str(student_list) + ("! ") + str(pronoun1) + (" continues to demonstrate a strong commitment to improving ") + str(pronoun2) + (" English skills."))
        strengths_output = str((strengths_output) + ("""
        
    """) + (strengths_str1))
    if pos2:
        strengths_str2 = str(("Well done, ") + str(student_list) + ("! ") + str(pronoun2) + (" dedication to mastering English is commendable and will lead to success."))
        strengths_output = str((strengths_output) + ("""
        
    """) + (strengths_str2))
    if pos3:
        strengths_str3 = str(("Excellent job, ") + str(student_list) + (". Your hard work and enthusiasm are reflected in the quality of your writing."))
        strengths_output = str((strengths_output) + ("""
        
    """) + (strengths_str3))
    if pos4:
        strengths_str4 = str(("In today's lesson ") + str(student_list) + (" successfully made good use of vocabulary related to [XXXX]"))
        strengths_output = str((strengths_output) + ("""
        
    """) + (strengths_str4))
    if pos5:
        strengths_str5 = str((student_list) + (" also did a good job using the [XXX] tense."))
        strengths_output = str((strengths_output) + ("""
        
    """) + (strengths_str5))

    #Areas for Improvement
    st.header(':orange[Areas for Improvement]')

    imp1 = st.checkbox("[Student's name] is doing well in maintaining grammar consistency, but [they/he/she] might want to focus on subject-verb agreement.")
    imp2 = st.checkbox("While [student's name]'s vocabulary usage is good, they should continue to practice [XXX].")

    if imp1:
        improvement_str1 = str((student_list) + (" is doing well in maintaining grammar consistency, but ") + str(pronoun1) + (" might want to focus on subject-verb agreement."))
        improvement_output = str((improvement_output) + ("""

    """) + (improvement_str1))
    if imp2:
        improvement_str2 = str(("While ") + str(student_list) + ("'s vocabulary usage is good, ") + str(pronoun1) + (" should continue to practice [XXX]."))
        improvement_output = str((improvement_output) + ("""

    """) + (improvement_str2))

    #Grammar And Syntax
    st.header(':red[Grammar And Syntax]')

    gns1 = st.checkbox("It's notable that [student's name] effectively uses sentence structures. Careful attention to subject-verb agreement will further elevate [their/his/her] writing.")
    gns2 = st.checkbox("[Student's name] exhibits a strong understanding of grammar. Ensuring consistent verb tenses will enhance overall clarity and fluency.")
    gns3 = st.checkbox("Remember to continue practising using the correct form of the verb, using articles correctly as well as using singular/plural nouns.")

    if gns1:
        gramNsyn_str1 = str(("It's notable that ") + str(student_list) + (" effectively uses sentence structures. Careful attention to subject-verb agreement will further elevate ") + str(pronoun2) + (" writing."))
        gramNsyn_output = str((gramNsyn_output) + ("""

    """) + (gramNsyn_str1))
    if gns2:
        gramNsyn_str2 = str(str(student_list) + (" exhibits a strong understanding of grammar. Ensuring consistent verb tenses will enhance overall clarity and fluency."))
        gramNsyn_output = str((gramNsyn_output) + ("""

    """) + (gramNsyn_str2))
    if gns3:
        gramNsyn_str3 = str(("Remember to continue practising using the correct form of the verb, using articles correctly as well as using singular/plural nouns."))
        gramNsyn_output = str((gramNsyn_output) + ("""

    """) + (gramNsyn_str3))

    #Vocabulary
    st.header(':blue[Vocabulary]')

    voc1 = st.checkbox("In [student's name]'s writing, vocabulary choice is vivid and engaging. Expanding [their/his/her] repertoire with more synonyms will add depth to [their/his/her] expression.")
    voc2 = st.checkbox("[Student's name] exhibits a wide-ranging vocabulary. Incorporating idiomatic expressions could further enrich [their/his/her] writing style.")
    voc3 = st.checkbox("It's evident that [student's name] is making strides in vocabulary enrichment. Experimenting with figurative language could elevate [their/his/her] writing even more.")
    voc4 = st.checkbox("Expanding vocabulary will help with comprehension and fluency.")

    if voc1:
        voc_str1 = str(("In ") + str(student_list) + ("'s writing, vocabulary choice is vivid and engaging. Expanding ") + str(pronoun2) + (" repertoire with more synonyms will add depth to ") + str(pronoun2) + (" expression."))
        voc_output = str((voc_output) + ("""

    """) + (voc_str1))
    if voc2:
        voc_str2 = str(str(student_list) + (" exhibits a wide-ranging vocabulary. Incorporating idiomatic expressions could further enrich ") + str(pronoun2) + (" writing style."))
        voc_output = str((voc_output) + ("""

    """) + (voc_str2))
    if voc3:
        voc_str3 = str(("It's evident that ") + str(student_list) + (" is making strides in vocabulary enrichment. Experimenting with figurative language could elevate ") + str(pronoun2) + (" writing even more."))
        voc_output = str((voc_output) + ("""

    """) + (voc_str3))
    if voc4:
        voc_str4 = str("Expanding vocabulary will help with comprehension and fluency.")
        voc_output = str((voc_output) + ("""

    """) + (voc_str4))


    st.header("""
    
    
    """)
    st.divider()
    st.header("""


    """)
    st.title('**FEEDBACK**')
    st.header("""
    
        """)
    st.header('Strengths')
    st.write(strengths_output)
    st.text ("""
    
    """)
    st.header('Areas To Improve On:')
    st.write(improvement_output)
    st.text ("""
    
    """)
    st.header('Grammar And Syntax:')
    st.write(gramNsyn_output)
    st.text ("""
    
    """)
    st.header('Vocabulary:')
    st.write(voc_output)
    st.text ("""
    
    """)
    st.divider()
    st.text("""

        """)

st.title ('Student Feedback Template')
st.subheader = '**--> Student Feedback Template <--**'
if st.button ('**--> Student Feedback Template <--**'):
    with st.spinner('Loading...'):
        time.sleep(3)
run()