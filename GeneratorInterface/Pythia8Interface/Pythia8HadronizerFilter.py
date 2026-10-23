import FWCore.ParameterSet.Config as cms

def Pythia8HadronizerFilter(*args, **kwargs):
  mod = cms.EDFilter('Pythia8HadronizerFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
