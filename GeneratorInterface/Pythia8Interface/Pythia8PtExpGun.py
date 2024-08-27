import FWCore.ParameterSet.Config as cms

def Pythia8PtExpGun(**kwargs):
  mod = cms.EDFilter('Pythia8PtExpGun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
