import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_TestAlpakaESProducerB(*args, **kwargs):
  mod = cms.ESProducer('alpaka_serial_sync::TestAlpakaESProducerB',
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
