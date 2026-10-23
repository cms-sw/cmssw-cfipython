import FWCore.ParameterSet.Config as cms

def CosmicMuonValidator(*args, **kwargs):
  mod = cms.EDAnalyzer('CosmicMuonValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
