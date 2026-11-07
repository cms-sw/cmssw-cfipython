import FWCore.ParameterSet.Config as cms

def MkFitIterationConfigESProducer(*args, **kwargs):
  mod = cms.ESProducer('MkFitIterationConfigESProducer',
    ComponentName = cms.string(''),
    config = cms.FileInPath(''),
    minPt = cms.double(0),
    maxClusterSize = cms.uint32(8),
    backwardSearchMinPixelLayers = cms.int32(0),
    backwardSearchPromptMaxD0 = cms.double(0),
    duplicateCleaningLowPtFraction = cms.double(0.1),
    duplicateCleaningLowPtRampStart = cms.double(5),
    duplicateCleaningLowPtRampEnd = cms.double(10),
    duplicateCleaningLowPtMaxRelDiffInvPt = cms.double(0.1),
    duplicateCleaningLowPtRequireSameCharge = cms.bool(True),
    duplicateCleaningLowPtMaxD0 = cms.double(2),
    duplicateCleaningLowPtMaxDRTimesPt = cms.double(0.1),
    duplicateCleaningMinUniqueHitsToKeep = cms.int32(9),
    duplicateCleaningMinPtUniqueHitsToKeep = cms.double(10),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
