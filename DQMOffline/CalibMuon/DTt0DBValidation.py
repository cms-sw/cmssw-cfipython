import FWCore.ParameterSet.Config as cms

def DTt0DBValidation(**kwargs):
  mod = cms.EDAnalyzer('DTt0DBValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
