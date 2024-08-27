import FWCore.ParameterSet.Config as cms

def L1TGlobalPrescalesVetosWriter(**kwargs):
  mod = cms.EDAnalyzer('L1TGlobalPrescalesVetosWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
