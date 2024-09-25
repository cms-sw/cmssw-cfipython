import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_TestAlpakaGlobalProducerE(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::TestAlpakaGlobalProducerE',
    eventSetupSource = cms.ESInputTag('', ''),
    source = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
