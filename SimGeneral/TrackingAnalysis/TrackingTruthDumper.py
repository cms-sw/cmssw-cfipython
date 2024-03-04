import FWCore.ParameterSet.Config as cms

def TrackingTruthDumper(**kwargs):
  mod = cms.EDAnalyzer('TrackingTruthDumper',
    moduleLabelTk = cms.InputTag('mix', 'MergedTrackTruth'),
    moduleLabelVtx = cms.InputTag('mix', 'MergedTrackTruth'),
    dumpVtx = cms.untracked.bool(True),
    dumpTk = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
