import FWCore.ParameterSet.Config as cms

def CSCValidation(**kwargs):
  mod = cms.EDAnalyzer('CSCValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
