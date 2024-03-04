import FWCore.ParameterSet.Config as cms

def LaserAlignmentEventFilter(**kwargs):
  mod = cms.EDFilter('LaserAlignmentEventFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
