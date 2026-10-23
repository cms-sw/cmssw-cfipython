import FWCore.ParameterSet.Config as cms

def MultiParticleInConeGunProducer(*args, **kwargs):
  mod = cms.EDProducer('MultiParticleInConeGunProducer',
    PGunParameters = cms.PSet(
      MinPt = cms.required.double,
      MaxPt = cms.required.double,
      InConeID = cms.required.vint32,
      MinDeltaR = cms.required.double,
      MaxDeltaR = cms.required.double,
      MinMomRatio = cms.required.double,
      MaxMomRatio = cms.required.double,
      InConeMinEta = cms.required.double,
      InConeMaxEta = cms.required.double,
      InConeMinPhi = cms.required.double,
      InConeMaxPhi = cms.required.double,
      InConeMaxTry = cms.required.uint32,
      PartID = cms.required.vint32,
      MinEta = cms.required.double,
      MaxEta = cms.required.double,
      MinPhi = cms.required.double,
      MaxPhi = cms.required.double
    ),
    Verbosity = cms.untracked.int32(0),
    AddAntiParticle = cms.required.bool,
    firstRun = cms.obsolete.untracked.uint32,
    psethack = cms.optional.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
