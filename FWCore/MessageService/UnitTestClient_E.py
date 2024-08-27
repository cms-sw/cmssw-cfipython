import FWCore.ParameterSet.Config as cms

def UnitTestClient_E(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_E',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
