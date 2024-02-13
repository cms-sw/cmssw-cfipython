import FWCore.ParameterSet.Config as cms

Phase2OTHarvestTrackingParticles = cms.EDProducer('Phase2OTHarvestTrackingParticles',
  TopFolderName = cms.string('TrackerPhase2OTL1TrackV'),
  mightGet = cms.optional.untracked.vstring
)
