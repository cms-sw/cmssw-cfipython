import FWCore.ParameterSet.Config as cms

def CaloTowerHardcodeGeometryEP(**kwargs):
  mod = cms.ESProducer('CaloTowerHardcodeGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
