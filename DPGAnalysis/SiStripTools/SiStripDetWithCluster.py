import FWCore.ParameterSet.Config as cms

def SiStripDetWithCluster(*args, **kwargs):
  mod = cms.EDFilter('SiStripDetWithCluster',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
