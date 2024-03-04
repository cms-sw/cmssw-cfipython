import FWCore.ParameterSet.Config as cms

def L1FastjetCorrectorProducer(**kwargs):
  mod = cms.EDProducer('L1FastjetCorrectorProducer',
    level = cms.required.string,
    algorithm = cms.required.string,
    srcRho = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
