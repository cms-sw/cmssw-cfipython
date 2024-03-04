import FWCore.ParameterSet.Config as cms

def SiStripDCSFilter(**kwargs):
  mod = cms.EDFilter('SiStripDCSFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
