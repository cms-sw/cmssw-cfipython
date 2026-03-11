import FWCore.ParameterSet.Config as cms

def GaussRandomPThetaGunProducer(*args, **kwargs):
  mod = cms.EDProducer('GaussRandomPThetaGunProducer',
    PGunParameters = cms.PSet(
      MeanP = cms.required.double,
      SigmaP = cms.required.double,
      PartID = cms.required.vint32,
      MinTheta = cms.required.double,
      MaxTheta = cms.required.double,
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
