import FWCore.ParameterSet.Config as cms

def MTDTimeCalibESProducer(**kwargs):
  mod = cms.ESProducer('MTDTimeCalibESProducer',
    BTLTimeOffset = cms.double(0),
    ETLTimeOffset = cms.double(0),
    BTLLightCollTime = cms.double(0.2),
    BTLLightCollSlope = cms.double(0.075),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
