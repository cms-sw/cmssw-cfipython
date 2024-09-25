import FWCore.ParameterSet.Config as cms

def UnitTestClient_H(*args, **kwargs):
  mod = cms.EDAnalyzer('UnitTestClient_H',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
