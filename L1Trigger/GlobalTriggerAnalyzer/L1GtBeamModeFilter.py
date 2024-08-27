import FWCore.ParameterSet.Config as cms

def L1GtBeamModeFilter(**kwargs):
  mod = cms.EDFilter('L1GtBeamModeFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
