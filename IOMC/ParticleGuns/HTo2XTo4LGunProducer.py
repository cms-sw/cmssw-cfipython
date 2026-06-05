import FWCore.ParameterSet.Config as cms

def HTo2XTo4LGunProducer(*args, **kwargs):
  mod = cms.EDProducer('HTo2XTo4LGunProducer',
    PGunParameters = cms.PSet(
      MinMassH = cms.required.double,
      MaxMassH = cms.required.double,
      MinPtH = cms.required.double,
      MaxPtH = cms.required.double,
      MinCTauLLP = cms.required.double,
      MaxCTauLLP = cms.required.double,
      LLPMassSpectrum = cms.string('flatMass'),
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
