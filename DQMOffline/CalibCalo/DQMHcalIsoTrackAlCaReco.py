import FWCore.ParameterSet.Config as cms

def DQMHcalIsoTrackAlCaReco(*args, **kwargs):
  mod = cms.EDProducer('DQMHcalIsoTrackAlCaReco',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
