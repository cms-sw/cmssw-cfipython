import FWCore.ParameterSet.Config as cms

def UnitTestClient_B(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_B',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
