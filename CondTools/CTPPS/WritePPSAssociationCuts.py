import FWCore.ParameterSet.Config as cms

def WritePPSAssociationCuts(**kwargs):
  mod = cms.EDAnalyzer('WritePPSAssociationCuts',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
