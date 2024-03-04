import FWCore.ParameterSet.Config as cms

def GenJetMatcher(**kwargs):
  mod = cms.EDProducer('GenJetMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
