import FWCore.ParameterSet.Config as cms

def SiStripCommissioningBasicPrescaler(**kwargs):
  mod = cms.EDFilter('SiStripCommissioningBasicPrescaler',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
