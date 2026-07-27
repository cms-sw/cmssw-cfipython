import FWCore.ParameterSet.Config as cms

def DisplacedParticleGunProducer(*args, **kwargs):
  mod = cms.EDProducer('DisplacedParticleGunProducer',
    PGunParameters = cms.PSet(
      PartID = cms.required.int32,
      NParticles = cms.required.int32,
      Momentum = cms.PSet(
        Magnitude = cms.PSet(
          Variable = cms.required.string,
          Min = cms.required.double,
          Max = cms.required.double
        ),
        Direction = cms.PSet(
          ThetaMin = cms.required.double,
          ThetaMax = cms.required.double,
          PhiMin = cms.required.double,
          PhiMax = cms.required.double
        )
      ),
      Geometry = cms.PSet(
        RadialDistribution = cms.required.string,
        Origin = cms.PSet(
          RMin = cms.required.double,
          RMax = cms.required.double,
          PhiMin = cms.required.double,
          PhiMax = cms.required.double
        ),
        Production = cms.PSet(
          Z = cms.required.double,
          RMin = cms.required.double,
          RMax = cms.required.double,
          PhiMin = cms.required.double,
          PhiMax = cms.required.double
        ),
        Target = cms.PSet(
          Z = cms.required.double,
          RMin = cms.required.double,
          RMax = cms.required.double,
          PhiMin = cms.required.double,
          PhiMax = cms.required.double
        )
      ),
      MaxSamplingAttempts = cms.required.uint32
    ),
    Verbosity = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
