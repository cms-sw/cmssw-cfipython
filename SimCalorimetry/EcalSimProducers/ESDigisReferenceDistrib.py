import FWCore.ParameterSet.Config as cms

def ESDigisReferenceDistrib(*args, **kwargs):
  mod = cms.EDAnalyzer('ESDigisReferenceDistrib',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
