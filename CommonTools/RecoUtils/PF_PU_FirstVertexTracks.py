import FWCore.ParameterSet.Config as cms

def PF_PU_FirstVertexTracks(*args, **kwargs):
  mod = cms.EDProducer('PF_PU_FirstVertexTracks',
    AssociationType = cms.required.InputTag,
    AssociationMap = cms.required.InputTag,
    TrackCollection = cms.required.InputTag,
    VertexCollection = cms.required.InputTag,
    MinQuality = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
