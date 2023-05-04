import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncTestAlpakaStreamProducer = cms.EDProducer('alpaka_rocm_async::TestAlpakaStreamProducer',
  source = cms.required.InputTag,
  eventSetupSource = cms.ESInputTag('', ''),
  productInstanceName = cms.string(''),
  size = cms.PSet(
    alpaka_serial_sync = cms.required.int32,
    alpaka_cuda_async = cms.required.int32
  ),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
