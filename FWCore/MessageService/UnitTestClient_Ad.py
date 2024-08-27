import FWCore.ParameterSet.Config as cms

def UnitTestClient_Ad(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_Ad',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
