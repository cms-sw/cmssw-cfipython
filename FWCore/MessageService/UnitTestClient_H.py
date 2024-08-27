import FWCore.ParameterSet.Config as cms

def UnitTestClient_H(**kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_H',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
