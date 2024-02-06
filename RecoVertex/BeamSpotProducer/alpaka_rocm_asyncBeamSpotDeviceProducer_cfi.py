import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncBeamSpotDeviceProducer = cms.EDProducer('alpaka_rocm_async::BeamSpotDeviceProducer',
  src = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
