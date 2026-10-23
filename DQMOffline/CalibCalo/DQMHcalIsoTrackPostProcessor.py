import FWCore.ParameterSet.Config as cms

def DQMHcalIsoTrackPostProcessor(*args, **kwargs):
  mod = cms.EDProducer('DQMHcalIsoTrackPostProcessor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
