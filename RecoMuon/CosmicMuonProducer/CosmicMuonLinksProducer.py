import FWCore.ParameterSet.Config as cms

def CosmicMuonLinksProducer(*args, **kwargs):
  mod = cms.EDProducer('CosmicMuonLinksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
