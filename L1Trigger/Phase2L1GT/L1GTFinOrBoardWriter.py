import FWCore.ParameterSet.Config as cms

def L1GTFinOrBoardWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('L1GTFinOrBoardWriter',
    filename = cms.required.untracked.string,
    fileExtension = cms.untracked.string('txt'),
    algoBlocksTag = cms.required.untracked.InputTag,
    channelsLow = cms.required.untracked.vuint32,
    channelsMid = cms.required.untracked.vuint32,
    channelsHigh = cms.required.untracked.vuint32,
    channelFinOr = cms.required.untracked.uint32,
    maxFrames = cms.untracked.uint32(1024),
    maxEvents = cms.untracked.uint32(0),
    patternFormat = cms.untracked.string('EMPv2'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
