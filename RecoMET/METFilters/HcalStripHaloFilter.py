import FWCore.ParameterSet.Config as cms

def HcalStripHaloFilter(**kwargs):
  mod = cms.EDFilter('HcalStripHaloFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
