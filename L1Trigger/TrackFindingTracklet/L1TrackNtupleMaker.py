import FWCore.ParameterSet.Config as cms

def L1TrackNtupleMaker(**kwargs):
  mod = cms.EDAnalyzer('L1TrackNtupleMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
