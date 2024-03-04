import FWCore.ParameterSet.Config as cms

def GsfTrackRefitter(**kwargs):
  mod = cms.EDProducer('GsfTrackRefitter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
