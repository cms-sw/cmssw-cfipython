import FWCore.ParameterSet.Config as cms

def DTDeadUpdate(**kwargs):
  mod = cms.EDAnalyzer('DTDeadUpdate',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
