import FWCore.ParameterSet.Config as cms

def CaloTowerGeometryToDBEP(*args, **kwargs):
  mod = cms.ESProducer('CaloTowerGeometryToDBEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
