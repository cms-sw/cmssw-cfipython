import FWCore.ParameterSet.Config as cms

def UnitTestClient_G(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_G',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
