import FWCore.ParameterSet.Config as cms

def TrackTorchClassifierFromSoA(*args, **kwargs):
  mod = cms.EDProducer('TrackTorchClassifierFromSoA',
    src = cms.InputTag('hltInitialStepTracks'),
    scores = cms.InputTag('hltInitialStepTrackTorchClassifier'),
    features = cms.InputTag('hltInitialStepTrackTorchClassifier'),
    copyTrajectories = cms.bool(False),
    minScore = cms.double(0.5),
    dxyThreshold = cms.double(0.5),
    highDxyMinScore = cms.double(0.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
