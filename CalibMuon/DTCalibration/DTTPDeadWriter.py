import FWCore.ParameterSet.Config as cms

def DTTPDeadWriter(**kwargs):
  mod = cms.EDAnalyzer('DTTPDeadWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
