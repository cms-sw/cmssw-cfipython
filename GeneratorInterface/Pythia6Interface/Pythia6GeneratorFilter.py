import FWCore.ParameterSet.Config as cms

def Pythia6GeneratorFilter(*args, **kwargs):
  mod = cms.EDFilter('Pythia6GeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
