import FWCore.ParameterSet.Config as cms

def MTDTimeCalibESProducer(*args, **kwargs):
  mod = cms.ESProducer('MTDTimeCalibESProducer',
    BTLLightCollSlope = cms.double(0.095),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
