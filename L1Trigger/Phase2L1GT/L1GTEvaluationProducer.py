import FWCore.ParameterSet.Config as cms

def L1GTEvaluationProducer(**kwargs):
  mod = cms.EDProducer('L1GTEvaluationProducer',
    random_seed = cms.optional.uint32,
    maxLines = cms.uint32(1024),
    outputFilename = cms.required.string,
    outputFileExtension = cms.string('txt'),
    patternFormat = cms.string('EMPv2'),
    platform = cms.string('VU9P'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
