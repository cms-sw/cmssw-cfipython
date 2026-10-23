import FWCore.ParameterSet.Config as cms

def GenJetMatcher(*args, **kwargs):
  mod = cms.EDProducer('GenJetMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
