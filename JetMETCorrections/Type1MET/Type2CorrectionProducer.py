import FWCore.ParameterSet.Config as cms

def Type2CorrectionProducer(**kwargs):
  mod = cms.EDProducer('Type2CorrectionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
