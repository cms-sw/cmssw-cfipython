import FWCore.ParameterSet.Config as cms

def edmtest_one_WatchLumiBlocksFilter(**kwargs):
  mod = cms.EDFilter('edmtest::one::WatchLumiBlocksFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
