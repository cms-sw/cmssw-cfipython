import FWCore.ParameterSet.Config as cms

def UnitTestClient_M(*args, **kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_M',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
