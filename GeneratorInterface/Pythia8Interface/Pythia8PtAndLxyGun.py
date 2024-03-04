import FWCore.ParameterSet.Config as cms

def Pythia8PtAndLxyGun(**kwargs):
  mod = cms.EDFilter('Pythia8PtAndLxyGun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
