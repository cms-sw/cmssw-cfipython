import FWCore.ParameterSet.Config as cms

def TestTBBTasksAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestTBBTasksAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
