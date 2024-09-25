import FWCore.ParameterSet.Config as cms

def CPEAccessTester(*args, **kwargs):
  mod = cms.EDAnalyzer('CPEAccessTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
