import FWCore.ParameterSet.Config as cms

def IsolationProducerForTracks(*args, **kwargs):
  mod = cms.EDProducer('IsolationProducerForTracks',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
