import FWCore.ParameterSet.Config as cms

def UnitTestClient_B(*args, **kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_B',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
