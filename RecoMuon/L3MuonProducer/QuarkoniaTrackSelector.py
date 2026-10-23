import FWCore.ParameterSet.Config as cms

def QuarkoniaTrackSelector(*args, **kwargs):
  mod = cms.EDProducer('QuarkoniaTrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
