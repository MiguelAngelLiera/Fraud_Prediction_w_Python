# Predicción del Fraude Crediticio

## Descripción
Ejercicio para predicción de fraude, contempla el proceso de exploración de datos, el pre-procesamiento, el analisis de modelos de clasificación 

## Updates
- [15/08/2024] The very first version has been uploaded to this public repo!

## Detailed Description
I focused in classification models:
<!--| without DWT      |                              with DWT                          |                              Network                          |
| ------------- | -------------------------------------------------------| -------------------------------------------------------| 
| [NARNN](https://github.com/MiguelAngelLiera/NN-Stock-Exchange-Pc-/blob/main/NARNN.ipynb) | [DWT_NARNN](https://github.com/MiguelAngelLiera/NN-Stock-Exchange-Pc-/blob/main/DWT_NARNN.ipynb)     | Not Linear Auto-regressive NN (NARNN)                   |
| [LSTMNN](https://github.com/MiguelAngelLiera/NN-Stock-Exchange-Pc-/blob/main/NARNN.ipynb) | [DWT_LSTMNN](https://github.com/MiguelAngelLiera/NN-Stock-Exchange-Pc-/blob/main/DWT_NARNN.ipynb)     | Long Short-Term Memory NN (LSTMNN)   | 
| [GRUNN](https://github.com/MiguelAngelLiera/NN-Stock-Exchange-Pc-/blob/main/NARNN.ipynb) | [DWT_GRUNN](https://github.com/MiguelAngelLiera/NN-Stock-Exchange-Pc-/blob/main/DWT_NARNN.ipynb)       | Gated Recurrent Unit NN (GRUNN)     |

On these notebooks we can find the data-preprocesing, prediction and evaluation of the models.

## Data Wavelet Transform (DWT)

The DWT is the discretization of the Continous Wavelet Transform (CWT) that is an advanced technique in signal procesing that decompose data and functions in their frecuency coefficents. It depend on to variables, the frecuency and translation over time, doing a frecuencial and temporal analysis over the signal.-->

<!---![image](imagenes/ACTINVRB_DWT_lvl1_5.png)-->
<!--<p align="center">
  <img src="imagenes/ACTINVRB_DWT_lvl1_5.png" alt="NARNN Architecture" height="600" style="vertical-align:top; margin:4px">
</p>
Five level decomposition of a time series (ACTINVRB)

## NARNN
They are an especific NN's architecture that consist in predicting future values starting with the past *d* values as an input.
<p align="center">
  <img src="imagenes/DWT-NARRN.png" alt="NARNN Architecture" height="400" style="vertical-align:top; margin:4px">
</p>

## LSTMNN
They are an especific NN's architecture that consist in predicting future values starting with the past *d* values as an input.
<p align="center">
  <img src="imagenes/LSTMnn_arquitectura.png" alt="NARNN Architecture" height="400" style="vertical-align:top; margin:4px">
</p>

## GRUNN
They are an especific NN's architecture that consist in predicting future values starting with the past *d* values as an input.
<p align="center">
  <img src="imagenes/GRUnn_arquitectura.png" alt="NARNN Architecture" height="400" style="vertical-align:top; margin:4px">
</p>-->
