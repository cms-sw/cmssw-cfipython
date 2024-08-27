import FWCore.ParameterSet.Config as cms

def HcalCalibTypeFilter(**kwargs):
  mod = cms.EDFilter('HcalCalibTypeFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
