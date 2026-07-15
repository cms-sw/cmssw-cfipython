import FWCore.ParameterSet.Config as cms

def TrackTorchClassifierAlpaka_alpaka(*args, **kwargs):
  mod = cms.EDProducer('TrackTorchClassifierAlpaka@alpaka',
    modelPath = cms.FileInPath('RecoTracker/FinalTrackSelectors/data/TrackTorchClassifier/model.pt'),
    features = cms.InputTag('hltInitialStepTrackFeatureExtractor'),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
