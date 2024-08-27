import FWCore.ParameterSet.Config as cms

def CaloTowerGeometryFromDBEP(**kwargs):
  mod = cms.ESProducer('CaloTowerGeometryFromDBEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
