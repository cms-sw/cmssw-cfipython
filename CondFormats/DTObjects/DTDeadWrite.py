import FWCore.ParameterSet.Config as cms

def DTDeadWrite(*args, **kwargs):
  mod = cms.EDAnalyzer('DTDeadWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
