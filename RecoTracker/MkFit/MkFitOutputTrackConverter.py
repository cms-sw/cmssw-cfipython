import FWCore.ParameterSet.Config as cms

def MkFitOutputTrackConverter(*args, **kwargs):
  mod = cms.EDProducer('MkFitOutputTrackConverter',
    mkFitEventOfHits = cms.InputTag('mkFitEventOfHits'),
    mkFitPixelHits = cms.InputTag('mkFitSiPixelHits'),
    mkFitStripHits = cms.InputTag('mkFitSiStripHits'),
    mkFitSeeds = cms.InputTag('mkFitSeedConverter'),
    src = cms.InputTag('mkFitProducer'),
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
    NavigationSchool = cms.ESInputTag('', 'SimpleNavigationSchool'),
    measurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
