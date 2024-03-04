import FWCore.ParameterSet.Config as cms

def L1UpgradeTfMuonShowerTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('L1UpgradeTfMuonShowerTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
