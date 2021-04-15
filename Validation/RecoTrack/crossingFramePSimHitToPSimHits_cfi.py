import FWCore.ParameterSet.Config as cms

crossingFramePSimHitToPSimHits = cms.EDProducer('CrossingFramePSimHitToPSimHitsConverter',
  src = cms.VInputTag(),
  mightGet = cms.optional.untracked.vstring
)
