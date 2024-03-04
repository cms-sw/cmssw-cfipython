import FWCore.ParameterSet.Config as cms

def GeneralPurposeTrackAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('GeneralPurposeTrackAnalyzer',
    TkTag = cms.InputTag('generalTracks'),
    TriggerResultsTag = cms.InputTag('TriggerResults', '', 'HLT'),
    BeamSpotTag = cms.InputTag('offlineBeamSpot'),
    VerticesTag = cms.InputTag('offlinePrimaryVertices'),
    isCosmics = cms.bool(False),
    doLatencyAnalysis = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
