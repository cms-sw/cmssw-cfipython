import FWCore.ParameterSet.Config as cms

def edmtest_stream_ProcessBlockIntFilter(**kwargs):
  mod = cms.EDFilter('edmtest::stream::ProcessBlockIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
