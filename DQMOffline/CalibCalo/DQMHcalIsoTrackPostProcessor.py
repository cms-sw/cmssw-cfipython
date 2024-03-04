import FWCore.ParameterSet.Config as cms

def DQMHcalIsoTrackPostProcessor(**kwargs):
  mod = cms.EDProducer('DQMHcalIsoTrackPostProcessor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
