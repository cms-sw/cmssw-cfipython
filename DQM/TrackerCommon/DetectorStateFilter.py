import FWCore.ParameterSet.Config as cms

def DetectorStateFilter(*args, **kwargs):
  mod = cms.EDFilter('DetectorStateFilter',
    DebugOn = cms.untracked.bool(False),
    DetectorType = cms.untracked.string('sistrip'),
    acceptedCombinations = cms.untracked.vstring(),
    DcsStatusLabel = cms.untracked.InputTag('scalersRawToDigi'),
    DCSRecordLabel = cms.untracked.InputTag('onlineMetaDataDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
