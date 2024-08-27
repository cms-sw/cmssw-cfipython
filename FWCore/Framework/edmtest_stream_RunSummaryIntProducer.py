import FWCore.ParameterSet.Config as cms

def edmtest_stream_RunSummaryIntProducer(**kwargs):
  mod = cms.EDProducer('edmtest::stream::RunSummaryIntProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
