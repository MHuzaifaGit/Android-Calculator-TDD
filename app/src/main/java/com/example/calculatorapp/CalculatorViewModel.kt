package com.example.calculatorapp

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import kotlin.math.sqrt

class CalculatorViewModel : ViewModel() {
    private val _displayText = MutableLiveData("0")
    val displayText: LiveData<String> = _displayText

    private var currentNumber = ""
    private var firstNumber = 0.0
    private var operation: Operation? = null

    enum class Operation {
        ADD, SUBTRACT, MULTIPLY, DIVIDE
    }

    fun onNumberClick(number: String) {
        currentNumber += number
        _displayText.value = currentNumber.ifEmpty { "0" }
    }

    fun onOperationClick(op: Operation) {
        if (currentNumber.isNotEmpty()) {
            firstNumber = currentNumber.toDouble()
            operation = op
            currentNumber = ""
        }
    }

    fun onEqualsClick() {
        if (currentNumber.isNotEmpty()) {
            val secondNumber = currentNumber.toDouble()
            val result = when (operation) {
                Operation.ADD -> firstNumber + secondNumber
                Operation.SUBTRACT -> firstNumber - secondNumber
                Operation.MULTIPLY -> firstNumber * secondNumber
                Operation.DIVIDE -> {
                    if (secondNumber == 0.0) {
                        _displayText.value = "Error: Divide by 0"
                        return
                    }
                    firstNumber / secondNumber
                }
                null -> secondNumber
            }
            _displayText.value = result.toString()
            currentNumber = result.toString()
            operation = null
        }
    }

    fun onSqrtClick() {
        if (currentNumber.isNotEmpty()) {
            val number = currentNumber.toDouble()
            if (number >= 0) {
                val result = sqrt(number)
                _displayText.value = result.toString()
                currentNumber = result.toString()
            } else {
                _displayText.value = "Error: Negative Root"
            }
        }
    }

    fun onClearClick() {
        currentNumber = ""
        firstNumber = 0.0
        operation = null
        _displayText.value = "0"
    }

    fun onDecimalClick() {
        if (!currentNumber.contains(".")) {
            currentNumber += "."
            _displayText.value = currentNumber
        }
    }
}
