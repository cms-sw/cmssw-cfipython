import FWCore.ParameterSet.Config as cms

def TrackerRemapper(**kwargs):
  mod = cms.EDAnalyzer('TrackerRemapper',
    src = cms.InputTag('generalTracks'),
    opMode = cms.int32(0),
    analyzeMode = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
