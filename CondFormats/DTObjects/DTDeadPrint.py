import FWCore.ParameterSet.Config as cms

def DTDeadPrint(*args, **kwargs):
  mod = cms.EDAnalyzer('DTDeadPrint',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
