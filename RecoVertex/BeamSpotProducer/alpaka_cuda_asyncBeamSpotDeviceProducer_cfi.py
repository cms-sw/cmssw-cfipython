import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncBeamSpotDeviceProducer = cms.EDProducer('alpaka_cuda_async::BeamSpotDeviceProducer',
  src = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
