import FWCore.ParameterSet.Config as cms

def HcalCalibTypeFilter(*args, **kwargs):
  mod = cms.EDFilter('HcalCalibTypeFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
