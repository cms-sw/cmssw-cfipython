import FWCore.ParameterSet.Config as cms

def edmtest_stream_InputProcessBlockIntFilterG(**kwargs):
  mod = cms.EDFilter('edmtest::stream::InputProcessBlockIntFilterG',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
