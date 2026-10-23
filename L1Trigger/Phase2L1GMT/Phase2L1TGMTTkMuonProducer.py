import FWCore.ParameterSet.Config as cms

def Phase2L1TGMTTkMuonProducer(*args, **kwargs):
  mod = cms.EDProducer('Phase2L1TGMTTkMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
