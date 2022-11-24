import FWCore.ParameterSet.Config as cms

SeedingOTEDProducer = cms.EDProducer('SeedingOTEDProducer',
  src = cms.InputTag('siPhase2VectorHits', 'accepted'),
  trackerEvent = cms.InputTag('MeasurementTrackerEvent'),
  beamSpotLabel = cms.InputTag('offlineBeamSpot'),
  updator = cms.string('KFUpdator'),
  mightGet = cms.optional.untracked.vstring
)
