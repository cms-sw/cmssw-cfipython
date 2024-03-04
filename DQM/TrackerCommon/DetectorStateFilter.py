import FWCore.ParameterSet.Config as cms

def DetectorStateFilter(**kwargs):
  mod = cms.EDFilter('DetectorStateFilter',
    DebugOn = cms.untracked.bool(False),
    DetectorType = cms.untracked.string('sistrip'),
    DcsStatusLabel = cms.untracked.InputTag('scalersRawToDigi'),
    DCSRecordLabel = cms.untracked.InputTag('onlineMetaDataDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
