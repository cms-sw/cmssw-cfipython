import FWCore.ParameterSet.Config as cms

def UnitTestClient_R(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_R',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
