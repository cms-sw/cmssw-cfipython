import FWCore.ParameterSet.Config as cms

def MagneticFieldFilter(*args, **kwargs):
  mod = cms.EDFilter('MagneticFieldFilter',
    magneticField = cms.untracked.int32(38),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
