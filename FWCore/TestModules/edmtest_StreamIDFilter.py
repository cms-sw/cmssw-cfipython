import FWCore.ParameterSet.Config as cms

def edmtest_StreamIDFilter(**kwargs):
  mod = cms.EDFilter('edmtest::StreamIDFilter',
    rejectStreams = cms.required.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
