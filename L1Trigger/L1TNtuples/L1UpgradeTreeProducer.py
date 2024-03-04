import FWCore.ParameterSet.Config as cms

def L1UpgradeTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('L1UpgradeTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
