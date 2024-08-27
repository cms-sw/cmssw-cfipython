import FWCore.ParameterSet.Config as cms

def L1GctValidation(**kwargs):
  mod = cms.EDAnalyzer('L1GctValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
