import FWCore.ParameterSet.Config as cms

def CaloTowerConstituentsMapBuilder(**kwargs):
  mod = cms.ESProducer('CaloTowerConstituentsMapBuilder',
    MapFile = cms.untracked.string(''),
    MapAuto = cms.untracked.bool(False),
    SkipHE = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
