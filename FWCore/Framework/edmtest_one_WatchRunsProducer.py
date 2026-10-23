import FWCore.ParameterSet.Config as cms

def edmtest_one_WatchRunsProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::one::WatchRunsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
