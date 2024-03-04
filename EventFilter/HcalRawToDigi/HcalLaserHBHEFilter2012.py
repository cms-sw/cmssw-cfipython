import FWCore.ParameterSet.Config as cms

def HcalLaserHBHEFilter2012(**kwargs):
  mod = cms.EDFilter('HcalLaserHBHEFilter2012',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
