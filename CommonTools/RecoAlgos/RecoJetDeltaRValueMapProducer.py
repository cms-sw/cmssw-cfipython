import FWCore.ParameterSet.Config as cms

def RecoJetDeltaRValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('RecoJetDeltaRValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
