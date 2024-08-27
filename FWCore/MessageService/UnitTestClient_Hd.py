import FWCore.ParameterSet.Config as cms

def UnitTestClient_Hd(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_Hd',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
