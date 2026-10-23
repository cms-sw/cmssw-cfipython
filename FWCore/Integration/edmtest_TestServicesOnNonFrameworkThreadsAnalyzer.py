import FWCore.ParameterSet.Config as cms

def edmtest_TestServicesOnNonFrameworkThreadsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::TestServicesOnNonFrameworkThreadsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
