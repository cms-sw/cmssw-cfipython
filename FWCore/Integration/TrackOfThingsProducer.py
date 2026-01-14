import FWCore.ParameterSet.Config as cms

def TrackOfThingsProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackOfThingsProducer',
    inputTag = cms.required.InputTag,
    keysToReference = cms.required.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
