import FWCore.ParameterSet.Config as cms

def L1OffsetCorrectorProducer(**kwargs):
  mod = cms.EDProducer('L1OffsetCorrectorProducer',
    level = cms.required.string,
    algorithm = cms.required.string,
    vertexCollection = cms.required.InputTag,
    minVtxNdof = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
