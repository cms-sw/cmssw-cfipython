import FWCore.ParameterSet.Config as cms

def CaloTowerTopologyEP(**kwargs):
  mod = cms.ESProducer('CaloTowerTopologyEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
