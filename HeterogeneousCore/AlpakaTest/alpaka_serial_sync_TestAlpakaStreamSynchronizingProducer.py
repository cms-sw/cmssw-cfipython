import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_TestAlpakaStreamSynchronizingProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::TestAlpakaStreamSynchronizingProducer',
    source = cms.required.InputTag,
    intSource = cms.required.InputTag,
    expectedInt = cms.required.int32,
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
