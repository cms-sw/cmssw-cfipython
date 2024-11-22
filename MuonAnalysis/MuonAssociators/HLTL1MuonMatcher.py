import FWCore.ParameterSet.Config as cms

def HLTL1MuonMatcher(*args, **kwargs):
  mod = cms.EDProducer('HLTL1MuonMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
