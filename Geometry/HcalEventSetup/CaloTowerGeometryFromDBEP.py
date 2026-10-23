import FWCore.ParameterSet.Config as cms

def CaloTowerGeometryFromDBEP(*args, **kwargs):
  mod = cms.ESProducer('CaloTowerGeometryFromDBEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
