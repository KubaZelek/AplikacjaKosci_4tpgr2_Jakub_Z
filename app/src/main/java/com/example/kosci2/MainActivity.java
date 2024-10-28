package com.example.kosci2;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Random;

public class MainActivity extends AppCompatActivity {

    private ImageView[] diceImages = new ImageView[5];
    private TextView rzutTeraz;
    private TextView gameScore;
    private int totalGameScore = 0;
    private Random random = new Random();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        diceImages[0] = findViewById(R.id.dice1);
        diceImages[1] = findViewById(R.id.dice2);
        diceImages[2] = findViewById(R.id.dice3);
        diceImages[3] = findViewById(R.id.dice4);
        diceImages[4] = findViewById(R.id.dice5);

        rzutTeraz = findViewById(R.id.currentRollResult);
        gameScore = findViewById(R.id.gameScore);

        Button rollDiceButton = findViewById(R.id.rollDiceButton);
        rollDiceButton.setOnClickListener(v -> rollDice());

        Button resetButton = findViewById(R.id.resetButton);
        resetButton.setOnClickListener(v -> resetGame());
    }

    private void rollDice() {
        int rollSum = 0;

        for (int i = 0; i < diceImages.length; i++) {
            int roll = random.nextInt(6) + 1;
            rollSum += roll;

            int resourceId = getResources().getIdentifier("dice" + roll, "drawable", getPackageName());
            diceImages[i].setImageResource(resourceId);
        }

        rzutTeraz.setText("Wynik tego losowania: " + rollSum);
        totalGameScore += rollSum;
        gameScore.setText("Wynik gry: " + totalGameScore);
    }

    private void resetGame() {
        for (ImageView diceImage : diceImages) {

            diceImage.setImageResource(R.drawable.dice_default);

        }

        rzutTeraz.setText("Wynik tego losowania: 0");
        gameScore.setText("Wynik gry: 0");
        totalGameScore = 0;
    }
}
