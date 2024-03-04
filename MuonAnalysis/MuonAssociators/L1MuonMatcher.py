import FWCore.ParameterSet.Config as cms

def L1MuonMatcher(**kwargs):
  mod = cms.EDProducer('L1MuonMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
