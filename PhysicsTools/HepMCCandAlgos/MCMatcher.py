import FWCore.ParameterSet.Config as cms

def MCMatcher(*args, **kwargs):
  mod = cms.EDProducer('MCMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
