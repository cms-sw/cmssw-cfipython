import FWCore.ParameterSet.Config as cms

def Pythia8PtGun(**kwargs):
  mod = cms.EDFilter('Pythia8PtGun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
