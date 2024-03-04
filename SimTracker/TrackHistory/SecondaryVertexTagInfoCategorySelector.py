import FWCore.ParameterSet.Config as cms

def SecondaryVertexTagInfoCategorySelector(**kwargs):
  mod = cms.EDFilter('SecondaryVertexTagInfoCategorySelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
