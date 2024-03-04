import FWCore.ParameterSet.Config as cms

def Geant4ePropagatorAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('Geant4ePropagatorAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
