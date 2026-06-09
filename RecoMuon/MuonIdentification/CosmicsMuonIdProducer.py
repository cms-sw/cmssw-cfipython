import FWCore.ParameterSet.Config as cms

def CosmicsMuonIdProducer(*args, **kwargs):
  mod = cms.EDProducer('CosmicsMuonIdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
