import FWCore.ParameterSet.Config as cms

def L1FastjetCorrectorProducer(*args, **kwargs):
  mod = cms.EDProducer('L1FastjetCorrectorProducer',
    level = cms.string(''),
    algorithm = cms.string(''),
    srcRho = cms.InputTag(''),
    skipMissingProduct = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
