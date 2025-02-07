import FWCore.ParameterSet.Config as cms

def L1MuonMatcher(*args, **kwargs):
  mod = cms.EDProducer('L1MuonMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
