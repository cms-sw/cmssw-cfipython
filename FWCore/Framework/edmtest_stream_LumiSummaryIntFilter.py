import FWCore.ParameterSet.Config as cms

def edmtest_stream_LumiSummaryIntFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::stream::LumiSummaryIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
