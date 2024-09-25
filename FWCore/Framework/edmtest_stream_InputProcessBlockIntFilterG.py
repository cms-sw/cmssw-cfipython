import FWCore.ParameterSet.Config as cms

def edmtest_stream_InputProcessBlockIntFilterG(*args, **kwargs):
  mod = cms.EDFilter('edmtest::stream::InputProcessBlockIntFilterG',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
