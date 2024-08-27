import FWCore.ParameterSet.Config as cms

def cms_alpakatest_TestESProducerA(**kwargs):
  mod = cms.ESProducer('cms::alpakatest::TestESProducerA',
    value = cms.required.int32,
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
