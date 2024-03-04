import FWCore.ParameterSet.Config as cms

def SiStripDetWithCluster(**kwargs):
  mod = cms.EDFilter('SiStripDetWithCluster',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
