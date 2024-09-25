import FWCore.ParameterSet.Config as cms

def TrackMatchedPhotonProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackMatchedPhotonProducer',
    srcObject = cms.required.InputTag,
    srcObjectsToMatch = cms.required.VInputTag,
    deltaRMax = cms.required.double,
    srcObjectSelection = cms.string(''),
    srcObjectsToMatchSelection = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
