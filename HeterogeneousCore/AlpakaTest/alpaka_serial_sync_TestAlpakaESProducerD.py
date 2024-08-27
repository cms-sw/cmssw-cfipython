import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_TestAlpakaESProducerD(**kwargs):
  mod = cms.ESProducer('alpaka_serial_sync::TestAlpakaESProducerD',
    srcA = cms.ESInputTag('', ''),
    srcB = cms.ESInputTag('', ''),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
