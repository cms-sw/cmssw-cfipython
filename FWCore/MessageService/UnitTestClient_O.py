import FWCore.ParameterSet.Config as cms

def UnitTestClient_O(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_O',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
