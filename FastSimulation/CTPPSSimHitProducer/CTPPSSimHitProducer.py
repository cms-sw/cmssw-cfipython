import FWCore.ParameterSet.Config as cms

def CTPPSSimHitProducer(**kwargs):
  mod = cms.EDProducer('CTPPSSimHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
