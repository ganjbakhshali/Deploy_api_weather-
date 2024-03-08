using System;
using System.Net.Http;
using System.Threading.Tasks;
using System.Windows.Forms;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System;
using System.IO;
using Newtonsoft.Json.Linq;

namespace api_weather
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void label8_Click(object sender, EventArgs e)
        {

        }
        public void assigne_pic(string description,int pixNum=1)
        {
            string img = "";
            string imagesFolder = "C:\\Users\\Ali\\Desktop\\Deploy_api_weather-\\api_weather\\api_weather\\images\\"; 

            if (description.Contains("Clear"))
                img = imagesFolder + "clear.png";
            else if (description.Contains("Few clouds"))
                img = imagesFolder + "few_cloudes.png";
            else if (description.Contains("Mix snow/rain"))
                img = imagesFolder + "rain_snow.png";
            else if (description.Contains("rain"))
                img = imagesFolder + "rain.png";
            else if (description.Contains("snow"))
                img = imagesFolder + "snow.png";
            else
                img = imagesFolder + "cludy.png";
            
            if (pixNum == 1)
            {
                pictureBox_today.ImageLocation = img;
                pictureBox_today.SizeMode = PictureBoxSizeMode.Zoom; 
            }
            else if (pixNum == 2)
            {
                pictureBox_tomorrow.ImageLocation = img;
                pictureBox_tomorrow.SizeMode = PictureBoxSizeMode.Zoom; 
            }





        }

        private async void btn_search_Click(object sender, EventArgs e)
        {
            var client = new HttpClient();
            string url = "https://api.weatherbit.io/v2.0/forecast/daily?&city=" + txt_city.Text + "&key=2effe1f9f06e40cc8ef77eb5be376022";

            try
            {
                var response = await client.GetAsync(url);
                response.EnsureSuccessStatusCode();
                string responseData = await response.Content.ReadAsStringAsync();
                // Save the response as a JSON file
                File.WriteAllText("weather_response.json", responseData);
                string json = File.ReadAllText("weather_response.json");

                // Parse the JSON
                JObject jsonObject = JObject.Parse(json);

                // Extract today's weather information
                JObject todayData = (JObject)jsonObject["data"][0];
                double todayTemp = (double)todayData["temp"];
                lbl_today_temp.Text = todayTemp.ToString();
                double todayWindSpeed = (double)todayData["wind_spd"];
                lbl_today_wind.Text = todayWindSpeed.ToString();
                string todayDescription = (string)todayData["weather"]["description"];
                lbl_today_cond.Text = todayDescription;
                assigne_pic(todayDescription);

                // Extract tomorrow's weather information 
                JObject tomorrowData = (JObject)jsonObject["data"][1];
                double tomorrowTemp = (double)tomorrowData["temp"];
                lbl_tomorrow_Temp.Text = tomorrowTemp.ToString();
                double tomorrowWindSpeed = (double)tomorrowData["wind_spd"];
                lbl_tomorrow_Wind.Text = tomorrowWindSpeed.ToString();
                string tomorrowDescription = (string)tomorrowData["weather"]["description"];
                lbl_tomorrow_cond.Text= tomorrowDescription;
                assigne_pic(tomorrowDescription,2);



            }
            catch (Exception ex)
            {
                MessageBox.Show($"An error occurred: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            finally
            {
                client.Dispose();
            }



        }
    }
}