import FWCore.ParameterSet.Config as cms

def TrackerRemapper(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackerRemapper',
    src = cms.InputTag('generalTracks'),
    opMode = cms.int32(0),
    analyzeMode = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
