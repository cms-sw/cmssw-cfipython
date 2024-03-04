import FWCore.ParameterSet.Config as cms

def Pythia8PtAndDxyGun(**kwargs):
  mod = cms.EDFilter('Pythia8PtAndDxyGun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
