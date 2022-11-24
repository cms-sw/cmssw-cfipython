import FWCore.ParameterSet.Config as cms

JetHTAnalyzer = cms.EDAnalyzer('JetHTAnalyzer',
  vtxCollection = cms.InputTag('offlinePrimaryVerticesFromRefittedTrks'),
  triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
  trackCollection = cms.InputTag('TrackRefitter'),
  mightGet = cms.optional.untracked.vstring
)
