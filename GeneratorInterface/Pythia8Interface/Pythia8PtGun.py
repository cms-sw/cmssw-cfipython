import FWCore.ParameterSet.Config as cms

def Pythia8PtGun(*args, **kwargs):
  mod = cms.EDFilter('Pythia8PtGun',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
