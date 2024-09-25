import FWCore.ParameterSet.Config as cms

def edmtest_StreamIDFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::StreamIDFilter',
    rejectStreams = cms.required.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
