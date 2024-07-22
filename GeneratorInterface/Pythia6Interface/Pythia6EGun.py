import FWCore.ParameterSet.Config as cms

def Pythia6EGun(**kwargs):
  mod = cms.EDProducer('Pythia6EGun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod