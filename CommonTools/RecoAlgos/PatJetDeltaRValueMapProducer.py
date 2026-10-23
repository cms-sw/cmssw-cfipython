import FWCore.ParameterSet.Config as cms

def PatJetDeltaRValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('PatJetDeltaRValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
