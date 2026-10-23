import FWCore.ParameterSet.Config as cms

def RecoJetToPatJetDeltaRValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('RecoJetToPatJetDeltaRValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
