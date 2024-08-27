import FWCore.ParameterSet.Config as cms

def CaloSimulationConstantsESModule(**kwargs):
  mod = cms.ESProducer('CaloSimulationConstantsESModule',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
