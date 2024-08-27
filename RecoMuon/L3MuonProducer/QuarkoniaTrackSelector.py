import FWCore.ParameterSet.Config as cms

def QuarkoniaTrackSelector(**kwargs):
  mod = cms.EDProducer('QuarkoniaTrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
