import FWCore.ParameterSet.Config as cms

def TrackMVAClassifierPrompt(*args, **kwargs):
  mod = cms.EDProducer('TrackMVAClassifierPrompt',
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
