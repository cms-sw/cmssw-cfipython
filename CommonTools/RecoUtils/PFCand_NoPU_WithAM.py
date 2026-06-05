import FWCore.ParameterSet.Config as cms

def PFCand_NoPU_WithAM(*args, **kwargs):
  mod = cms.EDProducer('PFCand_NoPU_WithAM',
    AssociationType = cms.required.InputTag,
    VertexPFCandAssociationMap = cms.required.InputTag,
    VertexCollection = cms.required.InputTag,
    MinQuality = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
