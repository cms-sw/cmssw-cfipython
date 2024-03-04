import FWCore.ParameterSet.Config as cms

def CosMuoGenProducer(**kwargs):
  mod = cms.EDProducer('CosMuoGenProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
