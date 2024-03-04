import FWCore.ParameterSet.Config as cms

def Prescaler(**kwargs):
  mod = cms.EDFilter('Prescaler',
    prescaleFactor = cms.required.int32,
    prescaleOffset = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
