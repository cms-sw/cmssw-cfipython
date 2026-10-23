import FWCore.ParameterSet.Config as cms

def CaloTowerAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('CaloTowerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
