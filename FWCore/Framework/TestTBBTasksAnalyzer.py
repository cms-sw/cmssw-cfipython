import FWCore.ParameterSet.Config as cms

def TestTBBTasksAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestTBBTasksAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
