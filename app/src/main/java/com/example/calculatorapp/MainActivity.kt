package com.example.calculatorapp

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.ViewModelProvider
import com.example.calculatorapp.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private lateinit var viewModel: CalculatorViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        viewModel = ViewModelProvider(this)[CalculatorViewModel::class.java]

        setupNumberButtons()
        setupOperationButtons()
        setupUtilityButtons()

        viewModel.displayText.observe(this) { text ->
            binding.resultTextView.text = text
        }
    }

    private fun setupNumberButtons() {
        val numberButtons = listOf(
            binding.button0, binding.button1, binding.button2, binding.button3,
            binding.button4, binding.button5, binding.button6, binding.button7,
            binding.button8, binding.button9
        )

        numberButtons.forEach { button ->
            button.setOnClickListener { viewModel.onNumberClick(button.text.toString()) }
        }
    }

    private fun setupOperationButtons() {
        binding.buttonAdd.setOnClickListener { 
            viewModel.onOperationClick(CalculatorViewModel.Operation.ADD) 
        }
        binding.buttonSubtract.setOnClickListener { 
            viewModel.onOperationClick(CalculatorViewModel.Operation.SUBTRACT) 
        }
        binding.buttonMultiply.setOnClickListener { 
            viewModel.onOperationClick(CalculatorViewModel.Operation.MULTIPLY) 
        }
        binding.buttonDivide.setOnClickListener { 
            viewModel.onOperationClick(CalculatorViewModel.Operation.DIVIDE) 
        }
        binding.buttonEquals.setOnClickListener { 
            viewModel.onEqualsClick() 
        }
    }

    private fun setupUtilityButtons() {
        binding.buttonClear.setOnClickListener { viewModel.onClearClick() }
        binding.buttonSqrt.setOnClickListener { viewModel.onSqrtClick() }
        binding.buttonDecimal.setOnClickListener { viewModel.onDecimalClick() }
    }
}
