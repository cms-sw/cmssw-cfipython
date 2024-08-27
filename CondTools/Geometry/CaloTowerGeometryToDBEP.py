import FWCore.ParameterSet.Config as cms

def CaloTowerGeometryToDBEP(**kwargs):
  mod = cms.ESProducer('CaloTowerGeometryToDBEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
