import FWCore.ParameterSet.Config as cms

def GsfTrackRefitter(*args, **kwargs):
  mod = cms.EDProducer('GsfTrackRefitter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
