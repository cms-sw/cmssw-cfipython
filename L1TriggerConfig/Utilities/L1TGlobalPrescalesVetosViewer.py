import FWCore.ParameterSet.Config as cms

def L1TGlobalPrescalesVetosViewer(**kwargs):
  mod = cms.EDAnalyzer('L1TGlobalPrescalesVetosViewer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
