import FWCore.ParameterSet.Config as cms

def UnitTestClient_D(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_D',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
