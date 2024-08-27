import FWCore.ParameterSet.Config as cms

def Pythia8JetGun(**kwargs):
  mod = cms.EDFilter('Pythia8JetGun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
