import FWCore.ParameterSet.Config as cms

def HcalSimulationConstantsESModule(**kwargs):
  mod = cms.ESProducer('HcalSimulationConstantsESModule',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
