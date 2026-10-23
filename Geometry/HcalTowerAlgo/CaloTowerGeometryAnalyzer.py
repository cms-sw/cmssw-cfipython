import FWCore.ParameterSet.Config as cms

def CaloTowerGeometryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloTowerGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
