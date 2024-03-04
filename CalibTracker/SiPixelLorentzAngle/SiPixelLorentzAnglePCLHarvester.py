import FWCore.ParameterSet.Config as cms

def SiPixelLorentzAnglePCLHarvester(**kwargs):
  mod = cms.EDProducer('SiPixelLorentzAnglePCLHarvester',
    newmodulelist = cms.vstring(),
    dqmDir = cms.string('AlCaReco/SiPixelLorentzAngle'),
    doChebyshevFit = cms.bool(False),
    order = cms.int32(5),
    fitChi2Cut = cms.double(20),
    fitRange = cms.vdouble(
      5,
      280
    ),
    minHitsCut = cms.int32(10000),
    record = cms.string('SiPixelLorentzAngleRcd'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
