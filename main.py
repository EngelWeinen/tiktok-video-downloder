"""
此代码需在 python 环境下运行，目的是下载到tiktok上所搜索关键词的无水印视频
抖音/TikTok视频下载器 (Douyin/TikTok Video Downloader)
作者: [EngelWeinen]
描述: 根据关键词搜索并下载短视频。
"""
import os
import re
import time
import requests
from urllib.parse import quote

keyword = input('请输入搜索关键词:')

keyword = quote(keyword)

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    'referer': f"https://www.douyin.com/search/{keyword}?aid=ab5912f9-327e-4bff-a290-fd892dade093&type=general",
    'uifid': "1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740c402c43e529c5a230b4a0578b21d0fc4c7d0468ed8dbc42aaba085dbec4e0317823aa68ea62609078ce45404857f4ed9",
    'Cookie': "enter_pc_once=1; UIFID_TEMP=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740c402c43e529c5a230b4a0578b21d0fc4c7d0468ed8dbc42aaba085dbec4e0317823aa68ea62609078ce45404857f4ed9; x-web-secsdk-uid=20652b6a-3cfc-46cb-b304-f2d817885f18; s_v_web_id=verify_md44mke4_wA4PCbgn_9Kee_4upq_9sbF_DcUeE7XCrxGD; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; dy_swidth=1536; dy_sheight=960; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A960%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; hevc_supported=true; fpk1=U2FsdGVkX183ryCMMZpkMsj/p/001ouDUODMlRVKZEXq1Gkd/YUBzVtLE0Qu5yWSNe4DPcB00WtVQuNYhr1VZA==; fpk2=7ddeda88d0c599cc494da0dece6554d5; strategyABtestKey=%221752559418.309%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; xgplayer_user_id=727369804286; passport_csrf_token=adf7d0d983ab45c85f2f546d0feed298; passport_csrf_token_default=adf7d0d983ab45c85f2f546d0feed298; ttwid=1%7Carnb5RdgVUE6tDkLknqJ3CmVeaxcxP1mnWmXbrkD_s4%7C1752559419%7C033d96d953fa377935adb7dd20a2407bfcd484dee5b9cbafdb3c835a54c2133b; biz_trace_id=5cd8323d; __security_mc_1_s_sdk_cert_key=a505cca3-4041-8a31; __security_mc_1_s_sdk_sign_data_key_web_protect=6441aa64-492b-8121; __security_mc_1_s_sdk_crypt_sdk=1f461d7f-467e-8821; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSkJXQjRHa0NEY3V1NXpRTmhFdHVDQnpRRnZRYkJha1NYeUVzYjVRWjJXTkc0Z2w0ZmJNZjdaanIyWk5DUlY2K3VNZk1WY05mQjdidVpPNUNxQjBobGM9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; bd_ticket_guard_client_web_domain=2; xg_device_score=7.4833732231672965; sdk_source_info=7e276470716a68645a606960273f276364697660272927676c715a6d6069756077273f276364697660272927666d776a68605a607d71606b766c6a6b5a7666776c7571273f275e58272927666a6b766a69605a696c6061273f27636469766027292762696a6764695a7364776c6467696076273f275e582729277672715a646971273f2763646976602729277f6b5a666475273f2763646976602729276d6a6e5a6b6a716c273f2763646976602729276c6b6f5a7f6367273f27636469766027292771273f273533303c34313c303037303234272927676c715a75776a716a666a69273f2763646976602778; bit_env=PNGQ7ZS8MLoisMPB8CzLODLY-E1p5i2428_jxcSycK4BbI4C-8hj7KktJl_3W-tSPPtNopOk3DnwRGhGM3g6_3ctxJST5rbUzNljtIQrnU8qDkhiVPXWmkcr4Z78Ok5Ul96gl5tmT9H91W3_tmhWWuxE2ePapG2SGfnbMlAfJLs-_GLEBwoDW5tzA-xg8mTSkXeLfyaUUiNHc0l0XFIZgZWbozUNcUMDAcOfNu_j2tTstuA16KAbSmukB_f_HeFR-boRqi0_SnIvv_HwURGtPScIeiXN97TvxcQ2WT-clQha0-Icd5tSVeQAlmUhd4aJsHMX0LSdsAEYHtitqKgGqQoiyGiVOWMpGXffq3h_X1jDZ-m-ODgfTaGSSv35myDJZJfvxUD8EAeN15L2FQ6bFLeds0j6LpO_Pc7VoZ_1DN87c621U-jYvQ0rFoEi2V9reZ3p19qXIrnmaEerAbcyt3JuxnH-KH8Wq1kl5B6I_kIhFxOSq8s2rvmKzKdiMjbT; gulu_source_res=eyJwX2luIjoiYTlmMjU3NzAxMWQ2OTIyYjc5NWQ5Zjk3NjY1OWVkOTNkMGQ2NjBjMWZhMmNkYzdjMGI4NmI5YTU2YjlhYmU1OCJ9; passport_auth_mix_state=v8mej2rey8clvkpurf8aqy98n8r7sfcl; odin_tt=2e780a154bb989700f38e00659843382d64d1a1fea2331d4668112a9a25f5c4fdb84cdb9848ab515a35a6cbc56b9a1a4e9d9129f40caff6722b12872903f1291a1adb65c2018d0a15ed0336bf246252d; is_dash_user=1; SEARCH_RESULT_LIST_TYPE=%22single%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; __ac_nonce=06875ef5f0046610ff637; csrf_session_id=f82581d645da2823b558c204be791fb3; IsDouyinActive=true; home_can_add_dy_2_desktop=%221%22; download_guide=%221%2F20250715%2F0%22"
}

url = f"https://www.douyin.com/aweme/v1/web/general/search/stream/?aid=6383&browser_language=zh-CN&browser_name=Chrome&browser_online=true&browser_platform=Win32&browser_version=138.0.0.0&channel=channel_pc_web&cookie_enabled=true&count=10&cpu_core_num=16&device_memory=8&device_platform=webapp&downlink=10&effective_type=4g&enable_history=1&engine_name=Blink&engine_version=138.0.0.0&from_group_id=&is_filter_search=0&keyword={keyword}&list_type=single&need_filter_settings=1&offset=0&os_name=Windows&os_version=10&pc_client_type=1&pc_libra_divert=Windows&platform=PC&query_correct_type=1&round_trip_time=50&screen_height=960&screen_width=1536&search_channel=aweme_general&search_source=normal_search&support_dash=1&support_h265=1&uifid=1b474bc7e0db9591e645dd8feb8c65aae4845018effd0c2743039a380ee64740c402c43e529c5a230b4a0578b21d0fc4c7d0468ed8dbc42aaba085dbec4e0317823aa68ea62609078ce45404857f4ed9&version_code=190600&version_name=19.6.0&webid=7527185321613772323&msToken=Nw6Q8PNTBd3b71M0lEVXjESqwYClLp95XVM5U302KIVjNc-k4bcgQ7Gjk-gIjm31PcQZw7xCtfHwJAWld8JLY2TN5Tk1NIF7xC5SHCNVQxxi8Vn0ExONzO1Wx2T7IdrfNN7uhZtNjYv1D2tbCHD9okVdoc2M0jftD27g2yyJiv7RbYBKm7Oseg%3D%3D&a_bogus=D6sjk7Swxx5fOdKbYcEctfxUPygANPSyB1ioS9%2Fl9Px4cwMbPRNXiNC3Goow6sy%2FtYphw9A7SEllbExb0stwZCnkFmkvuiwRez2IIhmLhqw6TlG%2FLqfue0szKwsKUYJNa%2FnSiA4RIsMnInVRnNA8Ad3G75zHQcjgbNZ5p2z9GDS8psLTIn2tecjAc7y%3D"
response = requests.get(url, headers=headers)

video_info_re = r'"desc":"(.*?)","create_time".*?"play_addr":.*?"url_list":\["(.*?)",".*?",".*?"\],"width"'
video_info_list = re.findall(video_info_re, response.text)

if not os.path.exists('抖音视频'):
    os.mkdir('抖音视频')

for video_title, video_url in video_info_list:

    video_title = video_title.replace('\n', '').replace('\\n', '').replace('!', '').replace(':', '').replace('?', '？')

    response = requests.get(video_url, headers=headers)

    with open(f'./抖音视频/{video_title}.mp4', 'wb') as file:
        file.write(response.content)
    print(f'{video_title} - 下载成功')

    time.sleep(1)

