import FWCore.ParameterSet.Config as cms

beamSpotDeviceProducer = cms.EDProducer('BeamSpotDeviceProducer@alpaka',
  src = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
