import FWCore.ParameterSet.Config as cms

def L1JPTOffsetCorrectorProducer(*args, **kwargs):
  mod = cms.EDProducer('L1JPTOffsetCorrectorProducer',
    level = cms.required.string,
    algorithm = cms.required.string,
    offsetService = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
