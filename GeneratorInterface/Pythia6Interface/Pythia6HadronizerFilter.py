import FWCore.ParameterSet.Config as cms

def Pythia6HadronizerFilter(*args, **kwargs):
  mod = cms.EDFilter('Pythia6HadronizerFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
