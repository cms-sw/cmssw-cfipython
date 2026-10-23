import FWCore.ParameterSet.Config as cms

def RandomtXiGunProducer(*args, **kwargs):
  mod = cms.EDProducer('RandomtXiGunProducer',
    PGunParameters = cms.PSet(
      Mint = cms.required.double,
      Maxt = cms.required.double,
      MinXi = cms.required.double,
      MaxXi = cms.required.double,
      Log_t = cms.untracked.bool(False),
      PartID = cms.required.vint32,
      MinPhi = cms.required.double,
      MaxPhi = cms.required.double,
      ECMS = cms.required.double
    ),
    Verbosity = cms.untracked.int32(0),
    FireBackward = cms.required.bool,
    FireForward = cms.required.bool,
    firstRun = cms.obsolete.untracked.uint32,
    psethack = cms.optional.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
