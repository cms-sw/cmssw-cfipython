import FWCore.ParameterSet.Config as cms

def DTt0DBValidation(*args, **kwargs):
  mod = cms.EDAnalyzer('DTt0DBValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
