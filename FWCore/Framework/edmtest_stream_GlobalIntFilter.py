import FWCore.ParameterSet.Config as cms

def edmtest_stream_GlobalIntFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::stream::GlobalIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
