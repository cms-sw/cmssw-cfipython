import FWCore.ParameterSet.Config as cms

def L1FastjetCorrectorProducer(*args, **kwargs):
  mod = cms.EDProducer('L1FastjetCorrectorProducer',
    level = cms.required.string,
    algorithm = cms.required.string,
    srcRho = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
