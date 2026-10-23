import FWCore.ParameterSet.Config as cms

def ExpoRandomPtGunProducer(*args, **kwargs):
  mod = cms.EDProducer('ExpoRandomPtGunProducer',
    PGunParameters = cms.PSet(
      MinPt = cms.required.double,
      MaxPt = cms.required.double,
      MeanPt = cms.required.double,
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
