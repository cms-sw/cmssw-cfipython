import FWCore.ParameterSet.Config as cms

def L1GctValidation(*args, **kwargs):
  mod = cms.EDAnalyzer('L1GctValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
