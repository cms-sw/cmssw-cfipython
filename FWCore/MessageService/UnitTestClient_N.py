import FWCore.ParameterSet.Config as cms

def UnitTestClient_N(*args, **kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_N',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
