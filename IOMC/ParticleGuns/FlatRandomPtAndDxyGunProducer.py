import FWCore.ParameterSet.Config as cms

def FlatRandomPtAndDxyGunProducer(*args, **kwargs):
  mod = cms.EDProducer('FlatRandomPtAndDxyGunProducer',
    PGunParameters = cms.PSet(
      MinPt = cms.required.double,
      MaxPt = cms.required.double,
      dxyMin = cms.required.double,
      dxyMax = cms.required.double,
      LxyMax = cms.required.double,
      LzMax = cms.required.double,
      ConeRadius = cms.required.double,
      ConeH = cms.required.double,
      DistanceToAPEX = cms.required.double,
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
