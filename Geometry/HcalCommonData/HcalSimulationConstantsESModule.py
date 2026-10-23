import FWCore.ParameterSet.Config as cms

def HcalSimulationConstantsESModule(*args, **kwargs):
  mod = cms.ESProducer('HcalSimulationConstantsESModule',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
