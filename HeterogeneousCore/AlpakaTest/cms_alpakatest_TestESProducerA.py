import FWCore.ParameterSet.Config as cms

def cms_alpakatest_TestESProducerA(*args, **kwargs):
  mod = cms.ESProducer('cms::alpakatest::TestESProducerA',
    value = cms.required.int32,
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
