import FWCore.ParameterSet.Config as cms

def Pythia6PartonPtGun(**kwargs):
  mod = cms.EDProducer('Pythia6PartonPtGun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
