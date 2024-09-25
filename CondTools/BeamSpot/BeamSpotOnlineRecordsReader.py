import FWCore.ParameterSet.Config as cms

def BeamSpotOnlineRecordsReader(*args, **kwargs):
  mod = cms.EDAnalyzer('BeamSpotOnlineRecordsReader',
    isHLT = cms.bool(True),
    rawFileName = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
