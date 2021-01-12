import FWCore.ParameterSet.Config as cms

siPixelGainCalibrationForHLTGPU = cms.ESProducer('SiPixelGainCalibrationForHLTGPUESProducer',
  appendToDataLabel = cms.string('')
)
