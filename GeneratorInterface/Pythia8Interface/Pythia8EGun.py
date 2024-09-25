import FWCore.ParameterSet.Config as cms

def Pythia8EGun(*args, **kwargs):
  mod = cms.EDFilter('Pythia8EGun',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
