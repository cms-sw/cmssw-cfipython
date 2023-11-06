import FWCore.ParameterSet.Config as cms

muonBeamspotConstraintValueMapProducer = cms.EDProducer('MuonBeamspotConstraintValueMapProducer',
  src = cms.InputTag('muons'),
  beamspot = cms.InputTag('offlineBeamSpot'),
  vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
  mightGet = cms.optional.untracked.vstring
)
