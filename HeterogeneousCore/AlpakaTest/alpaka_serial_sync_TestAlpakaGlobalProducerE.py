import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_TestAlpakaGlobalProducerE(**kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::TestAlpakaGlobalProducerE',
    eventSetupSource = cms.ESInputTag('', ''),
    source = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
