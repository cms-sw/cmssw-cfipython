import FWCore.ParameterSet.Config as cms

def TrivialDeltaRMatcher(*args, **kwargs):
  mod = cms.EDProducer('TrivialDeltaRMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
