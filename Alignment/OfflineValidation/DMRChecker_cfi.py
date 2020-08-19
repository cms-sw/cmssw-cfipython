import FWCore.ParameterSet.Config as cms

DMRChecker = cms.EDAnalyzer('DMRChecker',
  TkTag = cms.InputTag('generalTracks'),
  TriggerResultsTag = cms.InputTag('TriggerResults', '', 'HLT'),
  BeamSpotTag = cms.InputTag('offlineBeamSpot'),
  VerticesTag = cms.InputTag('offlinePrimaryVertices'),
  isCosmics = cms.bool(False),
  isPhase1 = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
