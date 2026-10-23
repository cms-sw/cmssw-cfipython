import FWCore.ParameterSet.Config as cms

def L1TrackNtupleMaker(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TrackNtupleMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
