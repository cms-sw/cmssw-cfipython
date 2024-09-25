import FWCore.ParameterSet.Config as cms

def HLTEcalIsolationFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTEcalIsolationFilter',
    saveTags = cms.bool(True),
    EcalIsolatedParticleSource = cms.InputTag('ecalIsolPartProd'),
    MaxNhitInnerCone = cms.int32(1000),
    MaxNhitOuterCone = cms.int32(0),
    MaxEnergyOuterCone = cms.double(10000),
    MaxEnergyInnerCone = cms.double(10000),
    MaxEtaCandidate = cms.double(1.3),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
