import FWCore.ParameterSet.Config as cms

def IsoTracks(**kwargs):
  mod = cms.EDProducer('IsoTracks',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
