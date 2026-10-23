import FWCore.ParameterSet.Config as cms

def edmtest_one_WatchLumiBlocksAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::one::WatchLumiBlocksAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
