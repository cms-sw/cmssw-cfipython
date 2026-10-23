import FWCore.ParameterSet.Config as cms

def DetStatus(*args, **kwargs):
  mod = cms.EDFilter('DetStatus',
    DebugOn = cms.untracked.bool(False),
    AndOr = cms.bool(True),
    ApplyFilter = cms.bool(True),
    DetectorType = cms.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
