import FWCore.ParameterSet.Config as cms

def HLTL1MuonMatcher(**kwargs):
  mod = cms.EDProducer('HLTL1MuonMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
