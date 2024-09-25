import FWCore.ParameterSet.Config as cms

def UnitTestClient_Nd(*args, **kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_Nd',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
