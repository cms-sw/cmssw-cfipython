import FWCore.ParameterSet.Config as cms

def Pythia6PartonPtGun(*args, **kwargs):
  mod = cms.EDProducer('Pythia6PartonPtGun',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
