import FWCore.ParameterSet.Config as cms

def MkFitOutputConverter(**kwargs):
  mod = cms.EDProducer('MkFitOutputConverter',
    mkFitEventOfHits = cms.InputTag('mkFitEventOfHits'),
    mkFitPixelHits = cms.InputTag('mkFitSiPixelHits'),
    mkFitStripHits = cms.InputTag('mkFitSiStripHits'),
    mkFitSeeds = cms.InputTag('mkFitSeedConverter'),
    tracks = cms.InputTag('mkFitProducer'),
    seeds = cms.InputTag('initialStepSeeds'),
    ttrhBuilder = cms.ESInputTag('', 'WithTrackAngle'),
    propagatorAlong = cms.ESInputTag('', 'PropagatorWithMaterial'),
    propagatorOpposite = cms.ESInputTag('', 'PropagatorWithMaterialOpposite'),
    qualityMaxInvPt = cms.double(100),
    qualityMinTheta = cms.double(0.01),
    qualityMaxR = cms.double(120),
    qualityMaxZ = cms.double(280),
    qualityMaxPosErr = cms.double(100),
    qualitySignPt = cms.bool(True),
    doErrorRescale = cms.bool(True),
    tfDnnLabel = cms.string('trackSelectionTf'),
    candMVASel = cms.bool(False),
    candWP = cms.double(0),
    batchSize = cms.int32(16),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
