import FWCore.ParameterSet.Config as cms

def edmtest_TestServicesOnNonFrameworkThreadsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('edmtest::TestServicesOnNonFrameworkThreadsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
