import FWCore.ParameterSet.Config as cms

def SiStripDetWithDigi(*args, **kwargs):
  mod = cms.EDFilter('SiStripDetWithDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
