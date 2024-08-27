import FWCore.ParameterSet.Config as cms

def DQMHcalIsoTrackAlCaReco(**kwargs):
  mod = cms.EDProducer('DQMHcalIsoTrackAlCaReco',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
