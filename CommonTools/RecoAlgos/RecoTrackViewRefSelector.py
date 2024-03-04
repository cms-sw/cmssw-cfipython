import FWCore.ParameterSet.Config as cms

def RecoTrackViewRefSelector(**kwargs):
  mod = cms.EDProducer('RecoTrackViewRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
