import FWCore.ParameterSet.Config as cms

def Pythia6PtGun(**kwargs):
  mod = cms.EDProducer('Pythia6PtGun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
