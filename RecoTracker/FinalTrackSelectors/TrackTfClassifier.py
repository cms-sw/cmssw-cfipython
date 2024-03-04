import FWCore.ParameterSet.Config as cms

def TrackTfClassifier(**kwargs):
  mod = cms.EDProducer('TrackTfClassifier',
    src = cms.InputTag(''),
    beamspot = cms.InputTag('offlineBeamSpot'),
    vertices = cms.InputTag('firstStepPrimaryVertices'),
    ignoreVertices = cms.bool(False),
    qualityCuts = cms.vdouble(
      -0.7,
      0.1,
      0.7
    ),
    mva = cms.PSet(
      tfDnnLabel = cms.string('trackSelectionTf'),
      batchSize = cms.int32(16)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
