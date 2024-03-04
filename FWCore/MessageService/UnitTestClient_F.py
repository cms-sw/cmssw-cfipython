import FWCore.ParameterSet.Config as cms

def UnitTestClient_F(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_F',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
