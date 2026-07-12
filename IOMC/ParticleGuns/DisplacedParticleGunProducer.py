import FWCore.ParameterSet.Config as cms

def DisplacedParticleGunProducer(*args, **kwargs):
  mod = cms.EDProducer('DisplacedParticleGunProducer',
    AddAntiParticle = cms.bool(False),
    PGunParameters = cms.PSet(
      MinPt = cms.double(5),
      MaxPt = cms.double(100),
      MinPhi = cms.double(-3.1415926535897931),
      MaxPhi = cms.double(3.1415926535897931),
      RMin = cms.double(0),
      RMax = cms.double(10),
      MinVtxPhi = cms.double(0),
      MaxVtxPhi = cms.double(6.2831853071795862),
      ZVtx = cms.double(0),
      NParticles = cms.int32(1),
      PartID = cms.int32(22),
      UniformDensityInR = cms.bool(False),
      MaxTries = cms.uint32(1000),
      PointingToHGCAL = cms.bool(True),
      RMinBackSurfaceHGCAL = cms.double(58.79),
      RMaxBackSurfaceHGCAL = cms.double(91.58),
      MinTheta = cms.double(-1.5707953267948966),
      MaxTheta = cms.double(1.5707953267948966),
      RestrictRInZPlaneAtZero = cms.bool(True),
      RMinAtZero = cms.double(0),
      RMaxAtZero = cms.double(150)
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
