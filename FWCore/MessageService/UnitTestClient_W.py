import FWCore.ParameterSet.Config as cms

def UnitTestClient_W(*args, **kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_W',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
