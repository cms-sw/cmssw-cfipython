import FWCore.ParameterSet.Config as cms

def GeneralPurposeTrackAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('GeneralPurposeTrackAnalyzer',
    TkTag = cms.InputTag('generalTracks'),
    TriggerResultsTag = cms.InputTag('TriggerResults', '', 'HLT'),
    BeamSpotTag = cms.InputTag('offlineBeamSpot'),
    VerticesTag = cms.InputTag('offlinePrimaryVertices'),
    isCosmics = cms.bool(False),
    doLatencyAnalysis = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
