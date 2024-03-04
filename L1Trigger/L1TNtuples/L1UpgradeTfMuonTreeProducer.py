import FWCore.ParameterSet.Config as cms

def L1UpgradeTfMuonTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('L1UpgradeTfMuonTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
