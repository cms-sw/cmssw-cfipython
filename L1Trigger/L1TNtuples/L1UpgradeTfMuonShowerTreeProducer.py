import FWCore.ParameterSet.Config as cms

def L1UpgradeTfMuonShowerTreeProducer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1UpgradeTfMuonShowerTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
