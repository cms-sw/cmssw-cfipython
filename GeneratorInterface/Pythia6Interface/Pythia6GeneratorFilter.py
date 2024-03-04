import FWCore.ParameterSet.Config as cms

def Pythia6GeneratorFilter(**kwargs):
  mod = cms.EDFilter('Pythia6GeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
