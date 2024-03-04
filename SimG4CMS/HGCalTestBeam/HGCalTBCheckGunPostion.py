import FWCore.ParameterSet.Config as cms

def HGCalTBCheckGunPostion(**kwargs):
  mod = cms.EDFilter('HGCalTBCheckGunPostion',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
