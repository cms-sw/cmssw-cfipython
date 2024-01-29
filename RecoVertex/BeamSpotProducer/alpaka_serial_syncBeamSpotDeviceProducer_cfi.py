import FWCore.ParameterSet.Config as cms

alpaka_serial_syncBeamSpotDeviceProducer = cms.EDProducer('alpaka_serial_sync::BeamSpotDeviceProducer',
  src = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
