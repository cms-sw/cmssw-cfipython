import FWCore.ParameterSet.Config as cms

def LaserAlignmentEventFilter(*args, **kwargs):
  mod = cms.EDFilter('LaserAlignmentEventFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
