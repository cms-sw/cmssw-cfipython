import FWCore.ParameterSet.Config as cms

def BasicGenTester(*args, **kwargs):
  mod = cms.EDAnalyzer('BasicGenTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
