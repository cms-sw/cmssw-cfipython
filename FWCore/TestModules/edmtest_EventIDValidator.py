import FWCore.ParameterSet.Config as cms

def edmtest_EventIDValidator(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::EventIDValidator',
    source = cms.untracked.InputTag('eventIDProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
