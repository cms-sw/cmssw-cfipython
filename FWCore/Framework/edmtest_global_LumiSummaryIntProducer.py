import FWCore.ParameterSet.Config as cms

def edmtest_global_LumiSummaryIntProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::global::LumiSummaryIntProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
