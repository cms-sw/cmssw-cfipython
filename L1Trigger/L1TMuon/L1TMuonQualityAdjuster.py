import FWCore.ParameterSet.Config as cms

def L1TMuonQualityAdjuster(**kwargs):
  mod = cms.EDProducer('L1TMuonQualityAdjuster',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
