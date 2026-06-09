import FWCore.ParameterSet.Config as cms

def CaloTowerConstituentsMapBuilder(*args, **kwargs):
  mod = cms.ESProducer('CaloTowerConstituentsMapBuilder',
    MapFile = cms.untracked.string(''),
    MapAuto = cms.untracked.bool(False),
    SkipHE = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
