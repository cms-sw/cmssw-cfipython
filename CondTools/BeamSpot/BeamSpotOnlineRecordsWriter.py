import FWCore.ParameterSet.Config as cms

def BeamSpotOnlineRecordsWriter(**kwargs):
  mod = cms.EDAnalyzer('BeamSpotOnlineRecordsWriter',
    isHLT = cms.bool(True),
    InputFileName = cms.untracked.string(''),
    IOVStartRun = cms.untracked.uint32(1),
    IOVStartLumi = cms.untracked.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
