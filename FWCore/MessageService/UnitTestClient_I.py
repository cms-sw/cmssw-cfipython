import FWCore.ParameterSet.Config as cms

def UnitTestClient_I(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_I',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
