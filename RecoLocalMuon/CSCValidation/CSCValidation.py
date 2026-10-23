import FWCore.ParameterSet.Config as cms

def CSCValidation(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
