import FWCore.ParameterSet.Config as cms

def TestAlpakaESProducerB_alpaka(*args, **kwargs):
  mod = cms.ESProducer('TestAlpakaESProducerB@alpaka',
    explicitLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
