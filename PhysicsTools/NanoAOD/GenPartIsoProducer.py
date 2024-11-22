import FWCore.ParameterSet.Config as cms

def GenPartIsoProducer(*args, **kwargs):
  mod = cms.EDProducer('GenPartIsoProducer',
    genPart = cms.required.InputTag,
    packedGenPart = cms.required.InputTag,
    additionalPdgId = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
