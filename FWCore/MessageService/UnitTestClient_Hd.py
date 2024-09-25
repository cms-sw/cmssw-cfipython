import FWCore.ParameterSet.Config as cms

def UnitTestClient_Hd(*args, **kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_Hd',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
