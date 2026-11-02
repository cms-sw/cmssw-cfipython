import FWCore.ParameterSet.Config as cms

def TruthGraphMetadataProducer(*args, **kwargs):
  mod = cms.EDProducer('TruthGraphMetadataProducer',
    graphProducer = cms.string('truthLogicalGraphProducer'),
    rawGraphProducer = cms.string('mix'),
    hitIndexProducer = cms.string('truthLogicalGraphHitIndexProducer'),
    generatorLabel = cms.string('generator'),
    generatorName = cms.string(''),
    generatorVersion = cms.string(''),
    generatorFragment = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
