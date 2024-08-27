import FWCore.ParameterSet.Config as cms

def TBHodoActiveVolumeRawInfoProducer(**kwargs):
  mod = cms.EDProducer('TBHodoActiveVolumeRawInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
