import FWCore.ParameterSet.Config as cms

def BeamSpotOnlineRecordsWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('BeamSpotOnlineRecordsWriter',
    isHLT = cms.bool(True),
    InputFileName = cms.untracked.string(''),
    IOVStartRun = cms.untracked.uint32(1),
    IOVStartLumi = cms.untracked.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
