main(){
    if [ $1 -eq 1 ];then
    	echo "禁止通行车辆:浙ABC255"
        cp ./license_plate/ZABC255/lp_database.txt ../lpr_config/
    elif [ $1 -eq 2 ];then
    	echo '禁止通行车辆:浙B53Y11'
        cp ./license_plate/ZB53Y11/lp_database.txt ../lpr_config/
    elif [ $1 -eq 3 ];then
    	echo '禁止通行车辆:浙C796YR'
        cp ./license_plate/ZC796YR/lp_database.txt ../lpr_config/
    elif [ $1 -eq 4 ];then
     	echo '禁止通行车辆:浙D8789H'
        cp ./license_plate/ZD8789H/lp_database.txt ../lpr_config/
    elif [ $1 -eq 5 ];then
     	echo '禁止通行车辆:沪C05EV8'
        cp ./license_plate/HC05EV8/lp_database.txt ../lpr_config/
    else
        echo '禁止通行车辆:None'
        cp ./license_plate/All/lp_database.txt ../lpr_config/
    fi
}


main $1
