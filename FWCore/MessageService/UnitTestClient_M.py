import FWCore.ParameterSet.Config as cms

def UnitTestClient_M(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_M',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
