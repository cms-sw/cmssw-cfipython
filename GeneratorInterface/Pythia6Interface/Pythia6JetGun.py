import FWCore.ParameterSet.Config as cms

def Pythia6JetGun(**kwargs):
  mod = cms.EDProducer('Pythia6JetGun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
