import FWCore.ParameterSet.Config as cms

def edmtest_global_RunSummaryIntProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::global::RunSummaryIntProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
