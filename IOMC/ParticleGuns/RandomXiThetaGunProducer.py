import FWCore.ParameterSet.Config as cms

def RandomXiThetaGunProducer(*args, **kwargs):
  mod = cms.EDProducer('RandomXiThetaGunProducer',
    verbosity = cms.untracked.uint32(0),
    particleId = cms.required.uint32,
    energy = cms.required.double,
    xi_min = cms.required.double,
    xi_max = cms.required.double,
    theta_x_mean = cms.required.double,
    theta_x_sigma = cms.required.double,
    theta_y_mean = cms.required.double,
    theta_y_sigma = cms.required.double,
    nParticlesSector45 = cms.required.uint32,
    nParticlesSector56 = cms.required.uint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
