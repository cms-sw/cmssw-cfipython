import FWCore.ParameterSet.Config as cms

def SecondaryVertexTagInfoCategorySelector(*args, **kwargs):
  mod = cms.EDFilter('SecondaryVertexTagInfoCategorySelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
