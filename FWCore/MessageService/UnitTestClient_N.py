import FWCore.ParameterSet.Config as cms

def UnitTestClient_N(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_N',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
