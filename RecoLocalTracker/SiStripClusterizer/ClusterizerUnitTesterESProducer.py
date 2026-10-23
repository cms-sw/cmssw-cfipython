import FWCore.ParameterSet.Config as cms

def ClusterizerUnitTesterESProducer(*args, **kwargs):
  mod = cms.ESProducer('ClusterizerUnitTesterESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
