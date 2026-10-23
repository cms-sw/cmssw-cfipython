import FWCore.ParameterSet.Config as cms

def BeamSpotOnlineShifter(*args, **kwargs):
  mod = cms.EDAnalyzer('BeamSpotOnlineShifter',
    isHLT = cms.bool(True),
    useFullPixel = cms.bool(False),
    xShift = cms.double(0),
    yShift = cms.double(0),
    zShift = cms.double(0),
    IOVStartRun = cms.untracked.uint32(1),
    IOVStartLumi = cms.untracked.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
