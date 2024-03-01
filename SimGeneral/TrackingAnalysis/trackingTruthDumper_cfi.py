import FWCore.ParameterSet.Config as cms

trackingTruthDumper = cms.EDAnalyzer('TrackingTruthDumper',
  moduleLabelTk = cms.InputTag('mix', 'MergedTrackTruth'),
  moduleLabelVtx = cms.InputTag('mix', 'MergedTrackTruth'),
  dumpVtx = cms.untracked.bool(True),
  dumpTk = cms.untracked.bool(True),
  mightGet = cms.optional.untracked.vstring
)
