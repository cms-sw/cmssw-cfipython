import FWCore.ParameterSet.Config as cms

MTDTimeCalibESProducer = cms.ESProducer('MTDTimeCalibESProducer',
  BTLTimeOffset = cms.double(0),
  ETLTimeOffset = cms.double(0),
  BTLLightCollTime = cms.double(0.2),
  BTLLightCollSlope = cms.double(0.075),
  appendToDataLabel = cms.string('')
)
