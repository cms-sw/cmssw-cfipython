import FWCore.ParameterSet.Config as cms

def DTDeadWrite(**kwargs):
  mod = cms.EDAnalyzer('DTDeadWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
