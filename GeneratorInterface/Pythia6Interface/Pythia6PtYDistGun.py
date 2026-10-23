import FWCore.ParameterSet.Config as cms

def Pythia6PtYDistGun(*args, **kwargs):
  mod = cms.EDProducer('Pythia6PtYDistGun',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
