import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaGlobalProducer = cms.EDProducer('alpaka_serial_sync::TestAlpakaGlobalProducer',
  eventSetupSource = cms.ESInputTag('', ''),
  size = cms.PSet(
    alpaka_serial_sync = cms.required.int32,
    alpaka_cuda_async = cms.required.int32
  ),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
