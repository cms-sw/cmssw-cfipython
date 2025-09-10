import FWCore.ParameterSet.Config as cms

def StudyCaloGen(*args, **kwargs):
  mod = cms.EDAnalyzer('StudyCaloGen',
    GenSrc = cms.untracked.string('genParticles'),
    UseHepMC = cms.untracked.bool(False),
    ChargedHadronSeedP = cms.untracked.double(1),
    PTMin = cms.untracked.double(1),
    MaxChargedHadronEta = cms.untracked.double(2.5),
    ConeRadius = cms.untracked.double(34.98),
    ConeRadiusMIP = cms.untracked.double(14),
    UseConeIsolation = cms.untracked.bool(True),
    PMaxIsolation = cms.untracked.double(5),
    Verbosity = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
