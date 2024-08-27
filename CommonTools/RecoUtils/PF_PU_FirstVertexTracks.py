import FWCore.ParameterSet.Config as cms

def PF_PU_FirstVertexTracks(**kwargs):
  mod = cms.EDProducer('PF_PU_FirstVertexTracks',
    AssociationType = cms.required.InputTag,
    AssociationMap = cms.required.InputTag,
    TrackCollection = cms.required.InputTag,
    VertexCollection = cms.required.InputTag,
    MinQuality = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
