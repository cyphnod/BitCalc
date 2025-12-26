using System;
using System.Drawing;
using System.Windows.Forms;

namespace BitCalc
{
    static class Program
    {
        [STAThread]
        static void Main()
        {
            ApplicationConfiguration.Initialize();
            Application.Run(new MainForm());
        }
    }

    public class MainForm : Form
    {
        TextBox txtBalance, txtRiskPercent, txtEntry, txtStop, txtTake;
        Label lblResult;

        public MainForm()
        {
            Text = "BitCalc – Crypto Trading Calculator v1";
            Size = new Size(520, 420);
            StartPosition = FormStartPosition.CenterScreen;
            FormBorderStyle = FormBorderStyle.FixedDialog;
            MaximizeBox = false;

            Font = new Font("Segoe UI", 10);

            int y = 20;

            Controls.Add(CreateLabel("Account Balance ($):", 20, y));
            txtBalance = CreateTextBox(220, y); y += 40;

            Controls.Add(CreateLabel("Risk per Trade (%):", 20, y));
            txtRiskPercent = CreateTextBox(220, y); y += 40;

            Controls.Add(CreateLabel("Entry Price ($):", 20, y));
            txtEntry = CreateTextBox(220, y); y += 40;

            Controls.Add(CreateLabel("Stop Loss Price ($):", 20, y));
            txtStop = CreateTextBox(220, y); y += 40;

            Controls.Add(CreateLabel("Take Profit Price ($):", 20, y));
            txtTake = CreateTextBox(220, y); y += 50;

            Button btnCalculate = new Button()
            {
                Text = "Calculate",
                Location = new Point(20, y),
                Size = new Size(440, 40)
            };
            btnCalculate.Click += Calculate;
            Controls.Add(btnCalculate);

            y += 60;
            lblResult = new Label()
            {
                Location = new Point(20, y),
                Size = new Size(460, 160),
                BorderStyle = BorderStyle.FixedSingle
            };
            Controls.Add(lblResult);
        }

        void Calculate(object sender, EventArgs e)
        {
            try
            {
                double balance = double.Parse(txtBalance.Text);
                double riskPercent = double.Parse(txtRiskPercent.Text) / 100.0;
                double entry = double.Parse(txtEntry.Text);
                double stop = double.Parse(txtStop.Text);
                double take = double.Parse(txtTake.Text);

                double riskAmount = balance * riskPercent;
                double riskPerUnit = Math.Abs(entry - stop);
                double positionSize = riskAmount / riskPerUnit;

                double profitPerUnit = Math.Abs(take - entry);
                double potentialProfit = profitPerUnit * positionSize;
                double rr = potentialProfit / riskAmount;

                lblResult.Text =
                    $"Risk Amount: $ {riskAmount:F2}\n" +
                    $"Position Size: {positionSize:F4} units\n\n" +
                    $"Potential Profit: $ {potentialProfit:F2}\n" +
                    $"Potential Loss: $ {riskAmount:F2}\n" +
                    $"Risk / Reward Ratio: {rr:F2}";
            }
            catch
            {
                MessageBox.Show("Please enter valid numeric values.",
                    "Input Error",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error);
            }
        }

        Label CreateLabel(string text, int x, int y)
        {
            Label lbl = new Label()
            {
                Text = text,
                Location = new Point(x, y + 5),
                AutoSize = true
            };
            Controls.Add(lbl);
            return lbl;
        }

        TextBox CreateTextBox(int x, int y)
        {
            TextBox txt = new TextBox()
            {
                Location = new Point(x, y),
                Width = 240
            };
            Controls.Add(txt);
            return txt;
        }
    }
}
