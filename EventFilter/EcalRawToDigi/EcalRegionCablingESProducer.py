import FWCore.ParameterSet.Config as cms

def EcalRegionCablingESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalRegionCablingESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
