import FWCore.ParameterSet.Config as cms

def FileRandomMultiParticlePGunProducer(*args, **kwargs):
  mod = cms.EDProducer('FileRandomMultiParticlePGunProducer',
    PGunParameters = cms.PSet(
      MinP = cms.required.double,
      MaxP = cms.required.double,
      FileName = cms.required.FileInPath,
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
