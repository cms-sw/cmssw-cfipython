import FWCore.ParameterSet.Config as cms

def AllTrackToTruthBranchAssociatorsProducer(*args, **kwargs):
  mod = cms.EDProducer('AllTrackToTruthBranchAssociatorsProducer',
    src = cms.InputTag('truthLogicalGraphProducer'),
    hitIndex = cms.InputTag('truthLogicalGraphHitIndexProducer'),
    recoCollections = cms.VInputTag(),
    assignableTargetsSrc = cms.InputTag('truthBranchTargets', 'assignableRoots'),
    targetsSrc = cms.InputTag('truthBranchTargets', 'selectedRoots'),
    denominatorDetectors = cms.vstring(),
    truthToRecoSignalOnly = cms.bool(True),
    maxConstituentScore = cms.double(0.25),
    heavyFlavorOnly = cms.bool(False),
    workingPointNames = cms.vstring('Fixed'),
    adaptiveReverseWeight = cms.vfloat(0),
    adaptiveMaxReverseScore = cms.vfloat(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
