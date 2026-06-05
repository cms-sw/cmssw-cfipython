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
    calibrate = cms.bool(True),
    calibBinCenter = cms.vdouble(
      0.1704,
      0.6028,
      1.0188,
      1.2898,
      1.439,
      1.4908,
      1.55
    ),
    calibBinCoeff = cms.vdouble(
      1,
      1.0004,
      1.00014,
      1.0027,
      1.0029,
      1.0009,
      0.9999
    ),
    calibBinOffset = cms.vdouble(
      0.0016,
      0.0032,
      0.0033,
      0.0045,
      0.0005,
      0.0012,
      0.0003
    ),
    NavigationSchool = cms.ESInputTag('', 'SimpleNavigationSchool'),
    measurementTrackerEvent = cms.InputTag('MeasurementTrackerEvent'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
