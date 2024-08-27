import FWCore.ParameterSet.Config as cms

def Pythia6PtYDistGun(**kwargs):
  mod = cms.EDProducer('Pythia6PtYDistGun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
