import FWCore.ParameterSet.Config as cms

def MTDTimeCalibESProducer(*args, **kwargs):
  mod = cms.ESProducer('MTDTimeCalibESProducer',
    BTLTimeOffset = cms.double(0),
    ETLTimeOffset = cms.double(0),
    BTLLightCollTime = cms.double(0.2),
    BTLLightCollSlope = cms.double(0.075),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
