import FWCore.ParameterSet.Config as cms

def CaloTowerHardcodeGeometryEP(*args, **kwargs):
  mod = cms.ESProducer('CaloTowerHardcodeGeometryEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
