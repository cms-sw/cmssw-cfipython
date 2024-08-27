import FWCore.ParameterSet.Config as cms

def UnitTestClient_X(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_X',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
