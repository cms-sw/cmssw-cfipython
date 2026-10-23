import FWCore.ParameterSet.Config as cms

def edmtest_stream_RunSummaryIntFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::stream::RunSummaryIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
