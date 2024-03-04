import FWCore.ParameterSet.Config as cms

def MagneticFieldFilter(**kwargs):
  mod = cms.EDFilter('MagneticFieldFilter',
    magneticField = cms.untracked.int32(38),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
