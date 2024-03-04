import FWCore.ParameterSet.Config as cms

def UnitTestClient_P(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_P',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
