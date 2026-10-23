import FWCore.ParameterSet.Config as cms

def AreaSeededTrackingRegionsEDProducer(*args, **kwargs):
  mod = cms.EDProducer('AreaSeededTrackingRegionsEDProducer',
    RegionPSet = cms.PSet(
      areas = cms.VPSet(
        template = cms.PSetTemplate(
          rmin = cms.double(0),
          rmax = cms.double(0),
          zmin = cms.double(0),
          zmax = cms.double(0),
          phimin = cms.double(0),
          phimax = cms.double(0)
        )
      ),
      operationMode = cms.string('BeamSpotFixed'),
      beamSpot = cms.InputTag('offlineBeamSpot'),
      vertexCollection = cms.InputTag('firstStepPrimaryVertices'),
      maxNVertices = cms.int32(-1),
      nSigmaZBeamSpot = cms.double(4),
      zErrorBeamSpot = cms.double(24.2),
      nSigmaZVertex = cms.double(3),
      zErrorVertex = cms.double(0.2),
      extraPhi = cms.double(0),
      extraEta = cms.double(0),
      ptMin = cms.double(0.9),
      originRadius = cms.double(0.2),
      precise = cms.bool(True),
      whereToUseMeasurementTracker = cms.string('Never'),
      measurementTrackerName = cms.InputTag(''),
      seedingMode = cms.string('Global'),
      input = cms.InputTag(''),
      deltaEta_Cand = cms.double(-1),
      deltaPhi_Cand = cms.double(-1),
      searchOpt = cms.bool(False)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
