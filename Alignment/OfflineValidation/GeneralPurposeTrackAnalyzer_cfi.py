import FWCore.ParameterSet.Config as cms

GeneralPurposeTrackAnalyzer = cms.EDAnalyzer('GeneralPurposeTrackAnalyzer',
  TkTag = cms.InputTag('generalTracks'),
  TriggerResultsTag = cms.InputTag('TriggerResults', '', 'HLT'),
  BeamSpotTag = cms.InputTag('offlineBeamSpot'),
  VerticesTag = cms.InputTag('offlinePrimaryVertices'),
  isCosmics = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
