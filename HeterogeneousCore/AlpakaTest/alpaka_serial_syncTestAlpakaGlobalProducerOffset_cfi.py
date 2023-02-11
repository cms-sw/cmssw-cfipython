import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaGlobalProducerOffset = cms.EDProducer('alpaka_serial_sync::TestAlpakaGlobalProducerOffset',
  xvalue = cms.PSet(
    alpaka_serial_sync = cms.double(0),
    alpaka_cuda_async = cms.double(0)
  ),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
