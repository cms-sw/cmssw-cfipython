import FWCore.ParameterSet.Config as cms

def TrackMatchedJetProducer(**kwargs):
  mod = cms.EDProducer('TrackMatchedJetProducer',
    srcObject = cms.required.InputTag,
    srcObjectsToMatch = cms.required.VInputTag,
    deltaRMax = cms.required.double,
    srcObjectSelection = cms.string(''),
    srcObjectsToMatchSelection = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
