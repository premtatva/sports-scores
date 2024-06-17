import streamlit as st
import time

st.set_page_config()  

st.title("Score Tracking System For Sports")
sport_name = st.selectbox("Select The Sport:",["Basketball","Volleyball","Soccer"])



if sport_name == "Basketball":
    def basketball_scorecard():
        st.title("Basketball Scorecard")
        quater = st.selectbox("Quater:",["1","2","3","4"])
        team1_name = st.text_input("Team 1 Name", "Team 1")
        team2_name = st.text_input("Team 2 Name", "Team 2")
        team1_score = st.number_input(team1_name + " Number of Baskets", value=0, step=1)
        team2_score = st.number_input(team2_name + " Number of Baskets", value=0, step=1)
        total1_score = int(team1_score)-int(team2_score)
        total2_score = int(team2_score) -int(team1_score)
        st.write(team1_name + " Total Score: " + str(team1_score))
        st.write(team2_name + " Total Score: " + str(team2_score))
        if quater=="1" or quater=="2" or quater=="3":
            if team1_score>team2_score:
                st.subheader(team1_name + " leads by " + str(total1_score ) + " Basket ")
                
            elif team1_score<team2_score:
                st.subheader(team2_name + " leads by  " + str(total2_score) + " Basket ")
                
            elif team1_score==team2_score and team1_score!=0 and team2_score!=0:
                st.subheader("The Scores Are Equal")
                
        if quater=="4":
            if team1_score>team2_score:
                st.subheader(team1_name + " Wins!!! ")
                
            if team1_score<team2_score:
                st.subheader(team2_name + " Wins!!! ")
                
            if team1_score==team2_score and team1_score!=0 and team2_score!=0:
                st.subheader("The Scores Are Equal")
        


        
            
    basketball_scorecard()
    user_input = st.text_input("Enter Time Period Of The Game:","0")
    ph = st.empty()
    N = int(user_input) * 60

    reset_button = st.button("Reset")
    start_button = st.button("Start The Game")
    
    

    if start_button:
        for secs in range(N, -1, -1):
            mm, ss = secs // 60, secs % 60
            if secs == 0:
                ph.subheader("Time out,End Of Quater")
                break
            else:
                ph.header(f"Countdown: {mm:02d}:{ss:02d}")
                time.sleep(1)
            if reset_button:
                N = int(user_input) * 60
                reset_button = False
        


if sport_name == "Volleyball":
    def volleyball_scorecard():
        st.title("Volleyball Scorecard")
        st.subheader("Maximum Points = 25")
        sets = st.selectbox("Sets:",["1","2","3","4","5"])
        team1_name = st.text_input("Team 1 Name", "Team 1")
        team2_name = st.text_input("Team 2 Name", "Team 2")
        team1_score = st.number_input(team1_name + " Score", value=0, step=1,max_value=25)
        team1_foul = st.number_input(team1_name+ "Number Of Fouls",value=0, step=1)
        team2_score = st.number_input(team2_name + " Score", value=0, step=1,max_value=25)
        team2_foul = st.number_input(team2_name + "Number of Fouls ",value=0,step=1 )
        st.write(team1_name + " Total Score: " + str(team1_score))
        st.write(team2_name + " Total Score: " + str(team2_score))
        if team1_score<25 and team1_score>team2_score:
            st.subheader(team1_name + " Leads ")
        elif team2_score<25 and team2_score>team1_score:
            st.subheader(team2_name + " Leads ")
        elif team1_score==25:
            st.subheader(team1_name + " Wins!!! ")
        elif team2_score==25:
            st.subheader(team2_name + " Wins!!! ")
        else:
            st.subheader("The Scores Are Equal.")
    volleyball_scorecard()

if sport_name=="Soccer":
    def soccer_scorecard():
        st.title("Soccer Scorecard")
        st.markdown("Duration of Game : 90 mins")
        team1_name = st.text_input("Team 1 Name", "Team 1")
        team2_name = st.text_input("Team 2 Name", "Team 2")
        team1_score = st.number_input(team1_name + " Number of Goals", value=0, step=1)
        team2_score = st.number_input(team2_name + " Number of Goals", value=0, step=1)
        st.write(team1_name + " Total Score: " + str(team1_score))
        st.write(team2_name + " Total Score: " + str(team2_score))

        def main():
            st.title("Timer")
            
    
            if 'countdown_seconds' not in st.session_state:
                st.session_state.countdown_seconds = 0
    
            user_input = st.text_input("Enter Time Period Of The Game (in minutes):",90)
            if user_input.isdigit():
                N = int(user_input) * 60
            else:
                N = 0
    
            reset_button = st.button("Reset")
            start_button = st.button("Start")
    
            if start_button:
                st.session_state.countdown_seconds = N
    
            countdown_placeholder = st.empty()
    
            while st.session_state.countdown_seconds > 0:
                mm = st.session_state.countdown_seconds // 60
                ss = st.session_state.countdown_seconds % 60
                countdown_placeholder.subheader(f"Countdown: {mm:02d}:{ss:02d}")
               
        
                if reset_button:
                    st.session_state.countdown_seconds = N
                    reset_button = False
        
                time.sleep(1)
                st.session_state.countdown_seconds -= 1
    
                if st.session_state.countdown_seconds == 0:
                    countdown_placeholder.header("Time out, Game Over")
                    if team1_score>team2_score:
                        countdown_placeholder.header(team1_name + " Wins!!! ")
                    elif team2_score>team1_score:
                        countdown_placeholder.header(team2_name + " Wins!!! ")
                    elif team2_score==team1_score:
                        countdown_placeholder.header("It's A Tie!")

        if __name__ == "__main__":
            main()
    soccer_scorecard()
    