import FWCore.ParameterSet.Config as cms

def Pythia8PtotGun(*args, **kwargs):
  mod = cms.EDFilter('Pythia8PtotGun',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
