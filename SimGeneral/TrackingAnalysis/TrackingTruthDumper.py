import FWCore.ParameterSet.Config as cms

def TrackingTruthDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackingTruthDumper',
    moduleLabelTk = cms.InputTag('mix', 'MergedTrackTruth'),
    moduleLabelVtx = cms.InputTag('mix', 'MergedTrackTruth'),
    dumpVtx = cms.untracked.bool(True),
    dumpTk = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
