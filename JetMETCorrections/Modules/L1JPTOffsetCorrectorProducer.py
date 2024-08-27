import FWCore.ParameterSet.Config as cms

def L1JPTOffsetCorrectorProducer(**kwargs):
  mod = cms.EDProducer('L1JPTOffsetCorrectorProducer',
    level = cms.required.string,
    algorithm = cms.required.string,
    offsetService = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
