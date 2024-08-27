import FWCore.ParameterSet.Config as cms

def AssociationMapAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('AssociationMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
