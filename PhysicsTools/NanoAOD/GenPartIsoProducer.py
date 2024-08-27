import FWCore.ParameterSet.Config as cms

def GenPartIsoProducer(**kwargs):
  mod = cms.EDProducer('GenPartIsoProducer',
    genPart = cms.required.InputTag,
    packedGenPart = cms.required.InputTag,
    additionalPdgId = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
