import FWCore.ParameterSet.Config as cms

def ESDigisReferenceDistrib(**kwargs):
  mod = cms.EDAnalyzer('ESDigisReferenceDistrib',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
