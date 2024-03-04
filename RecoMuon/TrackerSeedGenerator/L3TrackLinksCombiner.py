import FWCore.ParameterSet.Config as cms

def L3TrackLinksCombiner(**kwargs):
  mod = cms.EDProducer('L3TrackLinksCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
