import FWCore.ParameterSet.Config as cms

def EcalTrigTowerConstituentsMapBuilder(**kwargs):
  mod = cms.ESProducer('EcalTrigTowerConstituentsMapBuilder',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
