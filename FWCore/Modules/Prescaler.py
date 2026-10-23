import FWCore.ParameterSet.Config as cms

def Prescaler(*args, **kwargs):
  mod = cms.EDFilter('Prescaler',
    prescaleFactor = cms.required.int32,
    prescaleOffset = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
