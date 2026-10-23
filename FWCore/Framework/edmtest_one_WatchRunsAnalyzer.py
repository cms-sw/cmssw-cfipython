import FWCore.ParameterSet.Config as cms

def edmtest_one_WatchRunsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::one::WatchRunsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
