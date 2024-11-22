import FWCore.ParameterSet.Config as cms

def L1OffsetCorrectorProducer(*args, **kwargs):
  mod = cms.EDProducer('L1OffsetCorrectorProducer',
    level = cms.required.string,
    algorithm = cms.required.string,
    vertexCollection = cms.required.InputTag,
    minVtxNdof = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
