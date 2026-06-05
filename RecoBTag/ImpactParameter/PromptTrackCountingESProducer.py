import FWCore.ParameterSet.Config as cms

def PromptTrackCountingESProducer(*args, **kwargs):
  mod = cms.ESProducer('PromptTrackCountingESProducer',
    nthTrack = cms.int32(-1),
    impactParameterType = cms.int32(0),
    deltaR = cms.double(-1),
    deltaRmin = cms.double(0),
    maxImpactParameter = cms.double(0.1),
    maxImpactParameterSig = cms.double(999999),
    maximumDecayLength = cms.double(999999),
    maximumDistanceToJetAxis = cms.double(999999),
    trackQualityClass = cms.string('any'),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
