import FWCore.ParameterSet.Config as cms

def CandOneToOneDeltaRMatcher(*args, **kwargs):
  mod = cms.EDProducer('CandOneToOneDeltaRMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
