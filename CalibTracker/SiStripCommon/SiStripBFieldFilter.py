import FWCore.ParameterSet.Config as cms

def SiStripBFieldFilter(**kwargs):
  mod = cms.EDFilter('SiStripBFieldFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
