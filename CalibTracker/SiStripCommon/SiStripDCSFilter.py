import FWCore.ParameterSet.Config as cms

def SiStripDCSFilter(*args, **kwargs):
  mod = cms.EDFilter('SiStripDCSFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
