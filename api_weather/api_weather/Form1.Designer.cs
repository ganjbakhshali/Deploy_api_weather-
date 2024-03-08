namespace api_weather
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.txt_city = new System.Windows.Forms.TextBox();
            this.btn_search = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.pictureBox_today = new System.Windows.Forms.PictureBox();
            this.lbl_today_wind = new System.Windows.Forms.Label();
            this.lbl_today_cond = new System.Windows.Forms.Label();
            this.lbl_today_temp = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.pictureBox_tomorrow = new System.Windows.Forms.PictureBox();
            this.lbl_tomorrow_Wind = new System.Windows.Forms.Label();
            this.lbl_tomorrow_cond = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.lbl_tomorrow_Temp = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_today)).BeginInit();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_tomorrow)).BeginInit();
            this.SuspendLayout();
            // 
            // txt_city
            // 
            this.txt_city.Location = new System.Drawing.Point(156, 53);
            this.txt_city.Name = "txt_city";
            this.txt_city.Size = new System.Drawing.Size(321, 27);
            this.txt_city.TabIndex = 0;
            this.txt_city.Enter += new System.EventHandler(this.btn_search_Click);
            // 
            // btn_search
            // 
            this.btn_search.Location = new System.Drawing.Point(483, 53);
            this.btn_search.Name = "btn_search";
            this.btn_search.Size = new System.Drawing.Size(94, 29);
            this.btn_search.TabIndex = 1;
            this.btn_search.Text = "Search";
            this.btn_search.UseVisualStyleBackColor = true;
            this.btn_search.Click += new System.EventHandler(this.btn_search_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(23, 53);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(127, 20);
            this.label1.TabIndex = 2;
            this.label1.Text = "Enther City Name:";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.pictureBox_today);
            this.groupBox1.Controls.Add(this.lbl_today_wind);
            this.groupBox1.Controls.Add(this.lbl_today_cond);
            this.groupBox1.Controls.Add(this.lbl_today_temp);
            this.groupBox1.Controls.Add(this.label9);
            this.groupBox1.Controls.Add(this.label7);
            this.groupBox1.Controls.Add(this.label8);
            this.groupBox1.Location = new System.Drawing.Point(75, 162);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(292, 276);
            this.groupBox1.TabIndex = 3;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Today Forcast";
            this.groupBox1.Enter += new System.EventHandler(this.groupBox1_Enter);
            // 
            // pictureBox_today
            // 
            this.pictureBox_today.Location = new System.Drawing.Point(48, 154);
            this.pictureBox_today.Name = "pictureBox_today";
            this.pictureBox_today.Size = new System.Drawing.Size(196, 122);
            this.pictureBox_today.TabIndex = 9;
            this.pictureBox_today.TabStop = false;
            // 
            // lbl_today_wind
            // 
            this.lbl_today_wind.AutoSize = true;
            this.lbl_today_wind.Location = new System.Drawing.Point(122, 74);
            this.lbl_today_wind.Name = "lbl_today_wind";
            this.lbl_today_wind.Size = new System.Drawing.Size(0, 20);
            this.lbl_today_wind.TabIndex = 8;
            // 
            // lbl_today_cond
            // 
            this.lbl_today_cond.AutoSize = true;
            this.lbl_today_cond.Location = new System.Drawing.Point(122, 118);
            this.lbl_today_cond.Name = "lbl_today_cond";
            this.lbl_today_cond.Size = new System.Drawing.Size(0, 20);
            this.lbl_today_cond.TabIndex = 6;
            // 
            // lbl_today_temp
            // 
            this.lbl_today_temp.AutoSize = true;
            this.lbl_today_temp.Location = new System.Drawing.Point(122, 31);
            this.lbl_today_temp.Name = "lbl_today_temp";
            this.lbl_today_temp.Size = new System.Drawing.Size(0, 20);
            this.lbl_today_temp.TabIndex = 7;
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(6, 74);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(90, 20);
            this.label9.TabIndex = 4;
            this.label9.Text = "Wind Speed";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(6, 118);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(74, 20);
            this.label7.TabIndex = 2;
            this.label7.Text = "Condition";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(6, 31);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(93, 20);
            this.label8.TabIndex = 3;
            this.label8.Text = "Temperature";
            this.label8.Click += new System.EventHandler(this.label8_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.pictureBox_tomorrow);
            this.groupBox2.Controls.Add(this.lbl_tomorrow_Wind);
            this.groupBox2.Controls.Add(this.lbl_tomorrow_cond);
            this.groupBox2.Controls.Add(this.label4);
            this.groupBox2.Controls.Add(this.lbl_tomorrow_Temp);
            this.groupBox2.Controls.Add(this.label2);
            this.groupBox2.Controls.Add(this.label3);
            this.groupBox2.Location = new System.Drawing.Point(396, 162);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(292, 276);
            this.groupBox2.TabIndex = 4;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Tomorrow Forcast";
            // 
            // pictureBox_tomorrow
            // 
            this.pictureBox_tomorrow.Location = new System.Drawing.Point(37, 148);
            this.pictureBox_tomorrow.Name = "pictureBox_tomorrow";
            this.pictureBox_tomorrow.Size = new System.Drawing.Size(196, 122);
            this.pictureBox_tomorrow.TabIndex = 13;
            this.pictureBox_tomorrow.TabStop = false;
            // 
            // lbl_tomorrow_Wind
            // 
            this.lbl_tomorrow_Wind.AutoSize = true;
            this.lbl_tomorrow_Wind.Location = new System.Drawing.Point(127, 74);
            this.lbl_tomorrow_Wind.Name = "lbl_tomorrow_Wind";
            this.lbl_tomorrow_Wind.Size = new System.Drawing.Size(0, 20);
            this.lbl_tomorrow_Wind.TabIndex = 12;
            // 
            // lbl_tomorrow_cond
            // 
            this.lbl_tomorrow_cond.AutoSize = true;
            this.lbl_tomorrow_cond.Location = new System.Drawing.Point(127, 118);
            this.lbl_tomorrow_cond.Name = "lbl_tomorrow_cond";
            this.lbl_tomorrow_cond.Size = new System.Drawing.Size(0, 20);
            this.lbl_tomorrow_cond.TabIndex = 10;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(6, 118);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(74, 20);
            this.label4.TabIndex = 0;
            this.label4.Text = "Condition";
            // 
            // lbl_tomorrow_Temp
            // 
            this.lbl_tomorrow_Temp.AutoSize = true;
            this.lbl_tomorrow_Temp.Location = new System.Drawing.Point(127, 31);
            this.lbl_tomorrow_Temp.Name = "lbl_tomorrow_Temp";
            this.lbl_tomorrow_Temp.Size = new System.Drawing.Size(0, 20);
            this.lbl_tomorrow_Temp.TabIndex = 11;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(6, 31);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(93, 20);
            this.label2.TabIndex = 0;
            this.label2.Text = "Temperature";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(6, 74);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(90, 20);
            this.label3.TabIndex = 0;
            this.label3.Text = "Wind Speed";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btn_search);
            this.Controls.Add(this.txt_city);
            this.Name = "Form1";
            this.Text = "weather api";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_today)).EndInit();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_tomorrow)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private TextBox txt_city;
        private Button btn_search;
        private Label label1;
        private GroupBox groupBox1;
        private GroupBox groupBox2;
        private Label lbl_today_wind;
        private Label lbl_today_cond;
        private Label lbl_today_temp;
        private Label label9;
        private Label label7;
        private Label label8;
        private Label lbl_tomorrow_Wind;
        private Label lbl_tomorrow_cond;
        private Label label4;
        private Label lbl_tomorrow_Temp;
        private Label label2;
        private Label label3;
        private PictureBox pictureBox_today;
        private PictureBox pictureBox_tomorrow;
    }
}