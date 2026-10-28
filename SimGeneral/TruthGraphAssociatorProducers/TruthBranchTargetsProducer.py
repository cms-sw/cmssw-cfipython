import FWCore.ParameterSet.Config as cms

def TruthBranchTargetsProducer(*args, **kwargs):
  mod = cms.EDProducer('TruthBranchTargetsProducer',
    src = cms.InputTag('truthLogicalGraphProducer'),
    branchSelector = cms.PSet(
      ptMin = cms.float(1),
      ptMax = cms.float(3.40282347e+38),
      etaMin = cms.float(-4),
      etaMax = cms.float(4),
      pdgIds = cms.vint32(),
      signalOnly = cms.bool(False),
      intimeOnly = cms.bool(False),
      chargedOnly = cms.bool(False),
      invertEta = cms.bool(False),
      kinematicsOnStableOnly = cms.bool(True)
    ),
    assignableTargets = cms.PSet(
      excludeSynthetic = cms.bool(True),
      excludeBeamParticles = cms.bool(True),
      excludePartons = cms.bool(True),
      excludeElectroweakBosons = cms.bool(True),
      extraBarredPdgIds = cms.vint32()
    ),
    truthLevels = cms.vstring('caloBoundary'),
    signalSeedPdgIds = cms.vint32(),
    signalSeedHadronFlavors = cms.vint32(),
    truthToRecoSignalOnly = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
