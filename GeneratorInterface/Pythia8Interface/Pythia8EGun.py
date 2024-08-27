import FWCore.ParameterSet.Config as cms

def Pythia8EGun(**kwargs):
  mod = cms.EDFilter('Pythia8EGun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
