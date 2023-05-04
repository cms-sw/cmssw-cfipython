import FWCore.ParameterSet.Config as cms

cscOverlapsTrackPreparation = cms.EDProducer('CSCOverlapsTrackPreparation',
  src = cms.InputTag('ALCARECOMuAlBeamHaloOverlaps'),
  mightGet = cms.optional.untracked.vstring
)
