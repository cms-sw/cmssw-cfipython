import FWCore.ParameterSet.Config as cms

def Geant4ePropagatorAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('Geant4ePropagatorAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
