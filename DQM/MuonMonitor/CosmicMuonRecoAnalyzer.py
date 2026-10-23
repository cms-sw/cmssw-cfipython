import FWCore.ParameterSet.Config as cms

def CosmicMuonRecoAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('CosmicMuonRecoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
