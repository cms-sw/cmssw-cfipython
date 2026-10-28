import FWCore.ParameterSet.Config as cms

def AllVertexToTruthBranchAssociatorsProducer(*args, **kwargs):
  mod = cms.EDProducer('AllVertexToTruthBranchAssociatorsProducer',
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
    constituentAssociator = cms.string('allTrackToTruthBranchAssociators'),
    constituentCollection = cms.string('generalTracks'),
    vertexResolution = cms.string('immediate'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
