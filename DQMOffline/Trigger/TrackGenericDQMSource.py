import FWCore.ParameterSet.Config as cms

def TrackGenericDQMSource(*args, **kwargs):
  mod = cms.EDProducer('TrackGenericDQMSource',
    src = cms.required.InputTag,
    folder = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
