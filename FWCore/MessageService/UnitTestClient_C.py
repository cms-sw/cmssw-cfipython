import FWCore.ParameterSet.Config as cms

def UnitTestClient_C(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_C',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod