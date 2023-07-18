import FWCore.ParameterSet.Config as cms

offlineBeamSpotToCUDA = cms.EDProducer('BeamSpotToCUDA',
  src = cms.InputTag('offlineBeamSpot'),
  mightGet = cms.optional.untracked.vstring
)
