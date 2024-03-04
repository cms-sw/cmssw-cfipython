import FWCore.ParameterSet.Config as cms

def TrackMVAClassifierDetached(**kwargs):
  mod = cms.EDProducer('TrackMVAClassifierDetached',
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
      GBRForestLabel = cms.string(''),
      GBRForestFileName = cms.string('')
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
