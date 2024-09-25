import FWCore.ParameterSet.Config as cms

def Pythia8PtAndDxyGun(*args, **kwargs):
  mod = cms.EDFilter('Pythia8PtAndDxyGun',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
