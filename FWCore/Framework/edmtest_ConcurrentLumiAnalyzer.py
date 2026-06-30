import FWCore.ParameterSet.Config as cms

def edmtest_ConcurrentLumiAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::ConcurrentLumiAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
