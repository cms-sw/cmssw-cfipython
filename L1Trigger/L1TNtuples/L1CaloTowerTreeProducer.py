import FWCore.ParameterSet.Config as cms

def L1CaloTowerTreeProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1CaloTowerTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
