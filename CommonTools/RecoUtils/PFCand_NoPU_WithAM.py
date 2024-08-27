import FWCore.ParameterSet.Config as cms

def PFCand_NoPU_WithAM(**kwargs):
  mod = cms.EDProducer('PFCand_NoPU_WithAM',
    AssociationType = cms.required.InputTag,
    VertexPFCandAssociationMap = cms.required.InputTag,
    VertexCollection = cms.required.InputTag,
    MinQuality = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
