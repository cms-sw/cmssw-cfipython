import FWCore.ParameterSet.Config as cms

def Pythia8PtotGun(**kwargs):
  mod = cms.EDFilter('Pythia8PtotGun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
