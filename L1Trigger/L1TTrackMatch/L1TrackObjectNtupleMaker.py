import FWCore.ParameterSet.Config as cms

def L1TrackObjectNtupleMaker(**kwargs):
  mod = cms.EDAnalyzer('L1TrackObjectNtupleMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
