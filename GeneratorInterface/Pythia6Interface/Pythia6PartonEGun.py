import FWCore.ParameterSet.Config as cms

def Pythia6PartonEGun(**kwargs):
  mod = cms.EDProducer('Pythia6PartonEGun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
