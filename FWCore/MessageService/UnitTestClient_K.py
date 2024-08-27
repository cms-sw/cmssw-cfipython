import FWCore.ParameterSet.Config as cms

def UnitTestClient_K(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_K',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
