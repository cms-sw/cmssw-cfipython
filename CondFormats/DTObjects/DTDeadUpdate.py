import FWCore.ParameterSet.Config as cms

def DTDeadUpdate(*args, **kwargs):
  mod = cms.EDAnalyzer('DTDeadUpdate',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
