import FWCore.ParameterSet.Config as cms

def BeamSpotOnlineRecordsReader(**kwargs):
  mod = cms.EDAnalyzer('BeamSpotOnlineRecordsReader',
    isHLT = cms.bool(True),
    rawFileName = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
