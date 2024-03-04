import FWCore.ParameterSet.Config as cms

def UnitTestClient_J(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_J',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
