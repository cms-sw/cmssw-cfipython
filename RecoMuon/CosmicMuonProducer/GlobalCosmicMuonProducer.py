import FWCore.ParameterSet.Config as cms

def GlobalCosmicMuonProducer(*args, **kwargs):
  mod = cms.EDProducer('GlobalCosmicMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
