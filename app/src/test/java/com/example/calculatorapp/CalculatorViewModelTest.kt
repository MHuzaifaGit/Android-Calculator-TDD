package com.example.calculatorapp

import androidx.arch.core.executor.testing.InstantTaskExecutorRule
import org.junit.Before
import org.junit.Rule
import org.junit.Test
import org.junit.Assert.*

class CalculatorViewModelTest {
    private lateinit var viewModel: CalculatorViewModel

    @get:Rule
    val instantTaskExecutorRule = InstantTaskExecutorRule()

    @Before
    fun setup() {
        viewModel = CalculatorViewModel()
    }

    @Test
    fun `test addition`() {
        viewModel.onNumberClick("5")
        viewModel.onOperationClick(CalculatorViewModel.Operation.ADD)
        viewModel.onNumberClick("3")
        viewModel.onEqualsClick()
        assertEquals("8.0", viewModel.displayText.value)
    }

    @Test
    fun `test subtraction`() {
        viewModel.onNumberClick("10")
        viewModel.onOperationClick(CalculatorViewModel.Operation.SUBTRACT)
        viewModel.onNumberClick("4")
        viewModel.onEqualsClick()
        assertEquals("6.0", viewModel.displayText.value)
    }

    @Test
    fun `test multiplication`() {
        viewModel.onNumberClick("5")
        viewModel.onOperationClick(CalculatorViewModel.Operation.MULTIPLY)
        viewModel.onNumberClick("3")
        viewModel.onEqualsClick()
        assertEquals("15.0", viewModel.displayText.value)
    }

    @Test
    fun `test division`() {
        viewModel.onNumberClick("15")
        viewModel.onOperationClick(CalculatorViewModel.Operation.DIVIDE)
        viewModel.onNumberClick("3")
        viewModel.onEqualsClick()
        assertEquals("5.0", viewModel.displayText.value)
    }

    @Test
    fun `test square root`() {
        viewModel.onNumberClick("16")
        viewModel.onSqrtClick()
        assertEquals("4.0", viewModel.displayText.value)
    }

    @Test
    fun `test clear`() {
        viewModel.onNumberClick("5")
        viewModel.onClearClick()
        assertEquals("0", viewModel.displayText.value)
    }
}
