import FWCore.ParameterSet.Config as cms

def CloseByParticleGunProducer(**kwargs):
  mod = cms.EDProducer('CloseByParticleGunProducer',
    AddAntiParticle = cms.bool(False),
    PGunParameters = cms.PSet(
      ControlledByEta = cms.bool(False),
      ControlledByREta = cms.bool(False),
      Delta = cms.double(10),
      VarMax = cms.double(200),
      VarMin = cms.double(25),
      MaxVarSpread = cms.bool(False),
      LogSpacedVar = cms.bool(False),
      FlatPtGeneration = cms.bool(False),
      MaxEta = cms.double(2.7),
      MaxPhi = cms.double(3.14159265359),
      MinEta = cms.double(1.7),
      MinPhi = cms.double(-3.14159265359),
      NParticles = cms.int32(2),
      Overlapping = cms.bool(False),
      PartID = cms.vint32(22),
      Pointing = cms.bool(True),
      RMax = cms.double(120),
      RMin = cms.double(60),
      RandomShoot = cms.bool(False),
      ZMax = cms.double(321),
      ZMin = cms.double(320),
      UseDeltaT = cms.bool(False),
      TMin = cms.double(0),
      TMax = cms.double(0.05),
      OffsetFirst = cms.double(0)
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('random particles in phi and r windows'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod