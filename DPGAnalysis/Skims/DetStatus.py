import FWCore.ParameterSet.Config as cms

def DetStatus(**kwargs):
  mod = cms.EDFilter('DetStatus',
    DebugOn = cms.untracked.bool(False),
    AndOr = cms.bool(True),
    ApplyFilter = cms.bool(True),
    DetectorType = cms.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
