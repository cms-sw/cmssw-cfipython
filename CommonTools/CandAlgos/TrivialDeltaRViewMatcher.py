import FWCore.ParameterSet.Config as cms

def TrivialDeltaRViewMatcher(*args, **kwargs):
  mod = cms.EDProducer('TrivialDeltaRViewMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
