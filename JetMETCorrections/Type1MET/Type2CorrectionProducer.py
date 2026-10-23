import FWCore.ParameterSet.Config as cms

def Type2CorrectionProducer(*args, **kwargs):
  mod = cms.EDProducer('Type2CorrectionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
