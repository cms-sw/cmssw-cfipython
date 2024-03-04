import FWCore.ParameterSet.Config as cms

def edmtest_one_WatchRunsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('edmtest::one::WatchRunsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
